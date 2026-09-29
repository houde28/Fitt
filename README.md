# Fitt

A Django web app for tracking daily fitness — what you eat, how you train, and how it adds up over time.

## Status

Early-stage and actively in development. Core logging features work locally, but the app isn't deployed yet. I'm currently working on setting up CI/CD for it.

## What It Does

Fitt lets users log their daily meals, workouts, and exercises, and see everything for a given day in one place. Workouts contain exercises, and days contain both workouts and meals, so a full day is easy to track and look back on.

## Features

- User authentication
- CRUD for daily logs, workouts, exercises, and meals
- Single-day view showing all workouts, exercises, and meals together
- Relational data model linking days, workouts, exercises, and meals

## Planned Features

- Goal setting (weight, macros, activity targets)
- Macronutrient calculator based on body weight, height, and other inputs
- CI/CD pipeline and deployment

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development)
- **Frontend:** HTML, CSS (Django Templates)
- **Authentication:** Django's built-in auth system
- **Version Control:** Git, GitHub

## Why I Built This

I wanted a project outside of school where I could really dig into one framework and build something on my own, from the data model up to the UI. It's also been a good way to learn deployment and CI/CD, which I didn't get much of in my classes.