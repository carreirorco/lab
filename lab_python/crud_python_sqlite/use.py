from dml import db_insert, db_select, db_update, db_delete
from pprint import pprint

# db_insert('Rafael', '9811112222', 'rafael@gmail.com')
# db_insert('Vanessa', '9811112222', 'vanessa@gmail.com')
# db_insert('Laura', '9811112222', 'laura@gmail.com')

pprint(db_select('9811112222', 'phone'))