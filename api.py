from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

#DB configs
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Restaurant'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
api = Api(app)
conn = mysql.connect()
cursor = conn.cursor()


#PUT FUNCTIONS
class createItem(Resource):
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type = int, help='Item id')
            parser.add_argument('itemName', type = str, help='item name')
            parser.add_argument('itemCost', type = int, help = 'item cost')
            parser.add_argument('Menu_id', type = int, help='menu id')
            args = parser.parse_args()
            _id = args['id']
            _name = args['itemName']
            _cost = args['itemCost']
            _Menuid = args['Menu_id']
            cursor.callproc('createItem',(_id,_name, _cost, _Menuid))
            data = cursor.fetchall()
            if(len(data)) is 0:
                conn.commit()
                return{'StatusCode':'200','Message':'Item Created'}
            else:
                return{'StatusCode':'1000','Message':str(data[0])}

        except Exception as e:
            return {'error':str(e)}

class createMenu(Resource):
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('Menu_id', type = int, help='Menuid')
            parser.add_argument('Menu_name', type = str, help='Menu name')
            parser.add_argument('Restaurant_id', type = int, help = 'Restaurant\'s id')
            args = parser.parse_args()
            _Menuid = args['Menu_id']
            _Menuname = args['Menu_name']
            _RestID = args['Restaurant_id']
            cursor.callproc('createMenu',(_Menuid,_Menuname, _RestID))
            data = cursor.fetchall()
            if(len(data)) is 0:
                conn.commit()
                return{'StatusCode':'200','Message':'Menu Created'}
            else:
                return{'StatusCode':'1000','Message':str(data[0])}

        except Exception as e:
            return {'error':str(e)}

class createRestaurant(Resource):
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('Restaurant_id', type = int, help='Restaurant id')
            parser.add_argument('Restaurant_name', type = str, help='Restaurant name')
            parser.add_argument('Restaurant_address', type = str, help = 'Restaurant address')
            parser.add_argument('Restaurant_contact', type = int, help='Restaurant contact')
            args = parser.parse_args()
            _id = args['Restaurant_id']
            _name = args['Restaurant_name']
            _contact = args['Restaurant_contact']
            _address = args['Restaurant_address']
            cursor.callproc('createRestaurant',(_id,_name, _address, _contact))
            data = cursor.fetchall()
            if(len(data)) is 0:
                conn.commit()
                return{'StatusCode':'200','Message':'Restaurant Created'}
            else:
                return{'StatusCode':'1000','Message':str(data[0])}

        except Exception as e:
            return {'error':str(e)}



