from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required
from app.services.product_service import ProductService

product_bp = Blueprint("products", __name__, url_prefix="/")
service = ProductService()


@product_bp.route("/", methods=["GET"])
@login_required
def index():
    products = service.list_products()
    return render_template("index.html", products=products)


@product_bp.route("/products/new", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        try:
            service.create_product(request.form.to_dict())
            flash("Producto creado correctamente.", "success")
            return redirect(url_for("products.index"))
        except ValueError as e:
            flash(str(e), "danger")
            return render_template("form.html", product=request.form, action="create")
    return render_template("form.html", product=None, action="create")


@product_bp.route("/products/<int:product_id>/edit", methods=["GET", "POST"])
@login_required
def edit(product_id):
    product = service.get_product(product_id)
    if product is None:
        abort(404)

    if request.method == "POST":
        try:
            service.update_product(product_id, request.form.to_dict())
            flash("Producto actualizado correctamente.", "success")
            return redirect(url_for("products.index"))
        except ValueError as e:
            flash(str(e), "danger")
            return render_template("form.html", product=request.form, action="edit", product_id=product_id)

    return render_template("form.html", product=product, action="edit", product_id=product_id)


@product_bp.route("/products/<int:product_id>/delete", methods=["POST"])
@login_required
def delete(product_id):
    if service.delete_product(product_id):
        flash("Producto eliminado.", "success")
    else:
        flash("Producto no encontrado.", "danger")
    return redirect(url_for("products.index"))


@product_bp.route("/products/<int:product_id>", methods=["GET"])
@login_required
def detail(product_id):
    product = service.get_product(product_id)
    if product is None:
        abort(404)
    return render_template("detail.html", product=product)
