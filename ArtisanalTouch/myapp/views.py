from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Sum


# Create your views here.

def yourorders(request):
    uid = request.session["logid"]
    getdata = Order.objects.filter(Login_id=uid)
    print(getdata)
    context = {
        "yourorder": getdata
    }
    return render(request, "yourorders.html", context)


def indexpage(request):
    try:
        uid = request.session['logid']
        role = Login.objects.get(id=uid)
        getstores = Login.objects.filter(Role="Store")
        if role.Role == "User":
            fetchprodata = Product.objects.filter(Login_id__in=getstores)
            print(fetchprodata)
        else:
            fetchprodata = Product.objects.filter(Login_id=role)
        getcategories = Category.objects.all()
        print('getcategories')

        context = {
            'data': fetchprodata,
            'getstores': getstores,
            'getcategories':getcategories,
        }

        return render(request, 'index.html', context)
    except:
        getstores = Login.objects.filter(Role="Store")
        getcategories = Category.objects.all()
        fetchprodata = Product.objects.all()

        context = {
            'data': fetchprodata,
            'getstores': getstores,
            'getcategories': getcategories,
        }
        return render(request, 'index.html',context)


def aboutpage(request):
    getstores = Login.objects.filter(Role="Store")
    getcategories = Category.objects.all()
    fetchprodata = Product.objects.all()

    context = {
        'data': fetchprodata,
        'getstores': getstores,
        'getcategories': getcategories,
    }
    return render(request, 'about.html', context)


def checkoutpage(request):
    uid = request.session["logid"]
    getcategories = Category.objects.all()
    print('getcategories')
    fetchcartdata = Cart.objects.filter(userid=uid, cartstatus=1)
    total_amount = fetchcartdata.aggregate(total=Sum('totalamount'))['total']
    print(total_amount)
    print(fetchcartdata)
    context = {
        'getcategories': getcategories,
        'cart': fetchcartdata,
        'finaltotal': total_amount
    }
    return render(request, 'checkout.html', context)


def contactpage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'contact.html', context)


def complainpage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        getcategories: "getcategories"
    }
    return render(request, 'complain.html', context)


def feedbackpage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        getcategories: "getcategories"
    }
    return render(request, 'feedback.html', context)


def faqspage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'faqs.html', context)


def helppage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'help.html', context)


def iconspage(request):
    return render(request, 'icons.html')


def paymentpage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'payment.html', context)


def privacypage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'privacy.html', context)


def productpage(request):
    fetchprodata = Product.objects.all()
    print(fetchprodata)
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'data': fetchprodata,
        'getcategories': getcategories
    }
    return render(request, 'product.html', context)


def productpage2(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'product2.html', context)


def singlepage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'single.html', context)


def singlepage2(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'single2.html', context)


def termspage(request):
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'getcategories': getcategories
    }
    return render(request, 'terms.html', context)


def typographypage(request):
    return render(request, 'typography.html')


def insertuserdata(request):
    uname = request.POST.get('Name')
    uemail = request.POST.get('Email')
    upassword = request.POST.get('password')
    uconpassword = request.POST.get('Confirm Password')
    uphone = request.POST.get('phoneno')
    urole = request.POST.get('Role')

    insertdata = Login(Name=uname, Email=uemail, Password=upassword, Conf_Password=uconpassword, Role=urole,
                       Phone_no=uphone, Status='Active')
    insertdata.save()
    return redirect('/')


def checklogindata(request):
    useremail = request.POST.get('Email')
    userpassword = request.POST.get('password')
    try:
        chekuser = Login.objects.get(Email=useremail, Password=userpassword)
        request.session["logid"] = chekuser.id
        request.session["logname"] = chekuser.Name
        request.session["logrole"] = chekuser.Role
        request.session["email"] = chekuser.Email
        request.session.save()
    except:
        chekuser = None

    if chekuser is not None:
        messages.error(request, "Login Successfully")
        return redirect("/")
    else:
        print("Incorrect Details")
        messages.error(request, "Invalid Name or Password!.Please try again")
    return render(request, 'index.html')


def logout(request):
    try:
        del request.session["logid"]
        del request.session["logname"]
        del request.session["logrole"]
        del request.session["email"]
        return redirect(indexpage)
    except:
        pass
    return redirect("/")

def contactuserdetail(request):
    uname = request.POST.get('name')
    # usubject = request.POST.get('subject')
    uemail = request.POST.get('email')
    uphone = request.POST.get('Phone')
    umsg = request.POST.get('message')

    contactdetail = Contact_us(Name=uname, Email_id=uemail, Phone_no=uphone, Message=umsg)
    contactdetail.save()
    return redirect('/')


def complainuserdetail(request):
    uid = request.session["logid"]
    usubject = request.POST.get('subject')
    umsg = request.POST.get('message')

    complaindetail = Complain(Login_id=Login(id=uid), Subject=usubject, Message=umsg)
    complaindetail.save()

    messages.success(request, "Response Recorded Successful !")

    return redirect('/')


