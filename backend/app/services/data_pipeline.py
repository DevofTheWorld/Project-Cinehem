from pathlib import Path
import pandas as pd

class pipeline:

    def main(self):
        current_dir = Path(__file__).resolve().parent
        root_dir = current_dir.parent.parent.parent

        diary_filepath = root_dir / "letterboxd-whoisanthony-2026-09-09-11-48-utc" / "diary.csv"

        df = pd.read_csv(diary_filepath, usecols=['Date', 'Name', 'Rating', 'Watched Date'])
        df['Watched Date'] = pd.to_datetime(df['Watched Date'])

        five_star = df[df['Rating'] >= 4.5]['Name'].tolist()
        low_star = df[df['Rating'] <= 2]['Name'].tolist()
        recent_watched = df.sort_values(by=['Watched Date'], ascending=False).head(20)['Name'].tolist()

        return f"5-Star Movies: {five_star}, Low-Star Movies: {low_star}, Recent Watches: {recent_watched}"