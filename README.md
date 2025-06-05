# Employee dashboard

## Project Overview
This project contains a dashboard which allows managers to monitor employee performance and predicted recruitment risk. The dashboard:

- Visualizes the productivity of an individual employee or a team of employees.
- Displays either an employee’s likelihood of recruitment or the average recruitment risk for a team.

The data that feeds into the dashboard includes:
- A data entry form deployed to managers to record employees’ positive and negative performance events.
- A database named `employee_events` that stores inputs from the manager form.
- A machine learning model developed by a data scientist on your team, which predicts the likelihood of an employee being recruited by another company.

---

## Installation

1. Clone this repository: `git clone https://github.com/AndrejFTI/dsnd-dashboard-project`
2. Go into the repository: `cd dsnd-dashboard-project/`
3. Create and activate a virtual environment: `python -m venv venv` and then `venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. From project root, run: `python -m report.dashboard`
6. Go to `http://0.0.0.0:5002` in your browser to interact with the dashboard.

---

## Testing

If you make any changes, make sure to run the following (which also runs automatically using GitHub Actions): `pytest tests/test_employee_events.py`

---

## Repository Structure
```
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
```

---

## employee_events.db Schema Diagram

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
