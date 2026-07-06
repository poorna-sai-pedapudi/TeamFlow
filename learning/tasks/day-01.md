Sprint 1 - Day 1
Theme: Laying the Foundation of a Production Backend
Estimated Time: ~7 hours

👨‍💻 Poorna Task 1 — Product & Architecture Planning (60 min)
Objective
Before writing a single line of backend code, understand what you're building.
Your Assignment
We are building TeamFlow, a multi-tenant SaaS project management platform.
Think about these questions and write your answers in docs/architecture/system-overview.md.
What problem does TeamFlow solve?
Who are the users?
What are the main entities in the system?
What is Multi-Tenancy?
Why should Organizations own Projects instead of Users?
Draw a simple relationship diagram.
Example (don't copy directly):
Organization
     │
     ├── Users
     │
     ├── Projects
     │      │
     │      ├── Tasks
     │      └── Comments
     │
     └── Audit Logs
Think Before Coding
Could Projects exist without Organizations?
Can a User belong to multiple Organizations?
How does GitHub handle organizations?
What happens when an Organization is deleted?

Claude Planning Prompt
I'm designing the architecture for a production-grade project management SaaS called TeamFlow.

Review my proposed entities and relationships.

Identify missing entities, scalability concerns, multi-tenancy issues, and suggest improvements without writing implementation code.

👨‍💻 Poorna Task 2 — Backend Initialization (90 min)
Objective
Create the backend properly.
No business logic yet.
Initialize:
FastAPI
SQLAlchemy
Alembic
Environment configuration
Configuration management
Dependency management
Deliverables
By the end:
uvicorn backend.app.main:app --reload
should run successfully.
Swagger should open.
Nothing else.

Before Coding
Answer:
Why use FastAPI?
Why SQLAlchemy?
Why Alembic instead of Base.metadata.create_all()?
Why keep configuration in .env?
Write your answers first.

Claude Review Prompt
Review my backend project initialization.

Focus on project structure, dependency management, scalability, maintainability, and production readiness.

Do not rewrite everything unless there are architectural problems.

👨‍💻 Poorna Task 3 — PostgreSQL + Alembic (90 min)
Objective
Today we stop manually creating tables forever.
Set up:
PostgreSQL connection
SQLAlchemy Engine
Session management
Base model
Alembic initialization
First migration
Don't create User yet.
Create one simple table:
organizations
Fields:
id

name

created_at
Nothing more.

Think First
Answer:
Why is Alembic used in production?
What happens if 20 developers all change models?
Why are migrations version controlled?

Claude Architecture Prompt
Review my SQLAlchemy and Alembic setup.

Would this scale for a production backend with multiple developers?

Identify improvements while keeping the implementation beginner-friendly.

👨‍💻 Poorna Task 4 — React Initialization (45 min)
We are NOT learning frontend.
We're learning backend integration.
Initialize React.
Create:
frontend/

src/

App.jsx
Display:
Welcome to TeamFlow
Backend Status:
No backend integration yet.
Tomorrow we'll connect FastAPI.

🧠 Harish Task 1 — Backend Engineering Deep Dive (45 min)
Topic
What Actually Happens When You Type:
GET /organizations
I want you to understand the complete lifecycle.
Study:
Browser

↓

DNS

↓

TCP Handshake

↓

HTTP Request

↓

FastAPI Router

↓

Dependency Injection

↓

Service Layer

↓

Repository

↓

SQLAlchemy

↓

PostgreSQL

↓

JSON

↓

HTTP Response
At the end, explain the entire flow in your own words in docs/architecture/request-lifecycle.md.

🧠 Harish Task 2 — System Design (60 min)
Topic
Design GitHub Organizations.
Questions:
Why Organizations?
Why Teams?
Why Permissions?
Can Users belong to multiple Organizations?
Database relationships?
Draw the ER Diagram.
No code.
Pure architecture.

🧠 Harish Task 3 — DSA (45 min)
Topic:
Hash Maps
Problems:
Two Sum
Valid Anagram
Requirements:
Solve yourself.
Explain time complexity.
Explain why Hash Maps are preferred.
Then answer:
Where would Hash Maps naturally appear in backend systems?

🧠 Harish Task 4 — Interview Mastery (45 min)
This is one of the most important daily habits.
Pretend I am the Hiring Manager.
Answer these questions in your own words:
Tell me about TeamFlow.
Why did you choose PostgreSQL?
Why FastAPI instead of Flask?
Why Alembic?
Why Organizations instead of Users owning Projects?
Record yourself speaking if possible. Don't memorize answers—focus on explaining your reasoning naturally.

📘 Learning Journal (15 min)
Complete today's entry:
Sprint 1 – Day 1

1. What did I build today?

2. What backend engineering concept clicked today?

3. What was the hardest part?

4. If this system had 10 million users, what would break first?

5. What interview question can I confidently answer now?

6. One thing I want to improve tomorrow.

📦 Git Commits
Aim for meaningful commits rather than one big commit.
git checkout -b feature/sprint1-day1

git commit -m "docs: add TeamFlow system architecture"

git commit -m "feat: initialize FastAPI backend"

git commit -m "feat: configure SQLAlchemy and Alembic"

git commit -m "feat: initialize React frontend"

🎯 Sprint 1 Goal
By the end of tomorrow, you won't have built many features—and that's intentional.
Instead, you'll have built the foundation correctly:
A well-thought-out product design.
A clean backend architecture.
A production-ready project structure.
Version-controlled database migrations.
A React application ready to integrate.
Documentation explaining your design decisions.
Every feature we build from Day 2 onward will stand on this foundation.

