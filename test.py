import pandas as pd
import pickle as pic

class UserItemData:
    def __init__(self, path) -> None:
        self.path = path
        #self.from_date = from_date
        #self.to_date = to_date
        #self.min_ratings = min_ratings

    def read(self):
        df = pd.read_csv(self.path)
        return df

uim = UserItemData('data/user_ratedmovies.dat')
print(uim.read())