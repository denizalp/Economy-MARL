class Firm():

    def __init__():
        self.revenue = 0.0
        self.workers = set()

    def calculate_wage(self, worker):
        '''
        currently assuming equal disribution of revenue to workers
        '''
        new_num_of_workers = len(self.workers) + 1
        temp_wage = self.revenue / (1.0 * new_num_of_workers)
        return temp_wage

    def update_worker_wages(self):
        for worker in self.workers:
            temp_wage = self.calculate_wage(worker) # for robustness, don't assume anything about how wage is calculated
            worker.wage = temp_wage

    def add_worker(self, worker):
        self.workers.add(worker)
        worker.firm = self
        self.update_worker_wages()

    def remove_worker(self, worker):
        if worker in self.workers:
            self.workers.remove(worker)
            worker.firm = None
            self.update_worker_wages()
        
