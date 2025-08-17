# 🌊 WaveNet – Real-Time Hand Gesture Recognition with Agentic AI

WaveNet is an **AI-powered prototype** that translates **hand gestures into alphabet letters** in real time using **OpenCV** and **MediaPipe**.  
Built for **A2HackFest 2025**, WaveNet demonstrates how **computer vision + Agentic AI (via qRaptor)** can break communication barriers for the **deaf and hard-of-hearing community**.

---

## 🚀 Overview
Globally, millions of people depend on **sign language**, but communication is limited because very few outside the community understand it.  
This creates barriers in **education, healthcare, workplaces, and daily interactions**.  

**WaveNet** is designed as a solution:  
- Captures **hand gestures** via webcam.  
- Uses **MediaPipe hand tracking** + **custom gesture logic** to detect finger positions.  
- Maps gestures to **alphabet letters** (A, B, D, L, W, 5 in prototype).  
- With **qRaptor**, it will be extended into a **real-time Agentic AI app** that translates gestures into **text + speech output**.  

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- [OpenCV](https://opencv.org/) – computer vision  
- [MediaPipe](https://mediapipe.dev/) – real-time hand tracking  
- [FastAPI](https://fastapi.tiangolo.com/) – API integration (ready for deployment)  
- **qRaptor** – Agentic AI orchestration and deployment  

---

## ⚡ Key Features
- 🎥 **Real-time webcam tracking** with hand landmarks  
- ✋ **Finger state analysis** for gesture classification  
- 🔤 Supports gestures for **A, B, D, L, W, 5** (extendable to full alphabet)  
- 🗣️ **Planned integration with Text-to-Speech (TTS)** via qRaptor agents  
- 🌐 **Agent Orchestration with qRaptor**:  
  - Gesture Recognition Agent → Language Agent → TTS Agent  
  - Seamless workflow orchestration in a drag-and-drop interface  
  - One-click cloud deployment for universal accessibility  

---

## 🎯 Use Case
WaveNet is a foundation for a **gesture-to-speech communication bridge**:  
1. **Input** → Hand gestures via webcam  
2. **Processing** → Gesture Recognition Agent (detects letters) → Language Agent (forms words/sentences)  
3. **Output** → Text + real-time speech (via TTS Agent)  

This pipeline, orchestrated in **qRaptor**, enables **inclusive, real-time conversations** between signers and non-signers.  

---

## 🖼️ Demo
👉 

---

## 📦 Installation (Prototype)

Clone the repo and install dependencies:

```bash
git clone https://github.com/<xhrivas>/WaveNet.git
cd WaveNet
pip install -r requirements.txt
