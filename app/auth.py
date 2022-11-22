from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

def Email_OR_Username():
  def get_user(self, user_id):
    try:
      