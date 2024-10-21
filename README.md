# Food API

## Overview

The Food API is a RESTful web service built using Django and Django Rest Framework. It provides endpoints for managing chefs and users, as well as dishes, ingredients, ratings, and recommendations. This API is designed for applications focused on food, recipes, and culinary experiences.

## Features

- **Custom User Model**: A custom user model with roles (User, Chef) to distinguish between regular users and chefs.
- **Dish Management**: Create, read, update, and delete dishes, including details such as preparation methods and images.
- **Ingredient Management**: Manage ingredients associated with each dish.
- **Rating System**: Users can rate dishes on a scale from 1 to 5 and provide reviews.
- **Recommendations**: Users can recommend dishes with optional comments.
- **Role-based Permissions**: Custom permissions to restrict certain actions based on user roles.

## Technologies Used

- Django
- Django Rest Framework
- Python 3.x
- SQLite (or any other database you prefer)
- Django Admin for easy management of models

## Installation

### Prerequisites

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- pip (Python package installer).

### Clone the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/Local-Culinary-Explorer-API
