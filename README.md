# AI Drone Simulation (AirSim + Unreal Engine)

---

## 🇷🇺 Русская версия

### 📌 Описание проекта
Данный проект представляет собой симуляцию автономного движения квадрокоптера в виртуальной среде с использованием Unreal Engine и плагина AirSim.

Дрон запускается на карте Blocks и выполняет хаотичное движение в трёхмерном пространстве. Управление осуществляется через Python API AirSim.

Проект демонстрирует интеграцию AirSim с Unreal Engine, управление дроном через код и базовую логику автономного поведения.

Цель проекта — изучение принципов симуляции БПЛА и подготовка к разработке более сложных алгоритмов (навигация, компьютерное зрение, AI).

---

### ⚙️ Требования

**ПО:**
- Unreal Engine 4.27+
- AirSim
- Python 3.8+
- Visual Studio Code

**Зависимости:**
pip install -r requirements.txt

или:
pip install airsim numpy opencv-python

---

### 🚀 Инструкция запуска

1. Клонировать репозиторий:
git clone https://github.com/your-username/dron-project.git  
cd dron-project  

2. Запустить Unreal Engine:
- открыть карту Blocks  
- нажать Play  

3. Запустить скрипт:
python src/main.py  

---

### 🧪 Примеры использования

Запуск:
python src/main.py  

Автономное движение:
python src/drone_auto.py  

Пример API:
client.moveByVelocityAsync(1, 0, 0, 2)  

Получение состояния:
client.getMultirotorState()  

---

### 📂 Структура проекта

dron-project/  
│  
├── src/  
│   ├── main.py  
│   ├── drone.py  
│   ├── drone_auto.py  
│   └── test.py  
│  
├── requirements.txt  
├── README.md  
├── .gitignore  

---

### 📌 Примечания
Проект является базовой реализацией. Возможные улучшения:
- автономная навигация  
- компьютерное зрение  
- AI-управление  
- планирование траекторий  

---

## 🇬🇧 English Version

### 📌 Project Description
This project implements a simulation of autonomous drone movement in a virtual environment using Unreal Engine and the AirSim plugin.

The drone operates on the Blocks map and performs random movement in 3D space. Control is implemented via the AirSim Python API.

The project demonstrates AirSim integration, drone control via code, and basic autonomous behavior.

The goal is to explore UAV simulation fundamentals and serve as a base for advanced systems (navigation, computer vision, AI).

---

### ⚙️ Requirements

**Software:**
- Unreal Engine 4.27+
- AirSim
- Python 3.8+
- Visual Studio Code

**Dependencies:**
pip install -r requirements.txt

or:
pip install airsim numpy opencv-python

---

### 🚀 Run Instructions

1. Clone repository:
git clone https://github.com/your-username/dron-project.git  
cd dron-project  

2. Start Unreal Engine:
- open Blocks map  
- press Play  

3. Run script:
python src/main.py  

---

### 🧪 Usage Examples

Run:
python src/main.py  

Autonomous mode:
python src/drone_auto.py  

Example:
client.moveByVelocityAsync(1, 0, 0, 2)  

State:
client.getMultirotorState()  

---

### 📂 Project Structure

dron-project/  
│  
├── src/  
│   ├── main.py  
│   ├── drone.py  
│   ├── drone_auto.py  
│   └── test.py  
│  
├── requirements.txt  
├── README.md  
├── .gitignore  

---

### 📌 Notes
This is a basic implementation. Possible improvements:
- autonomous navigation  
- computer vision  
- AI-based control  
- trajectory planning  