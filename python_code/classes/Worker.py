class Worker():

    def __init__():
        self.wage = 0.0
        self.firm = None

    def switch_firm(self, new_firm):
        if new_firm != self.firm:
            # assuming *_worker methods update worker's wage and firm
            self.firm.remove_worker(self)
            new_firm.add_worker(self)

    def find_best_firm(self, firms):
        best_wage = self.wage
        best_firm = self.firm
        for firm in firms:
            if (firm != self.firm): # don't calculate new wage for a firm the worker is already in
                temp_wage = firm.calculate_wage(self)
                if temp_wage > best_wage:
                    best_wage = temp_wage
                    best_firm = firm
        return best_wage, best_firm

    def switch_to_best_firm(self, firms):
        best_wage, best_firm = self.find_best_firm(firms)
        self.switch_firm(best_firm)
