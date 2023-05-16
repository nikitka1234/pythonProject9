from flask import render_template, redirect, url_for

from . import app, db
from .models import Category, News, Feedback
from .forms import NewsForm, FeedbackForm, CategoryForm


def index():
    content = News.query.all()
    categories = Category.query.all()

    return render_template("index.html", content=content, categories=categories)


def feedback():
    form = FeedbackForm()
    feedback_list = Feedback.query.all()
    categories = Category.query.all()

    if form.validate_on_submit():
        feedback_model = Feedback()

        feedback_model.name = form.name.data
        feedback_model.text = form.text.data
        feedback_model.email = form.email.data
        feedback_model.rating = form.rating.data

        db.session.add(feedback_model)
        db.session.commit()

        return redirect(url_for("feedback"))

    return render_template("feedback.html", form=form, feedback_list=feedback_list, categories=categories)


def add_news():
    form = NewsForm()
    categories = Category.query.all()
    form.category.choices = [cat.title for cat in categories]

    if form.validate_on_submit():
        news_model = News()

        news_model.title = form.title.data
        news_model.text = form.text.data
        news_model.category_id = Category.query.filter(Category.title == form.category.data).first().id

        db.session.add(news_model)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_news.html", form=form, categories=categories)


def add_category():
    form = CategoryForm()
    categories = Category.query.all()

    if form.validate_on_submit():
        category_model = Category()

        category_model.title = form.title.data

        db.session.add(category_model)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_category.html", form=form, categories=categories)


def news_detail(id):
    content = News.query.get(id)
    categories = Category.query.all()

    return render_template("news_detail.html", news=content, categories=categories)


def category(id):
    category_object = Category.query.get(id)
    news = category_object.news
    category_name = category_object.title
    categories = Category.query.all()

    return render_template("category.html", category_name=category_name, news=news, categories=categories)


app.add_url_rule("/", "index", index)
app.add_url_rule("/feedback", "feedback", feedback, methods=["GET", "POST"])
app.add_url_rule("/add_news", "add_news", add_news, methods=["GET", "POST"])
app.add_url_rule("/add_category", "add_category", add_category, methods=["GET", "POST"])
app.add_url_rule("/news_detail/<int:id>", "news_detail", news_detail)
app.add_url_rule("/category/<string:id>", "category", category)
