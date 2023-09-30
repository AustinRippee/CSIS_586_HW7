from mrjob.job import MRJob

class RatingCount(MRJob):

    def mapper(self, _, line):
        userID, movieID, rating, timestamp = line.split(',')
        try:
            rating = int(rating)
            yield rating, 1
        except ValueError:
            pass

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    RatingCount.run()