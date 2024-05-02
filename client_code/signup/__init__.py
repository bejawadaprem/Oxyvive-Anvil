from ._anvil_designer import signupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class signup(signupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    username=self.text_box_1.text
    email=self.text_box_2.text
    password=self.text_box_3.text
    phone=self.text_box_4.text
    pincode=self.text_box_5.text
    # app_tables.users.add_row(username, email, password, phone, pincode)
    # anvil.server.call('add_info',username, email, password, phone, pincode)
    try: 
      # If not present, proceed to insert the new user
      rows = app_tables.users.search()
      id = f"C{len(rows):04d}"
      app_tables.users.add_row(id = id, username =username, email = email, password = password, phone = int(phone),pincode=pincode)
      """This method is called when the button is clicked"""
      alert (self.text_box_2.text + ' added')
      open_form('login')
    except Exception as e:
      print(e)
      pass

    """This method is called when the button is clicked"""
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("login")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("servicers_registration_form.servicers_registration_form_main")