#POST FUNCTIONS
class updateItem(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter id')
            parser.add_argument('Name', type=str, help='Enter old name')
            parser.add_argument('cost', type=int, help='Enter old cost')
            parser.add_argument('NewName', type=str, help='Enter new name')
            parser.add_argument('NewCost', type=int, help='Enter new cost')

            args = parser.parse_args()
            _id = args['id']
            _oldName = args['Name']
            _oldCost = args['cost']
            _updateName = args['NewName']
            _updateCost = args['NewCost']

            cursor.callproc('updateItem',(_id,_updateName, _updateCost, _oldName, _oldCost))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':' Update Successfull\n'}
            else:
                return{'StatusCode':'5xx','Message':'Error while updating'}

        except Exception as e:
            return {'error':str(e)}

class updateMenu(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter old name')
            parser.add_argument('Name', type=str, help='Enter old name')
            parser.add_argument('NewName', type=str, help='Enter new name')
            args = parser.parse_args()
            _id = args['id']
            _oldName = args['Name']
            _updateName = args['NewName']
            cursor.callproc('updateMenu',(_id,_updateName,_oldName))
            data = cursor.fetchall()
            if ((len(data)) is 0):
                conn.commit()
                return{'StatusCode':'200','Message':' Update Successfull\n'}
            else:
                return{'StatusCode':'5xx','Message':str(data[0])}

        except Exception as e:
            return {'error':str(e)}

class updateRestaurant(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter old name')
            parser.add_argument('Name', type=str, help='Enter old name')
            parser.add_argument('Address', type=str, help='Enter old address')
            parser.add_argument('Contact', type=int, help='Enter old contact number')
            parser.add_argument('NewName', type=str, help='Enter new name')
            parser.add_argument('NewAddress', type=str, help='Enter new address')
            parser.add_argument('NewContact', type=int, help='Enter new contact number')

            args = parser.parse_args()
            _id = args['id']
            _oldName = args['Name']
            _oldAddress = args['Address']
            _oldContact = args['Contact']
            _updateName = args['NewName']
            _updateAddress = args['NewAddress']
            _updateContact = args['NewContact']

            cursor.callproc('updateRestaurant',(_id,_updateName, _updateAddress, _updateContact, _oldName, _oldAddress, _oldContact))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':' Update Successfull\n'}
            else:
                return{'StatusCode':'5xx','Message':'Error while updating'}

        except Exception as e:
            return {'error':str(e)}



#GET SPECIFIC FUNCTIONS
class getSpecificItem(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter id')
            parser.add_argument('Name', type=str, help='Enter name')
            parser.add_argument('Cost', type=int, help='Enter cost')
            parser.add_argument('Menu_id', type=int, help='Enter menuid')
            args = parser.parse_args()

            _id = args['id']
            _Name = args['Name']
            _Cost = args['Cost']
            _Menuid = args['Menu_id']

            cursor.callproc('getSpecificItem',(_id,_Name, _Cost, _Menuid))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':str(data[0])}
            else:
                return{'StatusCode':'5xx','Message':'Error while getting information'}

        except Exception as e:
            return {'error':str(e)}

class getSpecificMenu(Resource):
    def ger(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter id')
            parser.add_argument('Name', type=str, help='Enter name')
            parser.add_argument('Restaurant_id', type=int, help='Enter Restaurant id')
            args = parser.parse_args()

            _id = args['id']
            _Name = args['Name']
            _RestID = args['Restaurant_id']
            cursor.callproc('getSpecificMenu',(_id,_Name, _RestID))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':str(data[0])}
            else:
                return{'StatusCode':'5xx','Message':'Error while getting information'}

        except Exception as e:
            return {'error':str(e)}

class getSpecificRestaurant(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter id')
            parser.add_argument('Name', type=str, help='Enter name')
            parser.add_argument('Address', type=str, help='Enter address')
            parser.add_argument('Contact', type=int, help='Enter contact number')
            args = parser.parse_args()

            _id = args['id']
            _Name = args['Name']
            _Address = args['Address']
            _Contact = args['Contact']

            cursor.callproc('getSpecificRestaurant',(_id,_Name, _Address, _Contact))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':str(data[0])}
            else:
                return{'StatusCode':'5xx','Message':'Error while getting information'}

        except Exception as e:
            return {'error':str(e)}



#GET ALL FUNCTIONS
class getItems(Resource):
    def get(self):
        cursor.callproc('getItems')
        data = cursor.fetchall()
        if ((len(data)) is not 0):
            conn.commit()
            return{'StatusCode':'200','Message':str(data)}
        else:
            return{'StatusCode':'5xx','Message':'Error while getting information'}

class getMenus(Resource):
    def get(self):
        cursor.callproc('getMenus')
        data = cursor.fetchall()
        if ((len(data)) is not 0):
            conn.commit()
            return{'StatusCode':'200','Message':str(data)}
        else:
            return{'StatusCode':'5xx','Message':'Error while getting information'}

class getRestaurants(Resource):
    def get(self):
        cursor.callproc('getRestaurants')
        data = cursor.fetchall()
        if ((len(data)) is not 0):
            conn.commit()
            return{'StatusCode':'200','Message':str(data)}
        else:
            return{'StatusCode':'5xx','Message':'Error while getting information'}



#DELETE FUNCTIONS
class deleteItem(Resource):
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter id')
            parser.add_argument('Name', type=str, help='Enter name')
            parser.add_argument('Cost', type=str, help='Enter cost')
            parser.add_argument('Menuid', type=int, help='Enter menu id')
            args = parser.parse_args()

            _id = args['id']
            _Name = args['Name']
            _Cost = args['Cost']
            _Menuid = args['Menuid']

            cursor.callproc('deleteItem',(_id,_Name, _Cost, _Menuid))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':str(data)}
            else:
                return{'StatusCode':'5xx','Message':str(data[0])}

        except Exception as e:
            return {'error':str(e)}

class deleteMenu(Resource):
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter id')
            parser.add_argument('Name', type=str, help='Enter name')
            parser.add_argument('Restaurant_id', type=int, help='Enter Restaurant id')
            args = parser.parse_args()

            _id = args['id']
            _Name = args['Name']
            _RestID = args['Restaurant_id']
            cursor.callproc('deleteMenu',(_id,_Name, _RestID))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':str(data)}
            else:
                return{'StatusCode':'5xx','Message':str(data[0])}

        except Exception as e:
            return {'error':str(e)}


class deleteRestaurant(Resource):
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, help='Enter id')
            parser.add_argument('Name', type=str, help='Enter name')
            parser.add_argument('Address', type=str, help='Enter address')
            parser.add_argument('Contact', type=int, help='Enter contact number')
            args = parser.parse_args()

            _id = args['id']
            _Name = args['Name']
            _Address = args['Address']
            _Contact = args['Contact']
            cursor.callproc('deleteRestaurant',(_id,_Name, _Address, _Contact))
            data = cursor.fetchall()
            if ((len(data)) is not 0):
                conn.commit()
                return{'StatusCode':'200','Message':str(data)}
            else:
                return{'StatusCode':'5xx','Message':str(data[0])}

        except Exception as e:
            return {'error':str(e)}

api.add_resource(createRestaurant,'/createRestaurant')
api.add_resource(updateRestaurant,'/updateRestaurant')
api.add_resource(getSpecificRestaurant,'/getSpecificRestaurant')
api.add_resource(getRestaurants,'/getRestaurants')
api.add_resource(deleteRestaurant,'/deleteRestaurant')


api.add_resource(createMenu,'/createMenu')
api.add_resource(updateMenu,'/updateMenu')
api.add_resource(getSpecificMenu,'/getSpecificMenu')
api.add_resource(getMenus,'/getMenus')
api.add_resource(deleteMenu,'/deleteMenu')


api.add_resource(createItem,'/createItem')
api.add_resource(updateItem,'/updateItem')
api.add_resource(getSpecificItem,'/getSpecificItem')
api.add_resource(getItems,'/getItems')
api.add_resource(deleteItem,'/deleteItem')



if __name__ == '__main__':
    app.run(debug=True)


















'''
DELIMITER $$
USE `Restaurant`$$
CREATE PROCEDURE `deleteRestaurant` (
IN name varchar(100),
IN address varchar(1000),
IN contact int
)
BEGIN

if ( select exists (select 1 from RestaurantTable where Restaurant_name = name and Restaurant_address = address or Restaurant_name = name and Restaurant_contact = contact) ) THEN

    DELETE FROM RestaurantTable WHERE Restaurant_name = name and Restaurant_address = address or Restaurant_name = name and Restaurant_contact = contact;
    select 'Restaurant Deleted !!';

ELSE
SELECT "Restaurant not found. Hence not deleted";

END IF;

END$$

DELIMITER ;



DELIMITER $$
USE `Restaurant`$$
CREATE PROCEDURE `updateRestaurant` (
IN _updateName varchar(100),
IN _updateAddress varchar(100),
IN _updateContact int,
IN _oldName varchar(100),
IN _oldAddress varchar(100),
IN _oldContact int
)
BEGIN

if ( select exists (select 1 from RestaurantTable where Restaurant_name = _oldName) ) THEN
	UPDATE RestaurantTable
	SET Restaurant_name = _updateName
	WHERE Restaurant_name = _oldName;
    select 'Restaurant Name';
    END IF;

if ( select exists (select 1 from RestaurantTable where Restaurant_address = _oldAddress) ) THEN
	UPDATE RestaurantTable
	SET Restaurant_address = _updateAddress
	WHERE Restaurant_address = _oldAddress;
    select 'Restaurant Address';
    END IF;

if ( select exists (select 1 from RestaurantTable where Restaurant_contact = _oldContact) ) THEN
	UPDATE RestaurantTable
	SET Restaurant_contact = _updateContact
	WHERE Restaurant_contact = _oldContact;
    select 'Restaurant Contact';
END IF;

END$$

DELIMITER ;
'''