def feedbackuserdetail(request):
    uid = request.session["logid"]
    urating = request.POST.get('rating')
    ucomment = request.POST.get('comment')

    feedbackdetail = Feedback(Login_id=Login(id=uid), Rating=urating, Comment=ucomment)
    feedbackdetail.save()
    messages.success(request, "Response Recorded Successful!")
    return redirect('/')


def singleproductpage(request, pid):
    uid = request.session['logid']
    role = Login.objects.get(id=uid)
    getsingledata = Product.objects.get(id=pid)
    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        'data': getsingledata,
        'getcategories': getcategories
    }
    return render(request, 'single.html', context)


def categoryviseproduct(request, id):
    fetchcat = Category.objects.all()
    catname = Category.objects.get(id=id)
    finalname = catname.Cat_name
    # catstatus = Product.objects.get(id=id)
    # finalstatus = catstatus.Product_status
    fetchprodata = Product.objects.filter(Cat_id=id)
    getcategories = Category.objects.all()
    # print(fetchcat)
    print(fetchprodata)
    context = {
        "data": fetchprodata,
        'getcategories': getcategories,
        "catdata": fetchcat,
        "catname": finalname,
        # "catstatus":finalstatus
    }
    return render(request, "categoryvise.html", context)

def storeviseproduct(request,id):
    fetchprodata = Product.objects.filter(Login_id=id)
    getcategories = Category.objects.all()
    print(getcategories)
    context = {
        "data":fetchprodata,
        'getcategories': getcategories,

    }
    return render(request,"categoryvise.html",context)






def search(request):
    query = request.GET.get("q", default="")
    products = Product.objects.filter(Product_name__icontains=query)

    matching_categories = Category.objects.filter(Cat_name__icontains=query)

    if matching_categories.exists():
        products = Product.objects.filter(Cat_id__in=matching_categories)

    getcategories = Category.objects.all()
    print('getcategories')
    context = {
        "products": products,
        "query": query,
        'getcategories': getcategories,
    }
    return render(request, "search.html", context)


def addtocart(request):
    uid = request.session["logid"]
    quantity = request.POST.get("quantity")
    prodid = request.POST.get("pid")
    proprice = request.POST.get("price")
    quantity = float(quantity)
    proprice = float(proprice)
    totalamount = proprice * quantity

    try:
        checkitemincart = Cart.objects.get(userid=uid, productid=prodid, cartstatus=1)

    except:
        checkitemincart = None

    if checkitemincart is None:
        storedata = Cart(userid=Login(id=uid), productid=Product(id=prodid), quantity=int(quantity),
                         totalamount=totalamount, cartstatus=1, orderid=0)
        storedata.save()

    else:
        checkitemincart.quantity += quantity
        checkitemincart.totalamount += totalamount
        checkitemincart.save()

    messages.success(request, "Added To Cart!!")
    return redirect("/")


def increaseitem(request, id):
    getitemdetail = Cart.objects.get(id=id)
    getitemdetail.quantity += 1
    getitemdetail.totalamount += getitemdetail.productid.Product_price
    getitemdetail.save()
    return redirect("/checkout.html")


def decreaseitem(request, id):
    getitemdetail = Cart.objects.get(id=id)
    quantity = getitemdetail.quantity

    if quantity == 1:
        getitemdetail.detail()
    else:
        getitemdetail.quantity -= 1
        getitemdetail.totalamount -= getitemdetail.productid.Product_price
        getitemdetail.save()
        return redirect("/checkout.html")


def removeitem(request, id):
    fetchitemfromcart = Cart.objects.filter(orderid=id)
    fetchitemfromcart.delete()
    fetchorderdata = Order.objects.get(id=id)
    fetchorderdata.delete()
    messages.success(request,"Order Canceled Successful")
    return redirect("/yourorders")


