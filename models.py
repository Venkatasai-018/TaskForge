from db.database import Base
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey,String,Integer
from sqlalchemy.orm import mapped_column,Mapped,validates
from sqlalchemy import DateTime,func
from datetime import datetime



class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False,autoincrement=True)
    email: Mapped[str] = mapped_column(String(30),nullable=False)
    username: Mapped[Optional[str]]=mapped_column(String(30),nullable=False)
    password: Mapped[str] = mapped_column(String(30),nullable=False)

class Projects(Base):
    __tablename__="projects"
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False,autoincrement=True)
    name: Mapped[Optional[str]]=mapped_column(String(30),nullable=False)
    description:Mapped[str]=mapped_column(String(100))
    ownerid:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now())

class Projectmembers(Base):
    __tablename__="projectmembers"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True,nullable=False)
    project_id:Mapped[int]=mapped_column(ForeignKey("projects.id"),nullable=False)
    user_id:Mapped[int]=mapped_column(ForeignKey('users.id'),nullable=False)
    role: Mapped[str] = mapped_column(String(10), default="member", nullable=False)

    ALLOWED_ROLES = ["owner", "member"]

    @validates("role")
    def validate_role(self, key, value):
        if value not in self.ALLOWED_ROLES:
            raise ValueError(f"Role must be one of {self.ALLOWED_ROLES}")
        return value
    
class Tasks(Base):
    __tablename__="tasks"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True,nullable=False)
    project_id:Mapped[int]=mapped_column(ForeignKey("projects.id"),nullable=False)
    title:Mapped[str]=mapped_column(String(30),nullable=False)
    description:Mapped[Optional[str]]=mapped_column(String(30))
    status:Mapped[str]=mapped_column(String(10),nullable=False,default="TODO")
    priority:Mapped[str]=mapped_column(String(10),nullable=False)
    deadline:Mapped[Optional[datetime]]=mapped_column(DateTime(timezone=True))
    assigned_to:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now())
    

    Allowed_Status=["TODO","Inprogress","Completed"]
    @validates(status)
    def validates_status(self,key,value):
        if value not in self.Allowed_Status:
            raise ValueError(f"Status must be one of {self.Allowed_Status}")
        return value
    Allowed_priority=["p1","p2","p3","p4"]
    @validates(priority)
    def validate_priority(self,key,value):
        if value not in self.Allowed_priority:
            raise ValueError(f"Priority must be one of {self.Allowed_priority}")
        return value


