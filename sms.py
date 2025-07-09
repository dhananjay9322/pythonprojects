{
 "cells": [
  {
   "cell_type": "raw",
   "id": "403e8fa2-20fb-4460-898d-28341ab19497",
   "metadata": {},
   "source": [
    "Function to send SMS using python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2221bee6-da54-49e3-80b8-0eab59429aaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from twilio.rest import Client\n",
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "# Load environment variables\n",
    "load_dotenv()\n",
    "\n",
    "def send_sms(to_number, message):\n",
    "    try:\n",
    "        # Load credentials\n",
    "        account_sid = os.getenv(\"TWILIO_ACCOUNT_SID\")\n",
    "        auth_token = os.getenv(\"TWILIO_AUTH_TOKEN\")\n",
    "        from_number = os.getenv(\"TWILIO_PHONE_NUMBER\")\n",
    "\n",
    "        client = Client(account_sid, auth_token)\n",
    "\n",
    "        # Send SMS\n",
    "        message = client.messages.create(\n",
    "            body=message,\n",
    "            from_=from_number,\n",
    "            to=to_number\n",
    "        )\n",
    "\n",
    "        print(f\"✅ SMS sent! SID: {message.sid}\")\n",
    "    except Exception as e:\n",
    "        print(f\"❌ Failed to send SMS: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "884ca591-3505-4758-9c15-ecb56d5858d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ SMS sent! SID: SM8a387ce1ab951a68ecbbd1e49a08f29f\n"
     ]
    }
   ],
   "source": [
    "send_sms(\"+919472444514\", \"Hello! This is a test SMS from Python using Twilio.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "6c285d6a-f6ef-43ac-9724-02676096e2f8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
