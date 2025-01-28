![image](https://github.com/user-attachments/assets/b018c10a-db2b-4c56-9832-6cafda16ed1f)

# GitHub Stat Checker

GitHub Contribution Tracker is a **Streamlit** web application that visualizes GitHub user contributions with insightful metrics, charts, and achievements. This app uses the **GitHub GraphQL API** to fetch and display data about a user's contribution history, enabling users to track and analyze their growth.

## Features

- **Summary Stats**:

  - Total contributions across all repositories.
  - Highest contributions in a single day.
  - Current streak of consecutive contribution days.
  - Longest streak of consecutive contribution days.

- **Visualizations**:

  - **Contributions Over Time**: A line chart showing daily contributions.
  - **Yearly Growth**: A bar chart summarizing contributions year by year.
  - **Weekly Contribution Heatmap**: An interactive table visualizing contributions by the day of the week and week of the year.
  - **Day-of-Week Analysis**: Contributions grouped by the day of the week.
  - **Weekday vs. Weekend Contributions**: A bar chart comparing contributions made on weekdays versus weekends.

- **Custom Metrics**:

  - Most productive day: Displays the date with the highest contributions.
  - Contribution streaks: Real-time updates of current and longest streaks.

- **Achievements**:

  - Dynamic achievements unlocked based on contribution activity, such as:
    - **"🔥 Streak Warrior"**: A streak of over 30 days.
    - **"💪 Commit Master"**: Total contributions exceeding 1000.

- **Language Usage (upcoming)**:
  - Extendable with GitHub API to display language usage stats for repositories.

## Installation

### Prerequisites

1. Python 3.7 or higher.
2. GitHub [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classi) with GraphQL API access.
3. Streamlit (`pip install streamlit`).

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/TheCarBun/GitHub-Stat-Checker.git
   cd GitHub-Stat-Checker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`).

---

## Usage

1. Enter your **GitHub Username**.
2. Provide a **GitHub Personal Access Token** (with `read:user` and `repo` scopes for GraphQL API access).
3. View detailed stats, visualizations, and achievements based on your contribution data.

### How to Generate a GitHub Personal Access Token

1. Go to [GitHub Developer Settings](https://github.com/settings/tokens).
2. Click on **Generate new token (classic)** or **Generate token** (for fine-grained).
3. Select the following scopes:
   - `repo`
   - `read:user`
4. Copy the generated token and use it in the app.

## Folder Structure

```
github-contribution-tracker/
├── github_stats.py         # Logic for fetching and processing GitHub contribution data.
├── app.py                  # Streamlit app for displaying the dashboard.
├── requirements.txt        # Python dependencies.
└── README.md               # Project documentation.
```

---

### Future Improvements

- Add more dynamic achievements.
- Include repository-specific stats (e.g., most active repositories).
- Display contributions grouped by month.
- Add user rankings for team or organization collaboration.
- Add language usage data.

## Screenshots

<details>
<summary><b>Click to View Images 📷</b></summary><br>

![image](https://github.com/user-attachments/assets/f8d8ede2-40ea-493a-9c50-ba043492c8be)

![image](https://github.com/user-attachments/assets/c8883411-8afe-403b-bad2-300897bba48d)

![image](https://github.com/user-attachments/assets/a18e3d50-29e9-43a7-91ad-30413c4039e4)

![image](https://github.com/user-attachments/assets/3e87ffb6-30b5-40ee-b1bd-50c1c63ff465)

</details>

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m 'Add your feature'`.
4. Push to your fork: `git push origin feature/your-feature`.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **[Streamlit](https://streamlit.io/)**: For building the interactive web application.
- **[GitHub GraphQL API](https://docs.github.com/en/graphql)**: For data fetching.
