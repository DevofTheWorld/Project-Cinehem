import pandas as pd

class pipeline:

    def main(self):
        diary_filepath = '/Users/anthonylumantao/PycharmProjects/Project Cinehem/letterboxd-whoisanthony-2026-09-09-11-48-utc/diary.csv'

        df = pd.read_csv(diary_filepath, usecols=['Date', 'Name', 'Rating', 'Watched Date'])
        df['Watched Date'] = pd.to_datetime(df['Watched Date'])

        five_star = df[df['Rating'] >= 4.5]['Name'].copy().reset_index(drop=True)
        recent_watched = df.sort_values(by=['Watched Date'], ascending=False).head(20)
        low_star = df[df['Rating'] <= 2].copy().reset_index(drop=True)

        return five_star
