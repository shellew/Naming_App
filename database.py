import sqlite3

conn = sqlite3.connect('naming_app.db')

create_users_table = '''
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT,
    register_date DATETIME,
    login_date DATETIME,
    withdrawal DATETIME
    );
    '''
    
create_name_suggestions_table = '''
CREATE TABLE NameSuggestions (
    suggestion_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    suggestion_name TEXT,
    suggestion_date DATETIME
);
'''

create_images_table = '''
CREATE TABLE Images (
    image_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    image_file_name TEXT,
    image_upload_date DATETIME,
    image_url TEXT,
    suggestion_id INTEGER
);
'''

create_privacy_settings_table = '''
CREATE TABLE PrivacySettings (
    privacy_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    setting_update_date DATETIME
);
'''
    
conn.execute(create_users_table)
conn.execute(create_name_suggestions_table)
conn.execute(create_images_table)
conn.execute(create_privacy_settings_table)

conn.commit()
conn.close()