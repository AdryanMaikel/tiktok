from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Video(Base):
    __tablename__ = "video"
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, nullable=False, unique=True)
    descricao = Column(String, nullable=True)
    estado = Column(String, nullable=False)


engine_videos = create_engine("sqlite:///db/videos.db")
Base.metadata.create_all(engine_videos)
Session = sessionmaker(bind=engine_videos)


def create_video(link, descricao, estado):
    with Session() as session:
        video = Video(link=link, descricao=descricao, estado=estado)
        session.add(video)
        session.commit()
        session.refresh(video)
        return video


def read_videos():
    session = Session()
    videos = session.query(Video).all()
    session.close()
    return videos


def read_video_by_id(video_id):
    session = Session()
    video = session.query(Video).filter(Video.id == video_id).first()
    session.close()
    return video


def update_video(video_id, link=None, descricao=None, estado=None):
    session = Session()
    video = session.query(Video).filter(Video.id == video_id).first()
    if not video:
        session.close()
        return None
    if link:
        video.link = link
    if descricao:
        video.descricao = descricao
    if estado:
        video.estado = estado
    session.commit()
    session.close()
    return video


def delete_video(video_id):
    session = Session()
    video = session.query(Video).filter(Video.id == video_id).first()
    if not video:
        session.close()
        return None
    session.delete(video)
    session.commit()
    session.close()
    return video


engine_videos = create_engine("sqlite:///db/videos.db")
Base.metadata.create_all(engine_videos)
Session = sessionmaker(bind=engine_videos)


if __name__ == "__main__":
    session = Session()
    for video in session.query(Video).all():
        print(video.id, video.link, video.descricao, video.estado)
