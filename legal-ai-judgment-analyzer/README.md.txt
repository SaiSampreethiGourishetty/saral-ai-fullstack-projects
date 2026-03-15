
## Legal NLP Extraction

The AI service extracts structured information from court judgements:

- Case Title
- Judge Name
- Decision Outcome
- Case Summary

This mimics real legal document analysis pipelines used in legal AI systems.

## Tech Stack

Frontend  
Angular

Backend  
Spring Boot

AI Service  
Python Flask

## Architecture

Angular → Spring Boot → Python NLP Service

## Run Instructions

### 1 Start AI Service

cd ai-service
pip install -r requirements.txt
python analyze.py

### 2 Start Spring Boot

cd backend-springboot
mvn spring-boot:run

### 3 Start Angular

cd frontend-angular
npm install
ng serve

Open

http://localhost:4200