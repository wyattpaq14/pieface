from sqlalchemy import create_engine, exists
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, LargeBinary, DateTime
from sqlalchemy import create_engine


Base = declarative_base()


class MediaSets(Base):
    __tablename__ = 'MediaSets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Type = Column(Integer, nullable=False)
    ResW = Column(Integer, nullable=False)
    ResH = Column(Integer, nullable=False)
    Content = Column(LargeBinary, nullable=False)
    DateCreated = Column(DateTime, nullable=False)
    PauseTime = Column(Integer, nullable=False)
    IsActive = Column(Integer, nullable=False)
    IsDefault = Column(Integer, nullable=False)
    StorageLocation = Column(String, nullable=False)

class db_functions():
    

    print("New database instance created!")
    engine = create_engine('mysql+pymysql://sqlusr:Raspberry@LARRY/PieFace')
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
        
    
    def insert_media_set(self, session, name, mtype, ResW, ResH, content, pause, active, default, storage):
        med_set = MediaSets()

        # this function is good

        # check to see if media set allready exists
        if not session.query(exists().where(MediaSets.Name == name)).scalar():
            med_set.ID = 0
            med_set.Name = name
            med_set.Type = mtype
            med_set.ResW = ResW
            med_set.ResH = ResH
            med_set.Content = content
            med_set.DateCreated = datetime.now()
            med_set.PauseTime = pause
            med_set.IsActive = active
            med_set.IsDefault = default
            med_set.StorageLocation = storage

                    
            session.add(med_set)
            session.commit()
        else:
            print("That media set allready exists!") 

    def get_all_media_sets(self):
        
        Sets = self.session.query(MediaSets)
        return Sets

    def update_media_set_by_id(self, mid, name, mtype, ResW, ResH, content, pause, active, default, storage):
        if self.session.query(exists().where(MediaSets.ID == mid)).scalar():
            med_set = self.session.query(MediaSets).filter_by(ID=mid).first()
            med_set.Name = name
            med_set.Type = mtype
            med_set.ResW = ResW
            med_set.ResH = ResH
            med_set.Content = content
            med_set.DateCreated = datetime.now()
            med_set.PauseTime = pause
            med_set.IsActive = active
            med_set.IsDefault = default
            med_set.StorageLocation = storage

            self.session.commit()
            return True


    def delete_media_set_by_id(self, mid):
        if self.session.query(exists().where(MediaSets.ID == mid)).scalar():
            self.session.query(MediaSets).filter_by(ID=mid).delete()
            self.session.commit()
        
    def get_media_set_by_id(self, mid):
        if self.session.query(exists().where(MediaSets.ID == mid)).scalar():
            med_set = self.session.query(MediaSets).filter_by(ID=mid).first()
            return med_set

    def enabled_categories(self):
        Sets = self.session.query(MediaSets)
        #print(Sets)
        return Sets
 