from datetime import datetime

class Task:
    """Represent a single task"""
    
    def __init__(self, id: int, title: str, status: str) -> None:
      self.id = id
      self.title = title
      self.status = status
      self.created_at = datetime.now().strftime("%Y-%m-%d%H:%M") 
      

    def to_dict(self) -> dict:
       return {
          "id": self.id,
          "title": self.title,
          "status": self.status,
          "created_at":
          self.created_at
       } 

    
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
       task = cls(data["id"], data["title"], data["status"])
       task.created_at = data["created_at"]
       return task 


    def edit(self,title: str | None = None,status: str | None = None,) -> None:
        if title is not None:
           self.title = title
        if status is not None:
           self.status = status