def dopayment(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    finaltotal = request.POST.get('finaltotal')
    print(finaltotal)
    print(name)
    print(address)
    context = {
        "name": name,
        "address": address,
        "finaltotal": finaltotal
    }
    return render(request, "payment.html", context)


def fetchorderdetails(request):
    uid = request.session["logid"]
    name = request.POST.get('username')
    address = request.POST.get('address')
    finaltotal = request.POST.get('finaltotal')
    payment = request.POST.get('paymode')
    if payment == "COD":
        paystatus = "pending"

        storedata = Order(Login_id=Login(id=uid), finaltotal=finaltotal, Payment_mode=payment, name=name,
                          address=address,
                          Pay_Status=paystatus)
        storedata.save()

        lastid = storedata.id
        print(lastid)

        fetchcartdata = Cart.objects.filter(userid=uid, cartstatus=1)

        for i in fetchcartdata:
            i.orderid = lastid
            i.cartstatus = 2
            i.save()

        messages.success(request, "Order Placed Successfully")
        return redirect(askstep)

    else:
        cardNumber = request.POST.get('number')
        cvv = request.POST.get('securitycode')
        expiryDate = request.POST.get('expiryDate')

        carddata = cardDetail.objects.first()
        number = carddata.card_number
        expdate = carddata.exp_date
        ccvv = carddata.card_cvv

        print(cardNumber  ,  "   " , number)
        print(cvv  ,  "   " , ccvv)
        print(expiryDate  ,  "   " , expdate)

        if cardNumber == number  and expiryDate == expdate and cvv == ccvv:

            paystatus = "paid"

            try:

                storedata = Order(Login_id=Login(id=uid), finaltotal=finaltotal, Payment_mode=payment, name=name, address=address,
                                  Pay_Status=paystatus)
                storedata.save()

                lastid = storedata.id
                print(lastid)

                fetchcartdata = Cart.objects.filter(userid=uid, cartstatus=1)

                for i in fetchcartdata:
                    i.orderid = lastid
                    i.cartstatus = 2
                    i.save()

                messages.success(request, "Order Placed Successfully")
                return redirect(askstep)
            except:
                pass
    messages.error(request , "Some Error Occured")
    return redirect(indexpage)

def storeadddetail(request):
    uid = request.session["logid"]
    fetchcategory = Category.objects.all()
    fetchstatus = Product.objects.all()
    context = {
        "catdata": fetchcategory,
        "catstatus": fetchstatus
    }
    return render(request, "storeadddetail.html", context)


def insertproductdata(request):
    uid = request.session["logid"]
    Cat_name = request.POST.get("catname")
    proname = request.POST.get("pname")
    proprice = request.POST.get("productPrice")
    prodesc = request.POST.get("pdesc")
    proimage = request.FILES['pimage']
    proquantity = request.POST.get("pquantity")
    prounit = request.POST.get("productunit")
    oldprice = request.POST.get("oproductPrice")
    status = request.POST.get("productstatus")

    insertdata = Product(Login_id=Login(id=uid), Cat_id=Category(Cat_name), Product_name=proname,
                         Product_price=proprice, Product_description=prodesc, Product_image=proimage,
                         Quantity=proquantity, unit=prounit, Old_Product_price=oldprice, Product_Status=status)
    insertdata.save()

    return redirect("/storeadddetail.html")


def manageproductpage(request):
    uid = request.session["logid"]
    fetchproduct = Product.objects.filter(Login_id=uid)
    print(fetchproduct)
    context = {
        'data': fetchproduct
    }
    return render(request, 'manageproduct.html', context)


def deleteproduct(request, id):
    getdata = Product.objects.get(id=id)
    getdata.delete()
    return redirect("/manageproduct.html")



def manageorders(request):
    # Retrieve the logged-in store's ID from the session
    uid = request.session["logid"]

    # Query the Product IDs added by the store
    product_ids = Product.objects.filter(Login_id=uid).values_list('id', flat=True)

    # Query the Cart model to get orders associated with the store's products
    store_orders = Cart.objects.filter(productid_id__in=product_ids, cartstatus=2)


    # Retrieve the order details and associated user details
    orders_details = []
    for order in store_orders:
        user_details = Order.objects.filter(id=order.orderid).exclude(STATUS="cancel")
        print(order)
        print(order.userid)
        order_details = {
            "order_id": order.orderid,
            "product_name": order.productid.Product_name,
            "quantity": order.quantity,
            "total_amount": order.totalamount,
            "user_name": order.userid,
            "user_phone"  : order.userid.Phone_no
            # "status":user_details.STATUS
            # Add more fields as needed
        }
        orders_details.append(order_details)

    return render(request, "manageorder.html", {"orders_details": orders_details})



def editproduct(request,id):
    getdata = Product.objects.get(id=id)

    context = {
        "data": getdata
    }
    return render(request,'editproduct.html',context)

def updateproduct(request):
    pid = request.POST.get("pid")
    pname = request.POST.get("pname")
    pdesc = request.POST.get("pdesc")
    pquantity = request.POST.get("pquantity")
    productunit = request.POST.get("productunit")
    pprice = request.POST.get("productPrice")

    try:
        pimage = request.FILES['pimage']
    except:
        getdata = Product.objects.get(id=pid)
        pimage = getdata.Product_image

    getdata = Product.objects.get(id=pid)
    getdata.Product_name = pname
    getdata.Product_description = pdesc
    getdata.Quantity = pquantity
    getdata.unit = productunit
    getdata.Product_price = pprice

    getdata.save()
    return redirect("/manageproduct.html")




def forgotpage(request):
    return render(request,'forgotpassword.html')


def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['uema' \
                                'il']
        print(username)
        try:
            user = Login.objects.get(Email=username)

        except Login.DoesNotExist:
            user = None
        # if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  # we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################

            msg = "hello here it is your new password  " + password  # this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'krushanuinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )

            # now update the password in model
            cuser = Login.objects.get(Email=username)
            cuser.Password = password
            cuser.save(update_fields=['Password'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return redirect("/")

        else:
            messages.info(request, 'This account does not exist')
    return redirect("/")

def cancelorder(request, oid):
    orders = Order.objects.filter(id=oid)
    for order in orders:
        order.STATUS = "cancel"
        order.save(update_fields=['STATUS'])

    return redirect(manageorders)


def askstep(reqeust):
    return render(reqeust, "askstep.html")