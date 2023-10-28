from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
import jwt
import pymysql


# menghubungkan ke gameitembase MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='tokodm',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
@view_config(route_name='index', renderer='json',  request_method="GET")
def index(request):
    return {
        'message': 'Server Running!',
        'description': 'Hello World!'
    }


def auth_jwt_verify(request):
    authentication_header = request.cookies.get('token')
    if authentication_header:
        try:
            decoded_user = jwt.decode(
                authentication_header, 'secret', algorithms=['HS256'])
            with connection.cursor() as cursor:
                sql = "SELECT jwt_token FROM tokens WHERE user_id=%s"
                cursor.execute(sql, (decoded_user['sub'],))
                result = cursor.fetchone()
            if result:
                return decoded_user
        except jwt.ExpiredSignatureError:
            request.response.status = 401  # tidak terdeteksi
    return None


# endpoint item atau membaca gameitem
@view_config(route_name='product', renderer="json", request_method="GET")
def product(request):

    auth_user = auth_jwt_verify(request)
    if auth_user:
        with connection.cursor() as cursor:
            sql = "SELECT id,nama,price FROM tokodm WHERE user_id=%s"
            cursor.execute(sql, (auth_user['sub'],))
            result = cursor.fetchall()
            

        gameitem = {}
        for item in result:
            gameitem[item['id']] = {
                'id': item['id'],
                'nama': item['nama'],
                'price': item['price'],
            }
        return {
            'message': 'ok',
            'description': 'Berhasil mendapatkan gameitem!',
            'gameitem': gameitem
        }
    else:
        request.response.status = 401  # Unauthorized
        return {'message': 'Unauthorized', 'description': 'token not found'}


# endpoint create gameitem tokodm
@view_config(route_name='create-gameitem', request_method='POST', renderer="json")
def tokodm_create(request):
    auth_user = auth_jwt_verify(request)
    if auth_user:
        with connection.cursor() as cursor:
            sql = "INSERT INTO tokodm (nama, price) VALUES (%s, %s, %s)"
            cursor.execute(sql, (request.POST['nama'], request.POST['price'], auth_user['sub'],))
            connection.commit()
        return {'message': 'ok', 'description': 'berhasil membuat gameitem ', 'gameitem': [request.POST['nama'], request.POST['price']]}
    else:
        request.response.status = 401
        return {'message': 'failed', 'description': 'token tidak ditemukan'}


# endpoint update gameitem tokodm
@view_config(route_name='update-gameitem', request_method='PUT', renderer="json")
def tokodm_update(request):
    auth_user = auth_jwt_verify(request)
    if auth_user:
        with connection.cursor() as cursor:
            sql = "UPDATE tokodm SET nama=%s, price=%s WHERE id=%s"
            cursor.execute(sql, (request.POST['nama'], request.POST['price'],
                            auth_user['sub'], request.POST['id']))
            connection.commit()
            return {'message': 'ok', 'description': 'berhasil membuat gameitem', 'gameitem': [request.POST['nama'], request.POST['price'],]}
    else:
        request.response.status = 401
        return {'message': 'failed', 'description': 'token tidak ditemukan'}


# endpoint untuk menghapus gameitem tokodm
@view_config(route_name='delete-gameitem', request_method='DELETE', renderer="json")
def tokodm_delete(request):
    auth_user = auth_jwt_verify(request)
    if auth_user:
        with connection.cursor() as cursor:
            sql = "SELECT id,nama,price FROM tokodm WHERE user_id=%s"
            cursor.execute(sql, (auth_user['sub'],))
            result = cursor.fetchall()
            gameitem = {}
            for item in result:
                gameitem = {
                'id': item['id'],
                'nama': item['nama'],
                'price': item['price'],
                }
            sql = "DELETE FROM tokodm WHERE id=%s"
            cursor.execute(sql, (request.POST['id']))
            connection.commit()
        return {'message': 'ok', 'description': 'menghapus gameitem berhasil', 'gameitem': gameitem}
    else:
        request.response.status = 401
        return {'message': 'failed', 'description': 'token tidak ditemukan'}


# fungsi endpoint logout
if __name__ == "__main__":
    with Configurator() as config:
        config = Configurator(settings={'jwt.secret': 'secret'})
        # mengkonfigurasi endpoint
        config.add_route('index', '/')
        config.add_route('product', '/product')
        config.add_route('create-gameitem', '/create')
        config.add_route('update-gameitem', '/update')
        config.add_route('delete-gameitem', '/delete')
        config.scan()
        app = config.make_wsgi_app()
    # Menjalankan aplikasi pada server lokal
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()