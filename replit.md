# MyTelegramBot2

## Overview
This is a Telegram bot for managing money-making opportunities through various websites. The bot helps users get access codes, view instructional videos, and manage withdrawals for different earning platforms.

## Recent Changes
- **2025-09-11**: Successfully imported GitHub project and configured for Replit environment
- **2025-09-11**: Set up Python dependencies and environment variables
- **2025-09-11**: Created main_replit.py with secure webhook configuration
- **2025-09-11**: Fixed security vulnerabilities related to bot token exposure
- **2025-09-11**: Configured workflow and deployment settings

## Project Architecture
- **Language**: Python 3.11
- **Framework**: Flask (webhook server) + pyTelegramBotAPI
- **Database**: Google Sheets (via gspread library)
- **Authentication**: Google Service Account
- **Hosting**: Replit with webhook integration

### Key Files
- `main_replit.py` - Main bot application optimized for Replit
- `Main.py` - Original bot file (preserved for reference)
- `requirements.txt` - Python dependencies
- `Procfile` - Original deployment configuration

### Environment Variables
- `BOT_TOKEN` - Telegram Bot API token
- `GOOGLE_SERVICE_ACCOUNT_JSON` - Google Sheets API credentials
- `REPLIT_DEV_DOMAIN` - Automatically provided by Replit
- `PORT` - Server port (defaults to 5000)

## Current State
- ✅ Bot is running and accessible via webhook
- ✅ Flask server running on 0.0.0.0:5000 
- ✅ Webhook configured securely at /webhook endpoint
- ✅ Google Sheets integration working
- ✅ All security vulnerabilities addressed
- ✅ Production deployment configured

## Bot Features
- User code distribution system
- Multiple earning platform tutorials (IP Web, UNU, VK Surfing, VK Target, Aviso)
- Withdrawal instruction videos
- Admin code management
- WhatsApp integration for payments

## Deployment
- **Development**: Runs via Replit workflow on dynamic domain
- **Production**: Configured for VM deployment with stable domain
- **Security**: Webhook path does not expose sensitive tokens