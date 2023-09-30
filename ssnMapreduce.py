from mrjob.job import MRJob

class CountValues(MRJob):

    def mapper(self, _, line):
        values = line.split()
        key = values[0]
        count = len(values) - 1
        for i in range(1, len(values)):
            yield key, count

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    CountValues.run()