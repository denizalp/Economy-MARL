class Job:
    jobNumber = 1

    def __init__(self, output, tasks):
        self.id = Job.jobNumber
        Job.jobNumber += 1
        self.output = output
        self.workers = []
        self.tasks = []

    def getWage(self):
        if(self.workers):
            return self.output / len(self.workers)
        return 0

    def getPotentialWage(self):
        return self.output / (len(self.workers) + 1)

    def addWorker(self, worker):
        self.workers.append(worker)

    def removeWorker(self, worker):
        self.workers.remove(worker)

    def __repr__(self):
        string = f"Job {self.id}:\n Current Wage: {self.getWage()} \n Wage with one more worker: {self.getPotentialWage()} \n Workers:\n {self.workers}\n\n"

    return string
