from datetime import date

from peewee import *

db = MySQLDatabase('spider', host="localhost", port=3306, user="loli", password="12358")


class User(Model):
    # 默认会自动添加 id 为主键，不显式指定的话，
    # id = IntegerField(primary_key=True)
    name = CharField(max_length=10)
    age = IntegerField()
    birthday = DateField(null=False)

    class Meta:
        database = db
        table_name = "temp_user"


if __name__ == "__main__":
    db.create_tables([User])
    user1 = User(name="mps", age=12, birthday=date(1960, 1, 15))
    user1.save()

    # uu = User.select().where(User.name == 'mps').get()
    uu = User.get(User.name == 'mps')
    print(uu)

    query = User.select().where(User.name.contains("mps"))
    for u in query:
        print(u.name, u.age)
