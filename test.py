import pandas as pd
import pickle as pic

class UserItemData:
    fileLines = []
    def __init__(self, path, start_date = None, end_date = None, min_ratings = 0):
        self.path = path
        self.start_date = start_date
        self.end_date = end_date
        self.min_ratings = min_ratings
        with open(path, 'r') as f:
            self.fileLines = f.readlines()

    def nratings(self):
        print(self.fileLines)
        return None

uim = UserItemData('data/user_ratedmovies.dat', start_date = '12.1.2007', end_date='16.2.2008', min_ratings=100)
print(uim.nratings())