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
    
            