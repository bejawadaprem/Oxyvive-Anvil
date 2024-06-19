from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.aviailable_Hospital_Address')

  def primary_color_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.availabe_vehical_services')

  def primary_color_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.available_zym_address')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def text_box_1_change(self, **event_args):
      # Get the query from the text box
      query = self.text_box_1.text
      if len(query) > 3:
          # Call the server function to get location data
          result = anvil.server.call('get_location', query)
          self.repeating_panel_1.visible=True
          if 'error' in result:
              alert(result['error'])
          else:
              # Update the repeating panel with location suggestions
              self.repeating_panel_1.items = result['results']

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('home')

