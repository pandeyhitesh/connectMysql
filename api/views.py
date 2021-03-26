from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . serializers import ProductSerializer
from . models import Product
from . models import CsaAll, Student_model, NoticeModel, EventsModel

from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from api.serializers import CSAUserSerializer, EventSerializer, NoticeSerializer, ProjectSerializer, StudentSerializer
from api.models import Project_model


from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail view':'/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>', 
        'Delete': '/product-delete/<int:id>',
    }

    return Response(api_urls)


'''
    APIs for Product
'''
@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
    # product = Product.objects.get(id=pk)

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['GET'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    
    return Response('items deleted successfully')


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''
    APIs for User Registration
'''


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''
    APIs for User Login
'''



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)




'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''
    name: CsaAll User View
    Description: APIs for CsaAll Model
    auther: pandeyhitesh
'''


'''
    APIs for Show All User
'''
@api_view(['GET'])
def showAllCsaUser(request):
    csa_users = CsaAll.objects.all()
    serializer = CSAUserSerializer(csa_users, many=True)
    return Response(serializer.data)

'''
    APIs for CSAAll Create User
'''
@api_view(['POST'])
def createCsaUser(request):
    # product = Product.objects.get(id=pk)

    serializer = CSAUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

'''
    APIs for CSAAll View one User
'''
@api_view(['GET'])
def viewCsaUser(request,user_id):
    csa_user = CsaAll.objects.get(user_id=user_id)
    serializer = CSAUserSerializer(csa_user, many=False)
    return Response(serializer.data)


'''
    APIs for CSAAll Update A User Detail
'''
@api_view(['POST'])
def updateCsaUser(request,pk):
    csa_user = CsaAll.objects.get(id=pk)
    serializer = CSAUserSerializer(instance=csa_user,data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

'''
    APIs for CSAAll Delete a User
'''
@api_view(['GET'])
def deleteCsaUser(request,pk):
    csa_user = CsaAll.objects.get(id=pk)
    csa_user.delete()
    
    return Response('User deleted successfully')















'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''
    name: StudentMOdel Views
    Description: APIs for StudentModel
    auther: pandeyhitesh
'''


'''
    APIs for Show All Students
'''
@api_view(['GET'])
def showAllStudents(request):
    Students = Student_model.objects.all()
    serializer = StudentSerializer(Students, many=True)
    return Response(serializer.data)

'''
    APIs for Create Student
'''
@api_view(['POST'])
def createStudent(request):
    # product = Product.objects.get(id=pk)

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

'''
    APIs for StudentModel View one Student
'''
@api_view(['GET'])
def viewStudent(request,pk):
    student = Student_model.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


'''
    APIs for StudentModel Update A Student Detail
'''
@api_view(['POST'])
def updateStudent(request,pk):
    student = Student_model.objects.get(id=pk)
    serializer = StudentSerializer(instance=student,data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

'''
    APIs for StudentModel Delete a Student
'''
@api_view(['GET'])
def deleteStudent(request,pk):
    student = Student_model.objects.get(id=pk)
    student.delete()
    
    return Response('Student deleted successfully')










'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''
    name: NoticeModel Views
    Description: APIs for NoticeModel
    auther: pandeyhitesh
'''


'''
    APIs for Show All Notices
'''
@api_view(['GET'])
def showAllNotices(request):
    notices = NoticeModel.objects.all()
    serializer = NoticeSerializer(notices, many=True)
    return Response(serializer.data)

'''
    APIs for Create Notice
'''
@api_view(['POST'])
def createNotice(request):
    # product = Product.objects.get(id=pk)

    serializer = NoticeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

'''
    APIs for NoticeModel View one Notice
'''
@api_view(['GET'])
def viewNotice(request,pk):
    notice = NoticeModel.objects.get(id=pk)
    serializer = NoticeSerializer(notice, many=False)
    return Response(serializer.data)


# '''
#     APIs for StudentModel Update A Student Detail
# '''
# @api_view(['POST'])
# def updateCsaUser(request,pk):
#     student = Student_model.objects.get(id=pk)
#     serializer = StudentSerializer(instance=student,data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

'''
    APIs for NoticeModel Delete a Notice
'''
@api_view(['GET'])
def deleteNotice(request,pk):
    notice = NoticeModel.objects.get(id=pk)
    notice.delete()
    
    return Response('Notice deleted successfully')









'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''
    name: EventsModel Views
    Description: APIs for EventsModel
    auther: pandeyhitesh
'''


'''
    APIs for Show All Events
'''
@api_view(['GET'])
def showAllEvents(request):
    events = EventsModel.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

'''
    APIs for Create Event
'''
@api_view(['POST'])
def createEvent(request):
    # product = Product.objects.get(id=pk)

    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

'''
    APIs for EventsModel View one Event
'''
@api_view(['GET'])
def viewEvent(request,pk):
    event = EventsModel.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


# '''
#     APIs for StudentModel Update A Student Detail
# '''
# @api_view(['POST'])
# def updateCsaUser(request,pk):
#     student = Student_model.objects.get(id=pk)
#     serializer = StudentSerializer(instance=student,data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

'''
    APIs for EventsModel Delete a Event
'''
@api_view(['GET'])
def deleteEvent(request,pk):
    event = EventsModel.objects.get(id=pk)
    event.delete()
    
    return Response('Event deleted successfully')












'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''
    name: ProjectModel Views
    Description: APIs for ProjectModel
    auther: pandeyhitesh
'''


'''
    APIs for Show All Projects
'''
@api_view(['GET'])
def showAllProjects(request):
    projects = Project_model.objects.all()
    serializer = ProductSerializer(projects, many=True)
    return Response(serializer.data)

'''
    APIs for Create Project
'''
@api_view(['POST'])
def createProject(request):
    # product = Product.objects.get(id=pk)

    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

'''
    APIs for Project_model View one Project
'''
@api_view(['GET'])
def viewProject(request,pk):
    project = Project_model.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


'''
    APIs for Project_model Update A Project Detail
'''
@api_view(['POST'])
def updateProject(request,pk):
    project = Project_model.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project,data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

'''
    APIs for Project_model Delete a Project
'''
@api_view(['GET'])
def deleteProject(request,pk):
    project = Project_model.objects.get(id=pk)
    project.delete()
    
    return Response('Project deleted successfully')
