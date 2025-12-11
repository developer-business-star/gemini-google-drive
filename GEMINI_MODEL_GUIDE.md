# Gemini Model Guide - Free Tier vs Paid

## ⚠️ Important: Free Tier Limitations

**`gemini-2.5-pro` and `gemini-2.0` models are NOT available on the free tier.**

These models require a paid Google Cloud plan. If you try to use them with a free API key, you'll get a quota exceeded error (429).

## ✅ Free Tier Models

These models work with the free tier:

### 1. `gemini-1.5-flash` (Recommended)
- **Fast and efficient**
- **Free tier available**
- Good for most tasks
- Lower latency

### 2. `gemini-1.5-pro`
- **More capable**
- **Free tier available**
- Better for complex queries
- Higher quality responses

## ❌ Paid Tier Models (Not Available on Free)

- `gemini-2.5-pro` - Requires paid plan
- `gemini-2.0-flash-exp` - Requires paid plan
- `gemini-2.0-pro-exp` - Requires paid plan

## How to Fix Quota Error

### Step 1: Update config.py

Change the model to a free tier model:

```python
GEMINI_MODEL = 'gemini-1.5-flash'  # Free tier
# OR
GEMINI_MODEL = 'gemini-1.5-pro'   # Free tier
```

### Step 2: Restart the Application

```cmd
py app.py
```

## Free Tier Limits

Even with free tier models, you have rate limits:

- **Requests per minute**: Limited
- **Requests per day**: Limited
- **Tokens per day**: Limited

If you hit rate limits:
1. Wait a few minutes
2. Try again
3. Consider upgrading to paid plan for higher limits

## Check Your Usage

Monitor your usage at: https://ai.dev/usage?tab=rate-limit

## Recommended Settings

For most users, use:

```python
GEMINI_MODEL = 'gemini-1.5-flash'
```

This gives you:
- ✅ Free tier access
- ✅ Fast responses
- ✅ Good quality
- ✅ No quota errors

---

**Remember**: Always use `gemini-1.5-flash` or `gemini-1.5-pro` for free tier access!

