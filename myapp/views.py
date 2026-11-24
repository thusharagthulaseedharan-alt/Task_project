from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class Bmiview(View):
    def post(self,request):
        data=json.loads(request.body)
        h=data.get("height")
        w=data.get("weight")
        
        #convert height from cm to m
        height=h/100
        
    #calculate bmi
        bmi=w/(height**2)
        
        result={
            "Height":data.get('height'),
            "Weight":w,
            "BMI":round(bmi , 2)
        }
        return JsonResponse(result)
    
    
@method_decorator(csrf_exempt,name='dispatch')
class Ageview(View):
    def post(self,request):
        data=json.loads(request.body)
        birth=data.get("birthyear")
        current=data.get("currentyear")
        
        
        result={
            "Birthyear":birth,
            "Current_year":current,
            "Age":current-birth
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Simpleinterest(View):
    def post(self,request):
        data=json.loads(request.body)
        p=data.get("principal")
        r=data.get("rate")
        t=data.get("time")
        
        result={
            "Principal":p,
            "Rate":r,
            "Time":t,
            "simple":(p*r*t)/100
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Electricityview(View):
    def post(self,request):
        data=json.loads(request.body)
        u=data.get("unit")
        r=data.get("rate")
        
        result={
            "Unit":u,
            "Rate":r,
            "Bill":u * r
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Percentage(View):
    def post(self,request):
        data=json.loads(request.body)
        ob=data.get("obtained_mark")
        to=data.get("total_mark")
        result={
            "Percentage":(ob/to)*100
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Discountview(View):
    def post(self,request):
        data=json.loads(request.body)
        p=data.get("price")
        d=data.get("discount_percentage")
        discount_amount=(p*d)/100
        final_price=p-discount_amount
        
        result={
            "Price":p,
            "Discount_percentage":d,
            "Discount_amount":discount_amount,
            "Final_price":final_price
            
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Profitview(View):
    def post(self,request):
        data=json.loads(request.body)
        c=data.get("cost_price")
        s=data.get("selling_price")
        profit=s-c
        result={
            "Cost_price":c,
            "Selling_price":c,
            "Profit":profit
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Salaryview(View):
    def post(self,request):
        data=json.loads(request.body)
        basic=data.get("basic_salary")
        bonus=data.get("bonus")
        d=data.get("deduction")
        net= basic + bonus - d
        result={
            "Basic_salary":basic,
            "Bonus":bonus,
            "Deduction":d,
            "Net_salary":net
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Timeview(View):
    def post(self,request):
        data=json.loads(request.body)
        h=data.get("hour")
        minutes=h*60
        second=h*3600
        result={
            "Hours":h,
            "Minutes":minutes,
            "Seconds":second
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Fuelcostview(View):
    def post(self,request):
        data=json.loads(request.body)
        dis=data.get("distance")
        mil=data.get("mileage")
        fuel_pri=data.get("fuel_price")
        fuel_req=dis/mil
        total=fuel_req*fuel_pri
        result={
            "Distance":dis,
            "Mileage":mil,
            "Fuel_price":fuel_pri,
            "Fuel_required":fuel_req,
            "Total_cost":total
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Productview(View):
    def post(self,request):
        data=json.loads(request.body)
        cp=data.get("cost_price")
        sp=data.get("selling_price")
        qua=data.get("quantity")
        total_cost=cp*qua
        total_sales=sp*qua
        profit=total_sales-total_cost
        result={
            "Cost_price":cp,
            "Selling_price":cp,
            "Quantity":qua,
            "Total_cost":total_cost,
            "Total_sales":total_sales,
            "Profit":profit
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Worksalary(View):
    def post(self,request):
        data=json.loads(request.body)
        hourworked=data.get("hours_worked")
        regularhour=data.get("regular_hour")
        hourlyrate=data.get("hourly_rate")
        overtimerate=data.get("overtime")
        regular_pay=regularhour*hourlyrate
        overtime_hours=hourworked - regularhour
        overtime_pay=overtime_hours*overtimerate
        total_salary=regular_pay+overtime_pay
        result={
            "Hours_worked":hourworked,
            "Regular_hours":regularhour,
            "Hourly_rate":hourlyrate,
            "Overtime_rate":overtimerate,
            "Regular_pay":regular_pay,
            "Overtime_hour":overtime_hours,
            "Overtime_pay":overtime_pay,
            "Total_salary":total_salary
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class Agedetailsview(View):
    def post(self,request):
        data=json.loads(request.body)
        a=data.get("age")
        months=a*12
        weeks=a*52
        days=a*365
        result={
            "Age":a,
            "Months":months,
            "Weeks":weeks,
            "Days":days
        }
        return JsonResponse(result)
        
        
        
        