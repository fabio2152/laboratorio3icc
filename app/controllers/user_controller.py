from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.services.user_service import UserService
from app.utils.decorators import admin_required

user_bp = Blueprint("users", __name__, url_prefix="/users")
service = UserService()


@user_bp.route("/")
@login_required
def index():
    users = service.list_users()
    return render_template("users/index.html", users=users)


@user_bp.route("/new", methods=["GET", "POST"])
@login_required
@admin_required
def create():
    if request.method == "POST":
        try:
            service.create_user(request.form.to_dict())
            flash("Usuario creado correctamente.", "success")
            return redirect(url_for("users.index"))
        except ValueError as e:
            flash(str(e), "danger")
            return render_template("users/form.html", user=request.form, action="create")
    return render_template("users/form.html", user=None, action="create")


@user_bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit(user_id):
    user = service.get_user(user_id)
    if user is None:
        abort(404)
    if request.method == "POST":
        try:
            service.update_user(user_id, request.form.to_dict())
            flash("Usuario actualizado correctamente.", "success")
            return redirect(url_for("users.index"))
        except ValueError as e:
            flash(str(e), "danger")
            return render_template("users/form.html", user=request.form, action="edit", user_id=user_id)
    return render_template("users/form.html", user=user, action="edit", user_id=user_id)


@user_bp.route("/<int:user_id>/delete", methods=["POST"])
@login_required
@admin_required
def delete(user_id):
    try:
        service.delete_user(user_id, current_user_id=current_user.id)
        flash("Usuario eliminado.", "success")
    except ValueError as e:
        flash(str(e), "danger")
    return redirect(url_for("users.index"))
