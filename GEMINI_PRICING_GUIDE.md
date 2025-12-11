# Gemini API Pricing Guide

## ⚠️ Important: Model Availability and Pricing

Some Gemini models require a **paid Google Cloud plan**, while others are available on the **free tier**.

## 💰 Pricing Tiers

### Free Tier Models (Recommended for Most Users)

These models work with the free tier and have generous limits:

1. **`gemini-flash-latest`** ✅ FREE
   - Fast responses
   - Good for most tasks
   - Recommended for general use
   - **Current default in this project**

2. **`gemini-pro-latest`** ✅ FREE
   - More capable than Flash
   - Better for complex queries
   - Slightly slower but higher quality

### Paid Tier Models

These models require a **paid Google Cloud billing account**:

- `gemini-2.5-pro` - Requires paid plan
- `gemini-2.5-flash` - Requires paid plan
- `gemini-2.0-flash-exp` - Requires paid plan
- `gemini-3-pro-preview` - Requires paid plan

## 🚨 Common Error Messages

### Error: "404 models/gemini-1.5-flash is not found"

**Solution:** The model name is incorrect. Use:
- `gemini-flash-latest` (not `gemini-1.5-flash`)
- `gemini-pro-latest` (not `gemini-1.5-pro`)

### Error: "429 Quota exceeded" with gemini-2.5-pro

**Solution:** This model requires a paid plan. Switch to:
- `gemini-flash-latest` (free tier)
- `gemini-pro-latest` (free tier)

## 📝 How to Configure

### Option 1: Use Free Tier (Recommended)

Edit `config.py`:

```python
GEMINI_MODEL = 'gemini-flash-latest'  # Free tier
```

Or in `.env` file:

```env
GEMINI_MODEL=gemini-flash-latest
```

### Option 2: Use Paid Tier Models

If you have a paid Google Cloud account:

1. **Enable billing** in Google Cloud Console
2. **Set up billing account** with payment method
3. Update `config.py`:

```python
GEMINI_MODEL = 'gemini-2.5-pro'  # Requires paid plan
```

## 💳 Setting Up Paid Billing

If you want to use paid tier models:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **Billing** → **Link a billing account**
3. Add a payment method (credit card)
4. Enable billing for your project
5. Update the model in `config.py`

## 📊 Free Tier Limits

Even with free tier models, you have rate limits:

- **Requests per minute**: Limited
- **Requests per day**: Limited  
- **Tokens per day**: Limited

If you hit limits:
- Wait a few minutes
- Try again
- Consider upgrading for higher limits

## ✅ Recommended Setup

**For most users (including clients):**

```python
GEMINI_MODEL = 'gemini-flash-latest'
```

This provides:
- ✅ Free tier access
- ✅ Fast responses
- ✅ Good quality
- ✅ No additional costs
- ✅ No billing setup required

## 🔍 Check Available Models

Run this command to see all available models:

```cmd
py check_models.py
```

## 📞 For Clients

**Message to share with clients:**

> "This application uses Google's Gemini AI API. The default configuration uses the free tier (`gemini-flash-latest`), which provides excellent performance at no cost. If you need access to premium models like `gemini-2.5-pro`, you'll need to set up a paid Google Cloud billing account. The free tier models are recommended for most use cases."

---

**Current Configuration:** The project is set to use `gemini-flash-latest` (free tier) by default, which should work without any billing setup.

