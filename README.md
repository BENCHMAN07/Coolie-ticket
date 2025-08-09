
# 🎬 Coolie-ticket

**Coolie-ticket** is a Python automation tool that:
1. Scrapes [BookMyShow](https://www.bookmyshow.com/) for **Chennai**.
2. Checks if a given movie is listed in **Now Showing** or **Upcoming**.
3. Sends a **WhatsApp alert** via [Twilio](https://www.twilio.com/) when the movie appears.

Perfect for tracking highly anticipated releases without refreshing the website every day.

---

## ✨ Features
- ✅ Scrapes BookMyShow movie listings for Chennai.
- ✅ Works for both **Now Showing** and **Upcoming** categories.
- ✅ Sends WhatsApp notification via Twilio.
- ✅ Fully automated with Selenium + BeautifulSoup.

---

## 📦 Requirements

Make sure you have:
- **Python 3.8+**
- **Google Chrome** installed
- Matching **ChromeDriver** for your Chrome version
- A **Twilio Account SID** and **Auth Token** (for WhatsApp API)
- The following Python packages:
  ```bash
  pip install selenium beautifulsoup4 requests twilio
````

---

## ⚙️ Setup

### 1️⃣ Download ChromeDriver

1. Check your Chrome version:

   * Open Chrome → `Menu (⋮)` → **Help** → **About Google Chrome**
2. Download the matching ChromeDriver:

   * [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
3. Extract and place it in:

   ```
   D:\Aditya Personal\Projects\Movie_script\chromedriver-win64\
   ```

---

### 2️⃣ Get Twilio WhatsApp API Credentials

1. Create a free [Twilio account](https://www.twilio.com/try-twilio).
2. Go to the **Messaging / WhatsApp** section and enable the sandbox.
3. Note down:

   * `ACCOUNT_SID`
   * `AUTH_TOKEN`
4. Join the sandbox by sending the code they provide to the WhatsApp number.

---

### 3️⃣ Add Your Twilio Details

In `app.py`, update these lines with your details:

```python
ACCOUNT_SID = "your_account_sid"
AUTH_TOKEN = "your_auth_token"
TWILIO_WHATSAPP = "whatsapp:+14155238886"  # Twilio sandbox number
MY_WHATSAPP = "whatsapp:+91xxxxxxxxxx"     # Your WhatsApp number
```

---

## 🚀 Usage

Run the script:

```bash
python app.py
```

Sample output:

```
🔍 Tracking movie: Coolie
🎯 Status: Upcoming
📩 WhatsApp alert sent!
```

---

## 📂 Project Structure

```
Movie_script/
│
├── app.py                 # Main script
├── README.md              # This file
└── chromedriver-win64/    # ChromeDriver folder
```

---

## 🔧 Troubleshooting

### ChromeDriver Version Error

If you see:

```
session not created: This version of ChromeDriver only supports Chrome version X
```

**Fix**: Download ChromeDriver matching your Chrome version.

### WhatsApp Message Not Sending

* Make sure you've joined Twilio's sandbox via WhatsApp.
* Check if `ACCOUNT_SID` and `AUTH_TOKEN` are correct.

---

## 📜 License

This project is for educational and personal use.
All BookMyShow content belongs to BookMyShow.

---

## ❤️ Credits

Developed by Benchman for the love of cinema 🎥🍿 with a touch of automation magic ⚡

```

