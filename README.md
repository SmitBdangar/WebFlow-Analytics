# 🔗 WebFlow Analytics

A Django-based link tracking system with real-time geolocation monitoring and a modern glassmorphism interface. Perfect for tracking link clicks with detailed analytics including IP addresses, geographic locations, and device information.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)

## ✨ Features

- 🔐 **Secure Authentication System** - Protected dashboard with user authentication
- 🎯 **Unique Tracking Links** - Generate custom tracking links with case identifiers
- 🌍 **Real-time Geolocation** - Automatic IP geolocation with city, region, and coordinates
- 📊 **Live Dashboard** - Monitor all clicks in real-time with detailed analytics
- 📱 **Mobile-First Design** - Optimized for mobile devices (95% of users)
- 🎨 **Glassmorphism UI** - Modern, beautiful interface with glass-morphic effects
- 🚀 **Production Ready** - Configured for Railway deployment with WhiteNoise

## 🎯 Use Cases

- **Marketing Campaigns** - Track link performance across different channels
- **Investigation Tools** - Monitor and log access to specific resources
- **Analytics Research** - Gather geographic and device data from visitors
- **Educational Projects** - Learn Django, geolocation APIs, and web tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 📖 Usage Guide

### 1. Login
Navigate to `/login/` and enter your credentials.

### 2. Generate Tracking Link
1. Enter a unique **Case Identifier** (e.g., "Campaign-2025")
2. Click **INITIATE GENERATION**
3. Copy the generated tracking link

### 3. Share and Monitor
- Share the tracking link with your audience
- Monitor clicks in real-time on the dashboard
- View detailed information:
  - Timestamp of each click
  - IP address
  - Geographic location (city, region, country)
  - GPS coordinates (latitude/longitude)
  - User agent (device/browser information)

## 🗄️ Database Models

### Link Model
```python
- slug: Unique identifier (10 characters)
- creator: User who created the link
- created_at: Creation timestamp
- case_name: Custom identifier for the link
- note: Optional notes
```

### Click Model
```python
- link: Foreign key to Link
- ts: Click timestamp
- ip: Client IP address
- user_agent: Browser/device information
- city: City name from geolocation
- region: Region/state name
- country: Country name
- latitude: GPS latitude
- longitude: GPS longitude
```

## 🌍 Geolocation

The system uses [ipapi.co](https://ipapi.co/) free API for IP geolocation:
- **Free tier**: 1,000 requests per day
- **No API key required**
- **Automatic fallback** for local/private IPs

### Supported Data
- City, Region, Country
- Latitude and Longitude coordinates
- Automatic handling of private IP addresses

## 📁 Project Structure

```
webflow-analytics/
├── tracker/                  # Main Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   └── tracker/
│   │       ├── login.html   # Login page
│   │       ├── main.html    # Dashboard
│   │       └── public_page.html
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── urls.py              # URL routing
│   └── admin.py             # Admin configuration
├── webflow/                 # Project settings
│   ├── settings.py          # Main settings
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI config
├── static/                  # Static files
│   └── images/              # Background images
├── staticfiles/             # Collected static files (generated)
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── Procfile                 # Railway/Heroku config
└── README.md                # This file
```

### Privacy & Legal

⚠️ **IMPORTANT**: This tool tracks user IP addresses and location data. Ensure you:
- Comply with GDPR, CCPA, and local privacy laws
- Provide clear privacy policies
- Obtain necessary user consent
- Implement data retention policies
- Secure all collected data

## 🛠️ Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🐛 Troubleshooting

### Common Issues

**Static files not loading:**
```bash
python manage.py collectstatic --noinput
```

**Database errors:**
```bash
python manage.py migrate
```

**Geolocation not working:**
- Check internet connection
- Verify IP is not private/local
- Check ipapi.co rate limits (1000/day free)

## 📝 Requirements

```
Django>=5.2
gunicorn>=21.2.0
whitenoise>=6.6.0
requests>=2.31.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

**This project is created for educational purposes only.** It demonstrates Django web development, tracking systems, and geolocation integration. Not intended for production use without proper security audits and legal compliance reviews.

---

**Made for educational purposes**
