from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    tech_involved = db.Column(db.String(200), nullable=False)
    github_link = db.Column(db.String(200), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    proficiency = db.Column(db.String(100), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)

class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200), nullable=False)
    certificate_url = db.Column(db.String(200), nullable=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    skill_involved = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    field_of_study = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    achievements = db.Column(db.String(1000), nullable=True)


class LicenseCertification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    authority = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(100), nullable=True)
    issue_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=True)
    certificate_url = db.Column(db.String(200), nullable=True)
    ranking = db.Column(db.Integer, nullable=False)

class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    tagline = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.String(1000), nullable=False)
    profile_pic = db.Column(db.String(200), nullable=True)


class UserMsg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    massage = db.Column(db.String(10000), nullable=False)
    
def create_all():
    db.create_all()

def sampledata():
    project1 = Project(title='Project1', description='Description for Project1', image_url='project1.jpg',
                       tech_involved='Python, Flask, SQLAlchemy', github_link='https://github.com/project1',ranking=1)
    db.session.add(project1)
    project2 = Project(title='Project2', description='Description for Project2', image_url='project2.jpg',
                       tech_involved='JavaScript, React, Node.js', github_link='https://github.com/project2',ranking=1)
    db.session.add(project2)
    # For Skills model
    skill1 = Skill(title='Python', description='Proficient in Python programming',proficiency="Experience",ranking=1)
    skill2 = Skill(title='JavaScript', description='Experience in JavaScript programming',proficiency="Proficient",ranking=1)
    db.session.add(skill1)
    db.session.add(skill2)
    # For Awards and Achievment model
    award1 = Award(image_url='award1.jpg', certificate_url='https://certificate1.com', title='Award1',
                   description='Description for Award1',ranking=1)
    award2 = Award(image_url='award2.jpg', certificate_url='https://certificate2.com', title='Award2',
                   description='Description for Award2',ranking=1)
    db.session.add(award1)
    db.session.add(award2)
    # For Experience model
    exp1 = Experience(title='Job1', description='Description for Job1', start_date= date.today(), end_date=date.today(),
                      skill_involved='Python, Flask',company="yahoo",location="delhi")
    exp2 = Experience(title='Job2', description='Description for Job2', start_date=date.today(), end_date=date.today(),
                      skill_involved='JavaScript, React',company="yahoo",location="delhi")
    db.session.add(exp1)
    db.session.add(exp2)
    # For Education model
    edu1 = Education(degree='Bachelor of Science', field_of_study='Computer Science', school='University1',
                     location='City1', start_date=date.today(), end_date=date.today(), achievements='Achievments')
    edu2 = Education(degree='Master of Science', field_of_study='Computer Science', school='University2',
                     location='City2', start_date=date.today(), end_date=date.today(), achievements='Achievments')
    db.session.add(edu1)
    db.session.add(edu2)
    # For License and Certification model
    lic1 = LicenseCertification(title='License1', authority='Authority1', license_number='12345',
                                issue_date=date.today(), expiration_date=date.today(),
                                certificate_url='https://certificate1.com',ranking=1)
    lic2 = LicenseCertification(title='License2', authority='Authority2', license_number='67890',
                                issue_date=date.today(), expiration_date=date.today(),
                                certificate_url='https://certificate2.com',ranking=1)
    db.session.add(lic1)
    db.session.add(lic2)
    # For Bio model
    bio = Bio(name='John Doe', job_title='Python Developer', tagline='Creating solutions, one line at a time',
              summary='I am a Python developer with experience in building web applications using the Flask framework and SQLAlchemy ORM. I am also proficient in JavaScript and have experience in building web applications using the React library.',
              profile_pic='john_doe.jpg')
    db.session.add(bio)
    db.session.commit()
