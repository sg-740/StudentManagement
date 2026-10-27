from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


def add_student(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")
        marks = request.POST.get("marks")

        Student.objects.create(
            name=name,
            age=age,
            course=course,
            marks=marks
        )

        return redirect("student_list")

    return render(
        request,
        "students/add_student.html"
    )


def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.course = request.POST.get("course")
        student.marks = request.POST.get("marks")

        student.save()

        return redirect("student_list")

    return render(
        request,
        "students/edit_student.html",
        {"student": student}
    )


def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.delete()

        return redirect("student_list")

    return render(
        request,
        "students/delete_student.html",
        {"student": student}
    )