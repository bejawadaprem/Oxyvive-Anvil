import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
import base64

@anvil.server.callable
def user(id,username,email,password,phone,pincode,wallet_balance):
  app_tables.users.add_row(id=id, username=username, email=email, password=password,phone=phone,pincode=pincode,wallet_balance=wallet_balance)
  
@anvil.server.callable
def BookSlot(slot_id, user_id, username,book_date,book_time):
  app_tables.bookslot.add_row(slot_id=slot_id, user_id=user_id, username=username, book_date=book_date, book_time=book_time)

@anvil.server.callable
def Oxiclinics(id, name, email, password, phone, address, Oxiclinics_Name, established_year, District, State, pincode, address_2, capsules, medical_licence, building_licence):
  app_tables.oxiclinics.add_row(id=id, name=name, email=email, password=password, phone=phone, address=address, Oxiclinics_Name=Oxiclinics_Name, established_year=established_year, District=District, State=State, pincode=pincode, address_2=address_2, capsules=capsules, medical_licence=medical_licence, building_licence=building_licence)

@anvil.server.callable
def Oxiwheels(id, name, email, password, phone, address, Oxiwheels_Name, model_year, District, State, pincode, address_2, capsules, vehicle_rc, driving_licence):
  app_tables.oxiwheels.add_row(id=id, name=name, email=email, password=password, phone=phone, address=address, Oxiwheels_Name=Oxiwheels_Name, model_year=model_year, District=District, State=State, pincode=pincode, address_2=address_2, capsules=capsules, vehicle_rc=vehicle_rc, driving_licence=driving_licence)

@anvil.server.callable
def Oxigyms(id, name, email, password, phone, address, Oxigyms_Name, established_year, District, State, pincode, address_2, capsules, gym_licence, building_licence):
  app_tables.oxigyms.add_row(id=id, name=name, email=email, password=password, phone=phone, address=address, Oxigyms_Name=Oxigyms_Name, established_year=established_year, District=District, State=State, pincode=pincode, address_2=address_2, capsules=capsules, gym_licence=gym_licence, building_licence=building_licence)

@anvil.server.callable
def create_media_object(content_type, file_data_base64, file_name):
    # Decode the base64 string to get the bytes data
    file_data = base64.b64decode(file_data_base64)
    media_object = anvil.media.BlobMedia(content_type, file_data, file_name)
    return media_object

@anvil.server.callable
def check_internet_status():
    # Perform a simple server call to check connectivity
    return True
# @anvil.server.callable
# def add_info(email, username, password, phone,pincode):
#     user_row = app_tables.users.add_row(
#         email=email,
#         username=username,
#         password=password,
 
#         phone=phone,
#         pincode=pincode
#     )
#     return user_row
@anvil.server.callable
def check_login_credentials(email, password):
    # Retrieve the user record based on the provided email address
    user = app_tables.users.get(email=email)
    
    # Check if a user exists with the provided email address and password matches
    if user and user['password'] == password:
        return True
    else:
        return False


import hashlib

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
