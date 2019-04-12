from mton.models import Student, Lecture, Enrollment

create_student = Student.objects.create

s1 = create_student(name='aaa')
s2 = create_student(name='bbb')
s3 = create_student(name='ccc')

l1 = Lecture.objects.create(title='컴개')
l2 = Lecture.objects.create(title='자료구조')
l3 = Lecture.objects.create(title='알고리즘')

Enrollment.objects.create(student=s2, lecture=l1)
Enrollment.objects.create(student=s1, lecture=l3)
Enrollment.objects.create(student=s1, lecture=l3)