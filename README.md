# WebFlow Analytics

A Django-based link tracking system with geolocation monitoring and a terminal-inspired interface.

## Features

- Generate unique tracking links with case identifiers
- Real-time click monitoring with IP geolocation
- Terminal-style UI (green/white/red color scheme)
- Secure authentication system
- Mobile-responsive design

## Installation

### 1. Clone and Setup

```bash
git clone <your-repository-url>
cd webflow-analytics
python -m venv venv

# Activate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install Django gunicorn whitenoise requests
```

### 3. Configure Settings

Edit `webflow/settings.py`:

```python
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

### 4. Setup Database

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

## Running

```bash
python manage.py runserver
```

Access at `http://127.0.0.1:8000/`

## Usage

1. **Login** at `/login/` with your credentials
2. **Generate Link**: Enter case ID → Click "INITIATE GENERATION" → Copy link
3. **Monitor Clicks**: View real-time data on dashboard with timestamps, IPs, locations, and coordinates

## Database Models

**Link**: slug, creator, created_at, case_name, note

**Click**: link, timestamp, ip, user_agent, city, region, country, latitude, longitude

## Geolocation

Uses [ipapi.co](https://ipapi.co/) free API (1,000 requests/day).

## Customization

Edit colors in `static/main-styles.css`:
```css
--primary-green: #00FF00;
--primary-white: #FFFFFF;
--primary-red: #FF0000;
--background: #000000;
```

## ⚠️ Educational Purpose Only

This project is created solely for educational purposes to demonstrate Django web development, tracking systems, and geolocation integration. Not intended for production use.
