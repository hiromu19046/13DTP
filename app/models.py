from app.routes import db

#PizzaTopping = db.Table("PizzaTopping", 
#    db.Column("pid", db.Integer, db.ForeignKey("Pizza.id")), 
#    db.Column("tid", db.Integer, db.ForeignKey("Topping.id")))

#class Pizza(db.Model):
#    __tablename__ = "Pizza"
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String())
#    description = db.Column(db.String())
#    photo = db.Column(db.String())
#    base = db.Column(db.Integer, db.ForeignKey("Base.id"))
#    base_name = db.relationship("Base", backref="pizzas")
#    topping = db.relationship("Topping", secondary=PizzaTopping, backref="pizzas")

#class Base(db.Model):
#    __tablename__ = "Base"
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String())
#    description = db.column(db.String())

#class Topping(db.Model):
#    __tablename__ = "Topping"
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String())
#    description = db.column(db.String())

ProductColour = db.Table("ProductColour",
    db.Column("pid", db.Integer, db.ForeignKey("Product.id")),
    db.Column("cid", db.Integer, db.ForeignKey("Colour.id")))

class Category(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    photo = db.Column(db.String())
    group = db.Column(db.String())
    category = db.Column(db.Integer, db.ForeignKey("Category.id"))
    category_name = db.relationship("Category", backref="products")
    colour = db.relationship("Colour", secondary=ProductColour, backref="products")

class Colour(db.Model):
    __tablename__ = "Colour"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    photo = db.Column(db.String())

    