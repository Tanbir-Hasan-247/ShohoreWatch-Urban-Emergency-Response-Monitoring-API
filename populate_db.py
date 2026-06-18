import os
import django
import random
from datetime import timedelta
from django.utils import timezone

# প্রোজেক্টের নাম অনুযায়ী সেটিংস কনফিগার করুন (প্রয়োজনে 'ShohoreWatch' পরিবর্তন করুন)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShohoreWatch.settings')
django.setup()

# মডেলগুলো ইমপোর্ট করুন (আপনার অ্যাপের নাম অনুযায়ী ইমপোর্ট পাথ ঠিক করে নেবেন)
from django.contrib.auth import get_user_model
from users.models import CitizenProfile, OfficialProfile, ResponderProfile # Profile models
from zones.models import Zone
from alerts.models import AlertCategory, Alert, AlertUpdate

User = get_user_model()

def populate():
    print("Database Population Started...")

    # 1. Create Zones
    zones_data = [
        {"name": "Gulshan", "code": "Z-GUL", "city": "Dhaka", "population": 250000},
        {"name": "Dhanmondi", "code": "Z-DHA", "city": "Dhaka", "population": 300000},
        {"name": "Mirpur", "code": "Z-MIR", "city": "Dhaka", "population": 600000},
        {"name": "Uttara", "code": "Z-UTT", "city": "Dhaka", "population": 400000},
        {"name": "Banani", "code": "Z-BAN", "city": "Dhaka", "population": 150000},
    ]
    zones = []
    for z_data in zones_data:
        zone, created = Zone.objects.get_or_create(code=z_data['code'], defaults=z_data)
        zones.append(zone)
    print("✅ 5 Zones Created/Checked.")

    # 2. Create Alert Categories
    categories_data = [
        {"name": "Fire Accident", "slug": "fire-accident", "severity_default": 5, "response_time_default": 10, "icon": "fire", "color_hex": "#FF0000"},
        {"name": "Medical Emergency", "slug": "medical-emergency", "severity_default": 4, "response_time_default": 15, "icon": "ambulance", "color_hex": "#FF0000"},
        {"name": "Waterlogging", "slug": "waterlogging", "severity_default": 3, "response_time_default": 120, "icon": "water", "color_hex": "#0000FF"},
        {"name": "Crime & Theft", "slug": "crime-theft", "severity_default": 4, "response_time_default": 20, "icon": "shield", "color_hex": "#000000"},
        {"name": "Road Crash", "slug": "road-crash", "severity_default": 5, "response_time_default": 15, "icon": "car-crash", "color_hex": "#FF6600"},
    ]
    categories = []
    for c_data in categories_data:
        category, created = AlertCategory.objects.get_or_create(slug=c_data['slug'], defaults=c_data)
        categories.append(category)
    print("✅ 5 Alert Categories Created/Checked.")

    # 3. Create Users & Profiles (1 Admin, 2 Officials, 3 Responders, 4 Citizens)
    users = {'admin': [], 'official': [], 'responder': [], 'citizen': []}
    roles_distribution = [
        ("admin@test.com", User.ADMIN),
        ("off1@test.com", User.OFFICIAL), ("off2@test.com", User.OFFICIAL),
        ("resp1@test.com", User.RESPONDER), ("resp2@test.com", User.RESPONDER), ("resp3@test.com", User.RESPONDER),
        ("cit1@test.com", User.CITIZEN), ("cit2@test.com", User.CITIZEN), ("cit3@test.com", User.CITIZEN), ("cit4@test.com", User.CITIZEN)
    ]
    
    for email, role in roles_distribution:
        user, created = User.objects.get_or_create(email=email)
        if created:
            user.set_password("password123") # Default password for testing
            user.role = role
            user.zone = random.choice(zones)
            user.save()

        # Safely create or get specific profiles based on role to avoid IntegrityError
        if role == User.CITIZEN:
            CitizenProfile.objects.get_or_create(
                user=user,
                defaults={
                    "gender": random.choice(["Male", "Female"]),
                    "address": f"House {random.randint(1, 100)}, Road {random.randint(1, 20)}, {user.zone.name if user.zone else 'Dhaka'}",
                    "emergency_contact_name": f"Contact of {email.split('@')[0]}",
                    "emergency_contact_phone": f"017{random.randint(10000000, 99999999)}"
                }
            )
        elif role == User.OFFICIAL:
            OfficialProfile.objects.get_or_create(
                user=user,
                defaults={
                    "employee_id": f"EMP-{random.randint(1000, 9999)}",
                    "designation": random.choice(["Duty Officer", "Zone Commander", "Control Room In-charge"]),
                    "department": random.choice(["City Corporation", "Police", "Fire Service"]),
                    "office_phone": f"018{random.randint(10000000, 99999999)}"
                }
            )
        elif role == User.RESPONDER:
            ResponderProfile.objects.get_or_create(
                user=user,
                defaults={
                    "badge_number": f"BDG-{random.randint(1000, 9999)}",
                    "organization": random.choice(["Fire Service", "Red Crescent", "Police"]),
                    "specialization": random.choice(["Paramedic", "Firefighter", "Rescue Ops", "Traffic Control"]),
                    "vehicle_number": f"DHA-{random.randint(11, 99)}-{random.randint(1000, 9999)}",
                    "availability_status": ResponderProfile.AVAILABLE
                }
            )
            
        users[role].append(user)
    print("✅ 10 Users and their specific Profiles Created/Checked.")

    # 4. Create 30 Alerts
    alert_titles = [
        "Massive fire in commercial building", "Severe accident on main road",
        "Waterlogging after heavy rain", "Suspicious activity near bank",
        "Medical support needed immediately", "Transformer blasted", 
        "Road blocked by fallen tree", "Street lights not working"
    ]
    status_choices = [Alert.PENDING, Alert.ACTIVE, Alert.ACKNOWLEDGED, Alert.RESPONDING, Alert.RESOLVED, Alert.FALSE_ALARM]
    
    # Delete old alerts to keep exactly 30 if you run this multiple times
    Alert.objects.all().delete() 

    for i in range(30):
        category = random.choice(categories)
        zone = random.choice(zones)
        reporter = random.choice(users[User.CITIZEN])
        status = random.choice(status_choices)
        
        assigned = None
        if status in [Alert.ACKNOWLEDGED, Alert.RESPONDING, Alert.RESOLVED]:
            assigned = random.choice(users[User.RESPONDER])

        alert = Alert.objects.create(
            title=f"{random.choice(alert_titles)} - {i+1}",
            description="This is a system generated dummy description for testing purposes.",
            category=category,
            zone=zone,
            reported_by=reporter,
            assigned_to=assigned,
            severity=random.randint(category.severity_default - 1, 5) if category.severity_default > 1 else 1,
            status=status,
            latitude=round(random.uniform(23.7000, 23.9000), 6), # Dhaka Latitudes
            longitude=round(random.uniform(90.3500, 90.4500), 6), # Dhaka Longitudes
            is_verified=random.choice([True, False])
        )
    print("✅ 30 Alerts Created.")

    # 5. Create 15 Alert Updates for Random Alerts
    AlertUpdate.objects.all().delete()
    all_alerts = list(Alert.objects.all())
    
    for i in range(15):
        target_alert = random.choice(all_alerts)
        posted_by = random.choice(users[User.OFFICIAL] + users[User.RESPONDER])
        
        AlertUpdate.objects.create(
            alert=target_alert,
            posted_by=posted_by,
            message=f"Update {i+1}: Situation is being monitored and teams are on site."
        )
    print("✅ 15 Alert Updates Created.")
    print("🎉 Database successfully populated!")

if __name__ == '__main__':
    populate()