from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime
from database import Base

class GenerationHistory(Base):
    __tablename__ = "generation_history"

    id = Column(Integer, primary_key=True, index=True)
    user_prompt = Column(Text, nullable=False)
    optimized_prompt = Column(Text, nullable=False)
    video_file = Column(String(255), nullable=False)
    website_code = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)