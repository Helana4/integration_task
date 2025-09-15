# Paymob Integration with Flask

A minimal Flask example that integrates Paymob Accept payment flow.

This repo shows order creation, payment key generation, and redirect to Paymob unified checkout. It is for development and testing.

## What this repo does

* create an order via Paymob
* create an intention or payment key
* redirect users to Paymob checkout page
* handle callback redirect from Paymob

## Project layout

```
integration_task/
├── app.py                 # Flask app and routes
├── paymob_checkout.py     # Paymob API helper functions
├── templates/
│   └── pay.html           # simple payment page
├── .env.example           # environment variables template
└── README.md              # this file
```

## Prerequisites

* Python 3.8 or newer
* pip
* Git
* Paymob account with Secret Key and Public Key

## Setup

1. clone

   ```bash
   git clone https://github.com/Helana4/integration_task.git
   cd integration_task
   ```

2. create virtual env and install

   ```bash
   python -m venv venv
   source venv/bin/activate    # mac/linux
   venv\Scripts\activate     # windows
   pip install -r requirements.txt
   ```

3. create .env from template

   * copy `.env.example` to `.env`
   * edit values

4. run

   ```bash
   python app.py
   ```

   open `http://127.0.0.1:5000`

## Environment variables (.env.example)

```
SECRET_KEY=your_paymob_secret_key
PUBLIC_KEY=your_paymob_public_key
INTEGRATION_ID=your_integration_id
```

## Code notes

* keep secret keys out of source control
* use `python-dotenv` to load env values in `paymob_checkout.py`

Example loader (Python):

```python
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
INTEGRATION_ID = os.getenv('INTEGRATION_ID')
```

## Endpoints

* `/` home page to start payment
* `/pay` start a payment
* `/create-intention` create an intention (example)
* `/payment_callback` handle redirect after payment

## Webhooks

* add `notification_url` when creating the intention
* configure dashboard callback for reliability

## Security

* do not expose `SECRET_KEY`
* verify webhook payloads in production

## Contributing

Open an issue or a pull request.

---

If you want I can generate a ready `.env.example` file and a small patch for `paymob_checkout.py` to read env values. Copy this README into your repo or let me guide you through the git steps.
