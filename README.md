# 🚗 AMG Car Rental System

A comprehensive car rental management system built with Django, featuring user authentication, car browsing, booking management, payment processing with Stripe, and an admin analytics dashboard.

![Django](https://img.shields.io/badge/Django-3.0.5-green.svg)
![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Heroku](https://img.shields.io/badge/Deploy-Heroku-purple.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Database Models](#-database-models)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Customer Features
- 🔐 **User Authentication** - Register, login, and manage user profiles
- 🚙 **Car Browsing** - Browse available cars with detailed specifications
- 📅 **Booking System** - Select rental dates with blocked date detection
- 📍 **Pickup Locations** - Choose from multiple pickup locations
- 🛡️ **Insurance & Fuel Options** - Add optional insurance and fuel packages
- 💳 **Stripe Payment Integration** - Secure credit card payment processing
- 📧 **Email Notifications** - Contact form and booking confirmations
- 📄 **PDF Invoice Generation** - Download rental invoices as PDF
- 🖼️ **Car Gallery** - View high-quality images of all available cars

### Business/Admin Features
- 📊 **Analytics Dashboard** - Visualize revenue, popular cars, and pickup locations
- ➕ **Car Management** - Add, update, and delete car listings
- 👥 **Customer Management** - View customer profiles and order history
- 📈 **Revenue Tracking** - Daily earnings and order statistics

---

## 📸 Screenshots

The application includes several key pages:

| Page | Description |
|------|-------------|
| **Home Page** | Landing page with car carousel and quick search |
| **Car Details** | Detailed car specifications with image gallery |
| **Car Listing** | Filterable list of available cars |
| **Booking Confirmation** | Order summary before payment |
| **Admin Dashboard** | Analytics and management interface |

*Screenshots are available in the `/screenshot` directory.*

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 3.0.5
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Authentication:** Django Built-in Auth with Custom User Model
- **Payment:** Stripe API

### Frontend
- **Templates:** Django Template Language (DTL)
- **CSS:** Custom CSS with Bootstrap integration
- **JavaScript:** jQuery for AJAX and dynamic content

### Additional Libraries
| Package | Version | Purpose |
|---------|---------|---------|
| `django-filter` | 2.2.0 | Advanced filtering |
| `Pillow` | 10.1.0 | Image processing |
| `stripe` | 2.50.0 | Payment processing |
| `xhtml2pdf` | 0.2.4 | PDF generation |
| `reportlab` | 4.0.0 | PDF creation |
| `whitenoise` | 5.2.0 | Static file serving |
| `gunicorn` | 20.0.4 | WSGI HTTP Server |

---

## 📁 Project Structure

```
car-rental/
├── AMG/                        # Main Django project configuration
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py                 # WSGI entry point
│   └── asgi.py                 # ASGI entry point
│
├── rent_car/                   # Primary car rental application
│   ├── models.py               # User, UserProfile, CarRent models
│   ├── views.py                # Main views and business logic
│   ├── forms.py                # User and car rental forms
│   ├── urls.py                 # App URL routing
│   ├── templates/              # HTML templates
│   │   ├── demo-business.html
│   │   ├── demo-business-login.html
│   │   ├── demo-business-register.html
│   │   └── ...
│   └── static/                 # Static assets (CSS, JS, images)
│
├── website/                    # Secondary website application
│   ├── models.py               # Car, Order, Customer, Location models
│   ├── views.py                # Website views
│   ├── forms.py                # Website forms
│   └── utilitiesViews.py       # PDF generation utilities
│
├── graph/                      # Analytics dashboard application
│   └── views.py                # Dashboard and graph views
│
├── templates/                  # Shared templates
│   ├── home.html               # Main homepage
│   ├── car.html                # Car details page
│   ├── renting.html            # Booking page
│   ├── confir.html             # Confirmation page
│   └── graph.html              # Analytics dashboard
│
├── static/                     # Global static files
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript files
│   └── images/                 # Image assets
│
├── media/                      # User-uploaded files
├── screenshot/                 # Application screenshots
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku deployment config
├── runtime.txt                 # Python runtime version
└── manage.py                   # Django management script
```

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/car-rental.git
   cd car-rental
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv car_env
   car_env\Scripts\activate

   # Linux/macOS
   python3 -m venv car_env
   source car_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root or set these environment variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Stripe Payment (Required for payments)
STRIPE_API_KEY=sk_test_your_stripe_secret_key

# Email Settings (Optional)
EMAIL_HOST=localhost
EMAIL_PORT=1025
EMAIL_HOST_USER=
EMAIL_USE_TLS=False
```

### Stripe Configuration

1. Create a [Stripe account](https://stripe.com/)
2. Get your API keys from the Stripe Dashboard
3. Update `views.py` in the website app:
   ```python
   stripe.api_key = 'your_stripe_secret_key'
   ```

### Database Configuration

By default, SQLite is used. For production, configure PostgreSQL:

```python
# AMG/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📖 Usage

### For Customers

1. **Register/Login** - Create an account or login
2. **Browse Cars** - View available cars with specifications
3. **Select Date Range** - Choose pickup and return dates
4. **Add Options** - Select insurance and fuel options
5. **Confirm Booking** - Review order details
6. **Make Payment** - Complete payment via Stripe
7. **Download Invoice** - Get PDF receipt

### For Administrators

1. **Access Admin Panel** - Go to `/admin/`
2. **Manage Cars** - Add/edit/delete car listings
3. **View Orders** - Monitor all bookings
4. **Analytics Dashboard** - Access at `/graph/` to view:
   - Daily revenue charts
   - Popular car models
   - Most used pickup locations

---

## 🔗 API Endpoints

### Authentication
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | GET, POST | User registration |
| `/buslogin` | GET, POST | User login |
| `/logout/` | GET | User logout |

### Profile Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/profile/` | GET | View user profile |
| `/profile/update/` | GET, POST | Update profile |
| `/change-password/` | GET, POST | Change password |

### Car Rentals
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/car-rents/` | GET | List all cars |
| `/car-rents/new/` | GET, POST | Create new listing |
| `/car-rents/<id>/` | GET | Car details |
| `/car-rents/<id>/edit/` | GET, POST | Update car |
| `/car-rents/<id>/delete/` | POST | Delete car |

### Booking
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/createOrder/<pk>/` | GET | Create booking |
| `/makeOrder/<pk>/` | POST | Confirm booking |
| `/payment/<pk>/` | POST | Process payment |
| `/cancelOrder/<pk>/` | POST | Cancel order |

### Utilities
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/pdfView/<pk>/` | GET | View invoice PDF |
| `/pdfDownload/<pk>/` | GET | Download invoice PDF |
| `/graph` | GET | Analytics dashboard |

---

## 📊 Database Models

### User Model (Custom)
```python
class User(AbstractUser):
    pass  # Extends Django's AbstractUser
```

### UserProfile
```python
class UserProfile(models.Model):
    user = ForeignKey(User)
    full_name = CharField(max_length=255)
    mobile_number = CharField(max_length=20)
    image = ImageField(upload_to='profile_images/')
    address = TextField()
```

### CarRent
```python
class CarRent(models.Model):
    name = CharField(max_length=100)
    model = CharField(max_length=100)
    color = CharField(max_length=50)
    number_plate = CharField(max_length=50)
    topspeed = IntegerField()
    date_from = DateField()
    date_to = DateField()
    insurance = BooleanField(default=False)
    seats = IntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)
    image1-5 = ImageField(upload_to='car_images/')
```

### Order
```python
class Order(models.Model):
    customer = CharField(max_length=70)
    customerID = CharField(max_length=50)
    carModel = CharField(max_length=70)
    automobileId = CharField(max_length=10)
    price = IntegerField()
    startRent = DateField()
    endRent = DateField()
    orderDate = DateTimeField(auto_now_add=True)
    pickUp = ForeignKey(Location)
    fullFuel = BooleanField(default=False)
    insurance = BooleanField(default=False)
    payed = BooleanField(default=False)
```

---

## 🌐 Deployment

### Heroku Deployment

1. **Install Heroku CLI** and login
   ```bash
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Add PostgreSQL addon**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set STRIPE_API_KEY=your-stripe-key
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Files for Deployment
- `Procfile` - Specifies the web server command
- `runtime.txt` - Specifies Python version
- `requirements.txt` - Lists all dependencies

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Developer** - *Initial work*

---

## 🙏 Acknowledgments

- Django Documentation
- Stripe API Documentation
- Bootstrap Framework
- Font Awesome Icons

---

<p align="center">
  Made with ❤️ using Django
</p>
