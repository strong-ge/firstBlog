# coding:utf-8 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
import simplejson,os,time
from django.conf import settings
import yanzhengma
from blog.models import IP,Dream
from django.core.mail import send_mail

def createdream(request):
    code_img = yanzhengma.create_validate_code()
    code_img[0].save("./blog/static/css/validate.png", "PNG")
    return render_to_response('createdream.html',locals())

def test(request):
    '''
    获得文件上传请求
    '''
    file= request.FILES['file']
    print(file)
    result,new_name=profile_upload(file)
    if result:
        json={'flag':'ok','pic_name':new_name}
    else:
        json={'flag':'no'}
    return HttpResponse(simplejson.dumps(json,ensure_ascii = False))
def profile_upload(file):  
    '''文件上传函数'''  
    if file:  
        path=settings.MEDIA_ROOT 
        suffix=(file.name).split()[-1]
        file_name=str(int(time.time()))+suffix
        path_file=os.path.join(path,file_name)
        print(path_file)
        fp = open(path_file, 'wb')  
        for content in file.chunks():   
            fp.write(content)  
        fp.close()  
        return (True,file_name) #change  
    return (False,file_name)   #change

def getVCode(request):
    '''
    点击换一张时生成新的验证码
    '''
    code_img = yanzhengma.create_validate_code()
    code_img[0].save("./blog/static/css/validate.png", "PNG")
    image_data = open("./blog/static/css/validate.png","rb").read()
    response = HttpResponse(image_data, content_type="image/png")
    #将验证码存储进session
    request.session['vcode'] = code_img[1].lower()
    return response

def verificeVCode(request):
    '''
    验证码校验 Jquery validate
    '''
    yourVCode=request.POST.get('captcha')
    if(yourVCode.lower()==request.session.get('vcode',default=None)):
        return HttpResponse("true")
    else:
        return HttpResponse("false")

def saveDream(request):
    '''
    保存dream信息
    '''
    username=request.POST.get('username')
    email=request.POST.get('email')
    content=request.POST.get('want')
    pic_name=request.POST.get('pic_name')
    try:
    	ip_address=request.META['HTTP_X_FORWARDED_FOR']
    	ip_address=ip_address.split(",")[0]
    except Exception, e:
    	try:
    		ip_address = request.META['REMOTE_ADDR']
    	except Exception, e:
    		ip_address=""
    ip=IP.objects.create(ip_address=ip_address)
    dream=Dream()
    dream.name=username
    dream.email=email
    dream.content=content
    dream.pic_name=pic_name
    dream.ip=ip
    dream.save()
    try:
        send_mail('强哥提醒您','您在strong-ge.com上留下了想说的话，内容为:', settings.DEFAULT_FROM_EMAIL,[str(email)], fail_silently=False)
    except Exception, e:
        raise e
    return HttpResponseRedirect('fly_success')

def fly_success(request):
    return render_to_response('fly_success.html')

def followdream(request):
    try:
        ip_address=request.META['HTTP_X_FORWARDED_FOR']
        ip_address=ip_address.split(",")[0]
    except Exception, e:
        try:
            ip_address = request.META['REMOTE_ADDR']
        except Exception, e:
            ip_address=""
    ip=ip_address
    dreams=Dream.objects.order_by('-create_time')[:10]
    return render_to_response('followdream.html',locals())

def support_it(request):
    dream_id=request.POST.get('dream_id')
    ip=request.POST.get('ip')
    old_love_num=request.POST.get('old_love_num')
    is_exist=IP.objects.filter(dream_id=dream_id,ip_address=ip)
    #在ip表查询是否ip与id对应上的记录，若存在则删除记录;若不存在，则添加记录
    status=0
    if is_exist:
        status=1
    if status==0:
        #insert into IP tabel
        ip=IP.objects.create(dream_id=dream_id,ip_address=ip)
        #update love_num
        Dream.objects.filter(id=dream_id).update(love_num=(int(old_love_num)+1))
    json={'status':status}
    return HttpResponse(simplejson.dumps(json,ensure_ascii = False))

def getIpAddress(request):
    try:
        ip_address=request.META['HTTP_X_FORWARDED_FOR']
        ip_address=ip_address.split(",")[0]
    except Exception, e:
        try:
            ip_address = request.META['REMOTE_ADDR']
        except Exception, e:
            ip_address=""
    return ip_address
