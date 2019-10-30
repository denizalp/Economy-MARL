class Economy:

    def __init__(self, outputs, jobIndexes):
        self.firms = [Job(output) for output in outputs]
        self.workers = [Worker(jobs) for jobs in [[self.firms[index-1] for index in indexes] for indexes in jobIndexes]]
