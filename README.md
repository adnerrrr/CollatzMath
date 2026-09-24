# 🖥️ Collatz Conjecture

![Python](https://img.shields.io/badge/Python-BFFF00?style=for-the-badge&logo=openjdk&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

> A system designed to try numbers and detect the highest they can go using Collatz Conjecture aswell as how many steps it would take to reach the number 1.

---

## 🎯 Purpose
The purpose of this project is to explore one of maths most intriguing problems. It's not expected to solve this conjecture, as it is only meant to check one number at a time.

## 🛠️ Technology
The simulator was entirely developed using *Python*.

## 🐳 How to run it using Docker (Recommended)

You will need Docker installed.

*1. Build the image:*
docker build -t collatzconjecture .  

*2. Execute the program (Windows):*
docker run --rm -it collatzconjecture
