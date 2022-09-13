# def change_format(data):
#     dict={}
#     for k in data: 
#         dict[k['key']]=k['value']
#     return dict

# from django.db import connection

# def my_custom_sql():
#     with connection.cursor() as cursor:
#         import pdb;pdb.set_trace()
#         query = "select json_object(s.key, s.value) from  app_store s "
#         cursor.execute(query)
#         row = cursor.fetchall()
#     return row