# Software Engineering for Data Scientists

This repository contains starter code for the **Software Engineering for Data Scientists** final project. Please reference your course materials for documentation on this repository's structure and important files. Happy coding!

---

## Project Overview

### Business Scenario

You are a data scientist at a manufacturing company. Upper management is concerned about losing their top employees to competitors. To address this, your data team has implemented the following:

- A data entry form deployed to managers to record employees’ positive and negative performance events.
- A database named `employee_events` that stores inputs from the manager form.
- A machine learning model developed by a data scientist on your team, which predicts the likelihood of an employee being recruited by another company.

Your responsibility is to **build a dashboard that allows managers to monitor employee performance and predicted recruitment risk**. The dashboard must fulfill these business requirements:

- Visualize the productivity of an individual employee or a team of employees.
- Display either an employee’s likelihood of recruitment or the average recruitment risk for a team.

---

### Technical Scenario

Your company has multiple data science teams, each working with different databases. To ensure that business-critical datasets are both tested and accessible across teams:

- Each data team must publish Python APIs for their databases.
- For this project, you must develop SQL queries to generate key datasets.
- You must package these queries into a Python library so users can retrieve critical datasets without writing SQL.

Additionally, your team has a history of deploying dashboards using the **FastHTML** framework. Your tasks include:

- Familiarizing yourself with the existing FastHTML-based codebase and repository structure.
- Using Object-Oriented Programming principles to extend and customize existing Python classes to build your dashboard.

---

### Repository Structure
├── README.md
├── assets
│   ├── model.pkl
│   └── report.css
├── venv
├── python-package
│   ├── employee_events
│   │   ├── init.py
│   │   ├── employee.py
│   │   ├── employee_events.db
│   │   ├── query_base.py
│   │   ├── sql_execution.py
│   │   └── team.py
│   ├── requirements.txt
│   ├── setup.py
├── report
│   ├── base_components
│   │   ├── init.py
│   │   ├── base_component.py
│   │   ├── data_table.py
│   │   ├── dropdown.py
│   │   ├── matplotlib_viz.py
│   │   └── radio.py
│   ├── combined_components
│   │   ├── init.py
│   │   ├── combined_component.py
│   │   └── form_group.py
│   ├── dashboard.py
│   └── utils.py
├── requirements.txt
├── start
├── tests
   └── test_employee_events.py


---

### employee_events.db Schema Diagram

```mermaid
erDiagram

  employee {
    INTEGER employee_id PK
    TEXT first_name
    TEXT last_name
    INTEGER team_id
  }

  employee_events {
    TEXT event_date
    INTEGER employee_id FK
    INTEGER team_id FK
    INTEGER positive_events
    INTEGER negative_events
  }

  notes {
    INTEGER employee_id PK
    INTEGER team_id PK
    TEXT note
    TEXT note_date PK
  }

  team {
    INTEGER team_id PK
    TEXT team_name
    TEXT shift
    TEXT manager_name
  }

  team ||--o{ employee_events : "team_id"
  employee ||--o{ employee_events : "employee_id"
  notes }o--o{ employee_events : ""