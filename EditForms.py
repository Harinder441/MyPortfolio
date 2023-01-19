from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, validators, SubmitField,IntegerField,SelectField


class ProjectForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    image_url = StringField('Image URL', [validators.URL()])
    tech_involved = StringField('Technology Involved', [validators.DataRequired()])
    github_link = StringField('Github Link', [validators.URL()])
    ranking = IntegerField('Ranking',[validators.DataRequired()])
    submit = SubmitField('Edit')


class SkillsForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    proficiency_list = ["Basic", "Proficient", "Experienced"]
    proficiency= SelectField("Proficiency",choices= proficiency_list,default= "Select Proficiency")
    ranking = IntegerField('Ranking',[validators.DataRequired()])

    submit = SubmitField('Edit')


class AwardsForm(FlaskForm):
    image_url = StringField('Image URL', [validators.URL()])
    certificate_url = StringField('Certificate URL', [validators.URL()])
    title = StringField('Title', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    ranking = IntegerField('Ranking',[validators.DataRequired()])
    submit = SubmitField('Edit')


class ExperienceForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    start_date = DateField('Start Date', [validators.DataRequired()], format='%Y-%m-%d')
    end_date = DateField('End Date', [validators.DataRequired()], format='%Y-%m-%d')
    skill_involved = StringField('Skills Involved', [validators.DataRequired()])
    submit = SubmitField('Edit')


class EducationForm(FlaskForm):
    degree = StringField('Degree', [validators.DataRequired()])
    field_of_study = StringField('Field of Study', [validators.DataRequired()])
    school = StringField('School', [validators.DataRequired()])
    location = StringField('Location', [validators.DataRequired()])
    start_date = DateField('Start Date', [validators.DataRequired()], format='%Y-%m-%d')
    end_date = DateField('End Date', [validators.DataRequired()], format='%Y-%m-%d')
    achievements = TextAreaField('Achievements')
    submit = SubmitField('Edit')


class BioForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    job_title = StringField('Job Title', [validators.DataRequired()])
    tagline = StringField('Tagline', [validators.DataRequired()])
    summary = TextAreaField('Summary', [validators.DataRequired()])
    profile_pic = StringField('Profile Picture URL', [validators.URL()])
    submit = SubmitField('Edit')


class LicenseCertificationForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    authority = StringField('Authority', [validators.DataRequired()])
    license_number = StringField('License Number', [validators.DataRequired()])
    issue_date = DateField('Issue Date', [validators.DataRequired()], format='%Y-%m-%d')
    expiration_date = DateField('Expiration Date', [validators.DataRequired()], format='%Y-%m-%d')
    certificate_url = StringField('Certificate URL', [validators.URL()])
    ranking = IntegerField('Ranking',[validators.DataRequired()])
    submit = SubmitField('Edit')
