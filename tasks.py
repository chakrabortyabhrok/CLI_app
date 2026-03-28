class Tasks:

    def __init__(self, id, name, status):
        self.id=id
        self.name=name
        self.status=status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status
        }
    
    def display_row(self):
        return(f"{self.id:<3} | {self.name:<24} | {self.status}")
    
    
    
    #def display_filtered_row(self, filtered):
    #    print("\nID  |           TASKS          | STATUS")
    #    print("-"*40)
    #    print(f"{self.id:<3} | {self.name:<24} | {self.status}")
    #    print("-"*40)
        #if self.status == filtered:
            