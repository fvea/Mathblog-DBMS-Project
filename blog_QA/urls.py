""" Defines URL patterns for blog_QA """

from django.urls import path

from . import views

app_name = 'blog_QA'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('entries/<int:topic_id>/', views.entries, name='entries'),
    # Page for editing a topic.
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for deleting a topic.
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    # Page for deleting an entry.
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]