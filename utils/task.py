from datetime import datetime

class Task:
    """Represent a single task"""
    
    def __init__(self, id: int, title: str, status: str) -> None:
      self.id = id
      self.title = title
      self.status = status
      self.created_at = datetime.now().strftime("%Y-%m-%d%H:%M")  