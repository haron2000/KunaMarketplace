# Kuna Marketplace 🛍️

**Kuna** is a web-based marketplace that connects personal users with nearby businesses offering services like barbering, carpentry, welding, and more. The app allows discovery of businesses via a swipe or grid layout, viewing business profiles, and real-time chatting.

---

## 🚀 Features

- 🔐 Custom signup for Personal & Business accounts
- 🏪 Business users can upload profile images, descriptions, and services
- 📍 Location-based business discovery
- 📸 Business profile viewing
- 💬 Real-time chat system (coming soon!)
- 🧭 Clean modular structure using Django apps

---

## 🛠 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript (optional swiping logic)
- **Database**: SQLite (for dev), PostgreSQL (for deployment)
- **Hosting**: Render (planned)

---

## 🧪 How to Run the App Locally

```bash
git clone https://github.com/haron2000/KunaMarketplace.git
cd KunaMarketplace

# Optional: Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations and start the server
python manage.py migrate
python manage.py runserver
