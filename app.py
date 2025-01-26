import streamlit as st
import pandas as pd
from datetime import datetime
from github_stats import fetch_contribution_data, process_contribution_data

# Title and input
st.title("GitHub Contribution Tracker")
with st.container(border=True):
    username = st.text_input("Enter GitHub Username:")
    token = st.text_input("Enter GitHub Personal Access Token:", type="password", help="Help: [Create Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)")
    button_pressed = st.button("Track", type="primary")

color = "#26a641"

if username and token and button_pressed:
    # Fetch data
    raw_data = fetch_contribution_data(username, token)
    if "errors" in raw_data:
        st.error("Error fetching data. Check your username/token.")
    else:
        stats = process_contribution_data(raw_data)

        # Display summary metrics
        st.header("Summary Stats")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            col1.metric(
                "Total Contributions", 
                stats['total_contributions'],
                delta=f"{stats['highest_contribution']} Highest"
                )
            col2.metric(
                "Longest Streak", 
                stats['longest_streak'],
                delta=f"{stats['current_streak']} Current",
                delta_color= "off" if stats['current_streak'] == 0 else "normal"
                )

        # Prepare data for visualizations
        days = stats["days"]
        dates = [datetime.strptime(day["date"], "%Y-%m-%d") for day in days]
        contributions = [day["contributionCount"] for day in days]

        # Contributions Over Time
        st.header("Contributions Over Time")
        with st.container(border=True):
            chart_data = pd.DataFrame({"Date": dates, "Contributions": contributions})
            st.line_chart(chart_data.set_index("Date"), x_label="Date", y_label="Contributions", color=color)

        # Yearly Growth
        chart_data['Year'] = chart_data['Date'].dt.year
        yearly_contributions = chart_data.groupby('Year')['Contributions'].sum()

        st.header("Yearly Growth")
        st.bar_chart(yearly_contributions, color=color)

        # Weekly Heatmap
        # st.header("Weekly Contribution Heatmap")
        chart_data["Week"] = chart_data['Date'].dt.isocalendar().week
        chart_data["Day"] = chart_data['Date'].dt.dayofweek

        heatmap_data = chart_data.pivot_table(index="Day", columns="Week", values="Contributions", aggfunc="sum", fill_value=0)
        # st.write("**Heatmap (Day of Week vs. Week of Year)**")
        # st.dataframe(heatmap_data, use_container_width=True)

        # Most Productive Days
        st.header("Most Productive Day")
        most_productive_day = chart_data.loc[chart_data['Contributions'].idxmax()]
        st.metric(
            "Date", 
            most_productive_day['Date'].strftime("%d-%m-%Y"), 
            delta=f"{most_productive_day['Contributions']} Contributions", 
            label_visibility="collapsed", 
            border=True
            )

        # Weekday vs. Weekend Contributions
        st.header("Weekday vs. Weekend Contributions")
        
        chart_data['IsWeekend'] = chart_data['Date'].dt.dayofweek >= 5
        weekend_data = chart_data.groupby('IsWeekend')['Contributions'].sum()
        weekend_data.index = ["Weekdays", "Weekends"]
        st.bar_chart(weekend_data, color=color, horizontal=True)

        # Contribution Times Analysis (if available)
        st.header("Contributions by Day of Week")
        day_of_week_data = chart_data.groupby("Day")['Contributions'].sum()
        day_of_week_data.index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        st.bar_chart(day_of_week_data, color=color, horizontal=True)

        # Custom Achievements
        st.header("Achievements")
        if stats['current_streak'] <= 2:
            st.markdown("🌱 **Streak Beginner**") 
        elif stats['current_streak'] > 2 and stats['current_streak'] <= 7:
            st.markdown("🌿 **Streak Novice**")
        elif stats['current_streak'] > 7 and stats['current_streak'] <= 14:
            st.markdown("🌳 **Streak Apprentice**") 
        elif stats['current_streak'] > 14 and stats['current_streak'] <= 30:
            st.markdown("⚔️ **Streak Journeyman**")
        elif stats['current_streak'] > 30 and stats['current_streak'] <= 60:
            st.markdown("🛡️ **Streak Expert**")
        elif stats['current_streak'] > 60 and stats['current_streak'] <= 90:
            st.markdown("🧙‍♂️ **Streak Master**")
        elif stats['current_streak'] > 90:
            st.markdown("🐉 **Streak Legend**") 

        
        if stats['total_contributions'] < 50:
            st.markdown("🌱 **Contributor**")
        elif stats['total_contributions'] >= 50 and stats['total_contributions'] < 100:
            st.markdown("🌿 **Regular Contributor**")
        elif stats['total_contributions'] >= 100 and stats['total_contributions'] < 500:
            st.markdown("🌳 **Active Contributor**")
        elif stats['total_contributions'] >= 500 and stats['total_contributions'] < 1000:
            st.markdown("⚔️ **Dedicated Contributor**")
        elif stats['total_contributions'] >= 1000 and stats['total_contributions'] < 5000:
            st.markdown("🛡️ **Seasoned Contributor**")
        elif stats['total_contributions'] >= 5000:
            st.markdown("🧙‍♂️ **GitHub Legend**")

        st.write("Keep growing your GitHub stats and unlock more achievements!")
