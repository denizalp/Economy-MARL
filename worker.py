class Worker:
    workerNumber = 1

    #Initialize the class with a list of the jobs each worker can do
    def __init__(self, jobs):
        self.job = None
        self.jobs = jobs
        self.id = Worker.workerNumber
        self.tasks = []
        Worker.workerNumber += 1

    def __repr__(self):
        string = f"Worker {self.id}, Jobs he can do: {[job.id for job in self.jobs]}\n"
        return string

    #Accessor function for Wage
    def getWage(self):
        return self.job.getWage()

    #Accessor function for job
    def getJob(self):
        return self.job

    #Given a list of job that the worker can accomplish return the job that pays him the most
    def getMaxJob(self):
        return max([job for job in self.jobs if job != self.job], key = lambda job: job.getPotentialWage())

    #Mutator function to change the job of the worker
    def setJob(self, job):
        self.job = job
