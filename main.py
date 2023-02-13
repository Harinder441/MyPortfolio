from flask import Flask, render_template, redirect, request, flash, send_from_directory
from flask_bootstrap import Bootstrap
from forms import UserForm, LoginForm
from EditForms import *
from database import db, create_all, Bio, Education, LicenseCertification, Project, Experience, Award, Skill, UserMsg, \
    sampledata
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from notifier import send_mail, msg_format
from dotenv import load_dotenv
from datetime import date
import os

load_dotenv()

users = {'admin': {
    'password': 'pbkdf2:sha256:260000$DQS0DPTWGn0eHkvK$82e919a0a59d1c5f6f1fa4d5acbb7f2b25d7161635ad07dcfc09fb59376af692',
    'active': True}
         }

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get("APP_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    # create_all()
    # sampledata()
    pass


class User(UserMixin):
    pass


# Load the user
@login_manager.user_loader
def load_user(username):
    if username not in users:
        return

    user = User()
    user.id = username
    user.active = users[username]['active']
    return user


@app.route("/")
def home():
    projects = Project.query.order_by(Project.ranking.asc()).all()[:3]
    skills = Skill.query.order_by(Skill.ranking.asc()).all()
    bio = db.session.query(Bio).all()
    form = UserForm()
    return render_template('index.html', projects=projects, skills=skills, bio=bio, form=form)


@app.route("/projects")
def projects():
    all_projects = Project.query.order_by(Project.ranking.asc()).all()
    return render_template('projects.html', projects=all_projects)


@app.route("/cv")
def cv():
    return render_template("cv.html")


@app.route('/download')
def download():
    return send_from_directory('static', path="files/HarinderSingh.pdf")


@app.route("/dataHandle", methods=["GET", "POST"])
def user_data():
    form = request.form
    new_msg = UserMsg(email=form['email'], massage=f"On {str(date.today())} read as {form['massage']}")
    db.session.add(new_msg)
    db.session.commit()
    # msg = msg_format(from_p="My Portfolio",
    #                  to="me", subject="New message from Portfolio.", body=f"{form['email']} \n{form['massage']}")
    # Email sending not working with render
    # send_mail(to_ad= os.environ.get("TO_EMAIL"),massage=msg)
    flash(message="Received your Message. Thank you!", category="information")
    return redirect(app.url_for('home'))


# --------------------------------------login route setup---------


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username not in users:
            flash(message="No user Exist", category="error")
            return render_template("login.html", form=form)

        user = User()
        user.id = username

        if check_password_hash(users[username]['password'], password):
            login_user(user)
            flash(message="Login success", category="information")
            return redirect(app.url_for('home'))
        else:
            flash(message="Password does not match,Try again!", category="error")
            return render_template("login.html", form=form)

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(app.url_for('home'))


# ---------------------------------login-required--------------------------------
@app.route("/msg")
@login_required
def all_msg():
    msgs = db.session.query(UserMsg).all()
    return render_template("msg.html", messages=msgs)


@app.route('/edit/<string:model_name>/<int:model_id>', methods=['GET', 'POST'])
@login_required
def edit(model_name, model_id):
    if model_name == 'project':
        model = Project.query.get(model_id)
        form = ProjectForm()
        if form.validate_on_submit():
            model.title = form.title.data
            model.description = form.description.data
            model.tech_involved = form.tech_involved.data
            model.github_link = form.github_link.data
            model.image_url = form.image_url.data
            model.ranking = form.ranking.data

            db.session.commit()
            flash('Project has been updated', 'success')
            return redirect(app.url_for('projects'))
        elif request.method == 'GET':
            form.title.data = model.title
            form.description.data = model.description
            form.tech_involved.data = model.tech_involved
            form.github_link.data = model.github_link
            form.image_url.data = model.image_url
            form.ranking.data = model.ranking

        return render_template('edit.html', form=form, model_name="project", id_=model_id)

    elif model_name == 'skill':
        model = Skill.query.get(model_id)
        form = SkillsForm()
        if form.validate_on_submit():
            model.title = form.title.data
            model.description = form.description.data
            model.proficiency = form.proficiency.data
            model.ranking = form.ranking.data
            db.session.commit()
            flash('Skill has been updated', 'success')
            return redirect(app.url_for('home'))
        elif request.method == 'GET':
            form.title.data = model.title
            form.description.data = model.description
            form.proficiency.data = model.proficiency
            form.ranking.data = model.ranking
        return render_template('edit.html', form=form, model_name="skill", id_=model_id)


@app.route('/add/<string:model_name>/', methods=['GET', 'POST'])
@login_required
def add(model_name):
    if model_name == 'project':
        form = ProjectForm()
        form.submit.name = "add"
        if form.validate_on_submit():
            model = Project()
            model.title = form.title.data
            model.description = form.description.data
            model.tech_involved = form.tech_involved.data
            model.github_link = form.github_link.data
            model.image_url = form.image_url.data
            model.ranking = form.ranking.data
            db.session.add(model)
            db.session.commit()
            flash('New project has been added', 'success')
            return redirect(app.url_for('projects'))
        return render_template('add.html', form=form, model_name=model_name)

    elif model_name == 'skill':
        form = SkillsForm()
        if form.validate_on_submit():
            model = Skill()
            model.title = form.title.data
            model.description = form.description.data
            model.proficiency = form.proficiency.data
            model.ranking = form.ranking.data
            db.session.add(model)
            db.session.commit()
            flash('New skill has been added', 'success')
            return redirect(app.url_for('home'))
        return render_template('add.html', form=form, model_name=model_name)


@app.route('/delete/<string:model_name>/<int:model_id>')
@login_required
def delete(model_name, model_id):
    if model_name == 'project':
        model = Project.query.get(model_id)
        db.session.delete(model)
        db.session.commit()
        flash('Project has been deleted', 'success')
        return redirect(app.url_for('projects'))
    elif model_name == 'skill':
        model = Skill.query.get(model_id)
        db.session.delete(model)
        db.session.commit()
        flash('Skill has been deleted', 'success')
        return redirect(app.url_for('home'))
    elif model_name == 'usermsg':
        model = UserMsg.query.get(model_id)
        db.session.delete(model)
        db.session.commit()
        return redirect(app.url_for('all_msg'))


if __name__ == '__main__':
    app.run(debug=True)
