from django.contrib import admin
from .models import *
# Register your models here.

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def export_to_pdf(modeladmin, request, queryset):
    # Create a new PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Generate the report using ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)

    elements = []

    # Define the style for the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Create the table headers
    headers = ['Login_id','name', 'finaltotal', 'Payment_mode', 'timestamp']

    # Create the table data
    data = []
    for obj in queryset:
        data.append([obj.Login_id,obj.name, obj.finaltotal, obj.Payment_mode, obj.timestamp])

    # Create the table
    t = Table([headers] + data, style=style)

    # Add the table to the elements array
    elements.append(t)

    # Build the PDF document
    doc.build(elements)

    return response


export_to_pdf.short_description = "Export to PDF"


class showLogin(admin.ModelAdmin):
    list_display = ['Email', 'Name', 'Phone_no', 'Password', 'Conf_Password', 'Reg_Date', 'Role', 'Status']


admin.site.register(Login, showLogin)


class showUser_Details(admin.ModelAdmin):
    list_display = ['Login_id', 'DOB', 'user_photo', 'Gender', 'Address', 'City_name']


admin.site.register(User_Details, showUser_Details)


class showCategory(admin.ModelAdmin):
    list_display = ['Cat_name']


admin.site.register(Category, showCategory)


class showProduct(admin.ModelAdmin):
    list_display = ['Login_id', 'Cat_id', 'Product_name', 'Product_images', 'Product_description', 'Quantity', 'unit',
                    'Product_price', 'Old_Product_price', 'Product_Status']


admin.site.register(Product, showProduct)


class showOrder(admin.ModelAdmin):
    list_display = ['id','Login_id', 'finaltotal', 'name', 'address', 'Payment_mode', 'Pay_Status', 'STATUS'  ,'timestamp']
    list_filter = ['name','Payment_mode','timestamp']
    actions = [export_to_pdf]


admin.site.register(Order, showOrder)


# class showCard(admin.ModelAdmin):
#     list_display = ['Login_id','Order_id','Holder_name','Expire','Price']
#
# admin.site.register(Card,showCard)

class showFeedback(admin.ModelAdmin):
    list_display = ['Login_id', 'Rating', 'Comment', 'Date']


admin.site.register(Feedback, showFeedback)


class showComplain(admin.ModelAdmin):
    list_display = ['Login_id', 'Subject', 'Message']


admin.site.register(Complain, showComplain)


class showContact_us(admin.ModelAdmin):
    list_display = ['Name', 'Email_id', 'Phone_no', 'Message', 'Timestamp']


admin.site.register(Contact_us, showContact_us)


class showCart(admin.ModelAdmin):
    list_display = ['userid', 'productid', 'quantity', 'totalamount', 'cartstatus', 'orderid']


admin.site.register(Cart, showCart)


class showCard(admin.ModelAdmin):
    list_display = ['nameoncard','card_number', 'card_cvv', 'exp_date', 'card_balance']


admin.site.register(cardDetail, showCard)