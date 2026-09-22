# A Universe of Us — Birthday Surprise Site

A personal, animated Streamlit website: a story page, a 30-photo memory
timeline, a couples quiz, a "reasons I love you" generator, and a closing
letter. Built to be shown on a phone.

## 1. Personalize it

Open `app.py` and edit the block at the top marked:

```
# 1. EDIT THIS SECTION — make it yours!
```

You can change:
- Her name, your name, site title, tagline
- Colors (hex codes)
- "Our Story" text
- All 30 memory captions
- The 5 quiz questions, options, and correct answers
- The list of "reasons I love you"
- The final letter text

## 2. Add your photos

Drop 30 photos into the `photos/` folder, named `1.jpg`, `2.jpg`, ... `30.jpg`
(matching the order of your captions in `app.py`). `.jpeg` and `.png` work too.
If a photo is missing, the app just shows a placeholder instead of crashing —
handy for testing before all 30 are ready.

## 3. Set the login username & password

The site now shows a login screen first — she has to enter the right
username and password before the "Universe of Us" page appears.

**For local/private use**, just edit these two lines in `app.py`:

```python
APP_USERNAME = "her_username"
APP_PASSWORD = "your_secret_password"
```

**If you're deploying it (see Hosting below)**, don't leave the real
password sitting in `app.py` — that file ends up on GitHub. Instead:

1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
2. Edit the real username/password inside it:
   ```toml
   [auth]
   username = "her_username"
   password = "your_secret_password"
   ```
3. The app automatically reads from here if it exists, and ignores the
   `APP_USERNAME`/`APP_PASSWORD` values in `app.py` as a result.

`.streamlit/secrets.toml` is already listed in `.gitignore`, so it will
**not** be pushed to GitHub — only `secrets.toml.example` (with placeholder
values) goes up publicly.

## 4. Install & run

```powershell
pip install -r requirements.txt
streamlit run app.py
```

This opens the app in your browser on your laptop. Click through every
section once to check your edits and photos look right.

## 5. Show it on her phone

Easiest option — do it live, no deployment needed:

1. Make sure your phone and laptop are on the **same Wi-Fi network**.
2. When you run `streamlit run app.py`, the terminal prints a
   **"Network URL"** (something like `http://192.168.1.23:8501`).
3. Open that exact URL in her phone's browser.
4. Hand her the phone. 🎉

If you'd rather send her a real link she can open any time (not just while
your laptop is running), the free option is **Streamlit Community Cloud**:
push this folder to a GitHub repo, connect it at share.streamlit.io, and it
gives you a public `https://...streamlit.app` link — just note that anyone
with the link could technically view it, so it's not private.

## 6. Hosting it (public link instead of live demo)

If you deploy via **Streamlit Community Cloud** (share.streamlit.io):

1. Push this folder to a GitHub repo (keep it Private).
   `.gitignore` already keeps your real `secrets.toml` out of the push.
2. In the Streamlit Cloud dashboard, after connecting your repo, go to
   your app's **Settings → Secrets** and paste in:
   ```toml
   [auth]
   username = "her_username"
   password = "your_secret_password"
   ```
3. Deploy. The hosted app reads credentials from Streamlit Cloud's secrets
   manager the same way it reads your local `secrets.toml` — no code change
   needed.

This way the login password is protected in two places: never committed to
GitHub, and required before anyone with the link can see the site.

## 7. Tips

- Test the full flow once yourself before the big reveal — check captions,
  quiz answers, and that all photos load.
- Keep photos reasonably sized (under ~2MB each) so it loads fast on mobile
  data if you're not on Wi-Fi.
- The nav bar at the top (🏠📖📸🧩💌💝) lets you jump to any section, in case
  you want to skip around while showing her.
