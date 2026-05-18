# 🏡 House Price Prediction Deployment Guide

This guide provides step-by-step instructions to deploy your Streamlit Machine Learning application to Streamlit Community Cloud.

## 📁 Project Folder Structure
Ensure your project directory looks exactly like this before deploying:

```text
project/
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
├── .python-version
└── README.md
```

## 🚀 Step-by-Step Deployment Instructions

### Step 1: Upload to GitHub
1. Create a GitHub account if you don't have one: [github.com](https://github.com/)
2. Create a new repository by clicking the **"+"** icon in the top right corner and selecting **"New repository"**.
3. Name your repository (e.g., `house-price-predictor`).
4. Set it to **Public** or **Private**.
5. Do not initialize with a README, .gitignore, or license just yet.

### Step 2: Push Repository
Upload your project files to the new GitHub repository. You can do this via the command line or directly through the GitHub website:

**Option A (GitHub Website):**
1. In your new repository, click on **"uploading an existing file"**.
2. Drag and drop `app.py`, `house_price_model.pkl`, `requirements.txt`, and `.python-version` into the upload area.
3. Click **"Commit changes"**.

**Option B (Command Line/Git):**
```bash
git init
git add .
git commit -m "Initial commit - House Price App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```

### Step 3: Open Streamlit Cloud
1. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
2. Sign in or sign up using your GitHub account.

### Step 4: Connect GitHub
1. Once logged in, click the **"New app"** button.
2. If prompted, authorize Streamlit to access your GitHub repositories.

### Step 5: Select app.py
1. In the deployment configuration page:
   - **Repository:** Select your repository (e.g., `YOUR_USERNAME/house-price-predictor`).
   - **Branch:** Select `main` (or `master`).
   - **Main file path:** Type `app.py`.
2. (Optional) In the "Advanced settings", you can specify a custom app URL.

### Step 6: Deploy
1. Click the **"Deploy!"** button.
2. Streamlit will now spin up a server, install your dependencies listed in `requirements.txt` using Python 3.11 (from `.python-version`), and launch your app.
3. Wait a minute or two for the "baking" process to complete.

---

## 🛠️ Troubleshooting Tips

- **ModuleNotFoundError**: If you get an error that a package is missing, double-check your `requirements.txt` to ensure the package is listed and spelled correctly.
- **Model Loading Error**: If the app fails to load the model, verify that `house_price_model.pkl` is uploaded to the root of your GitHub repository.
- **Dependency Conflicts**: If Streamlit cloud gets stuck during deployment, there might be a dependency conflict. We've pinned stable versions in `requirements.txt` to avoid this. If it happens, you might try removing the specific version numbers (e.g., just `pandas` instead of `pandas==2.2.3`) to let Streamlit resolve them, though pinned is usually safer.
- **Rebooting App**: If your app hangs or crashes, you can reboot it from the Streamlit Cloud dashboard by clicking the three dots next to your app and selecting **"Reboot app"**.
