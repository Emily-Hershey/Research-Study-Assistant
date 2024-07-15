from app import db

class Database(db.Model):
    __tablename__ = 'scrapy_database'
    id = db.Column(db.Integer, primary_key=True)  # Add a primary key column
    topic = db.Column(db.String(200), unique=False, nullable=False)
    link = db.Column(db.String(200), unique=False, nullable=False)
    text = db.Column(db.String(200), unique=False, nullable=False)
    summary = db.Column(db.String(200), unique=False)
                        
    def to_json(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "link": self.link,
            "text": self.text,
            "summary": self.summary,
        }
    def insert_data(topic, link, text, summary):
        new_entry = Database(topic=topic, link=link, text=text, summary=summary)
        db.session.add(new_entry)
        db.session.commit()
    def reset_database():
        db.drop_all()  # Drop all tables
        db.create_all()  # Create tables as per the models defined
        print("Database has been reset.")


# Example usage
