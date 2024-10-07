from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import PersonalDetail, PDFFile  # Import your model
from .serializers import PersonalDetailSerializer  # Import your serializer
from .serializers import PDFFileSerializer  # Import your serializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from pdf2image import convert_from_path
import os
import pytesseract as tess
from PIL import Image


# Set the Tesseract-OCR executable path
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




class PersonalDetailViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetail.objects.all()
    serializer_class = PersonalDetailSerializer
    permission_classes = [AllowAny]  # Allow anyone to access this API

@api_view(['POST'])
def save_personal_details(request):
    if request.method == 'POST':
        serializer = PersonalDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt  # Use only for development; not recommended for production!
def file_upload_view(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # save in database
        pdf_file_instance = PDFFile(file=uploaded_file)
        pdf_file_instance.save() 
        
        # Save the file
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        pdf_file_path = os.path.join(fs.location, filename)  # Get full path of the saved PDF

        try:
            # Convert PDF to images
            images = convert_from_path(pdf_file_path, poppler_path=r"C:\Users\ACER\Downloads\Release-24.07.0-0\poppler-24.07.0\Library\bin")

            # Save images and extract text
            image_paths = []
            extracted_text = ""
            for i, image in enumerate(images):
                image_filename = f"{os.path.splitext(filename)[0]}_page_{i + 1}.png"  # Create image filename
                image_path = os.path.join(fs.location, image_filename)  # Full path for saving image
                image.save(image_path, "PNG")  # Save image
                image_paths.append(fs.url(image_filename))  # Store URL for response
                
                # Extract text from the image
                text = tess.image_to_string(image)
                extracted_text += text + "\n"  # Append the text from each image

            # Return a JSON response with image URLs and extracted text file URL
            return JsonResponse({
                'message': 'File uploaded and converted successfully',
                'images': image_paths,  # URLs of the converted images
                'extracted_text': extracted_text.strip() 
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
