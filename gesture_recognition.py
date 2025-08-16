import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Finger tip landmark indices
tip_ids = [4, 8, 12, 16, 20]

def get_finger_states(lm_list):
    """Returns list of finger states: 1 for open, 0 for closed."""
    fingers = []

    # Thumb
    if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers
    for id in range(1, 5):
        if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

def classify_gesture(fingers):
    """Maps finger states to simple gestures/letters."""
    if fingers == [0, 0, 0, 0, 0]:
        return "A"   # Fist
    elif fingers == [0, 1, 1, 1, 1]:
        return "B"   # Open hand
    elif fingers == [0, 1, 0, 0, 0]:
        return "D"   # Index finger up
    else:
        return "-"   # Unknown

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            h, w, _ = img.shape
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

            if lm_list:
                fingers = get_finger_states(lm_list)
                letter = classify_gesture(fingers)
                cv2.putText(img, f'Letter: {letter}', (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Recognition Prototype", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
