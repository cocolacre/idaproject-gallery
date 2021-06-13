from PIL import Image as Im

def resize(src,dst, w=None, h=None):
    """
    Требование:
    'Можно задать только ширину, только высоту, или оба значения. 
    Пропорции изображения должны  сохраняться.'
    
    Замечание:
        TODO:
            ОБЯЗАТЕЛЬНО описать опечатки в ТЗ.
        Q: Что делать, если пользователь задал оба значения,
           пропорция между которыми не соответствует оригиналу?
            (см. 40 строку)
        
    Returns: (result, msg)
        If <result> is True, then operation was successful
        and <msg> contains new image file path.
        If not, <msg> contains error\exception message.
    
    ...(quick dirty Sunday's late night hack)
    """
    img = Im.open(src)
    img_w, img_h = img.size[0],img.size[1]
    if not w and not h:
        return (False, "Error: empty W,H values were given.")
        
    if w and not h: #only w is given
        w_ratio = img_w*1.0/w
        new_w = w
        new_h = int(img_h / w_ratio)
        
    elif h and not w:
        h_ratio = img_h*1.0/h
        new_h = h
        new_w = int(img_w / h_ratio)


    #Если заданы оба значения, но пропорция между новой шириной и высотой
    # не соответствует пропорции оригинала
    #(с погрешностью, например, в 1% от пропорции оригинала),
    # - выдать ошибку.
    elif w and h:
        new_w = w
        new_h = h
        original_ratio = 1.0*img_w/float(img_h)
        print("original_ratio: " + str(original_ratio))
        new_ratio = float(new_w)/float(new_h)
        print("new_ratio: " + str(new_ratio))
        print("abs((original_ratio - new_ratio)/original_ratio):")
        print(abs((original_ratio - new_ratio)/original_ratio))
        if abs((original_ratio - new_ratio)/original_ratio) > 0.01:
            return (False, "Wrong ratio given. Either set just one value or set correct ratio manually.\n(And I'm not going to help you! Use calculator or something.)")
    try:
        new_img = img.resize((new_w,new_h), resample=Im.BILINEAR)
        new_img.save(dst)
        return (True, dst)
    except Exception as _e:
        print(str(_e))
        return (False, str(_e))

def resize2(src=None,img_w=500,img_h=500, w=None, h=None):
	#img = Im.open(src)
    #img_w, img_h = img.size[0],img.size[1]
    #img_w, img_h = 500,500
    
    w_ratio = img_w*1.0/w
    new_w = w
    new_h = int(img_h / w_ratio)
    print("Old w,h: %s %s"%(img_w,img_h))
    print("New w,h: %s %s"%(new_w,new_h))

#resize2(w=300)
#resize2(w=250)
#resize2(h=250)

if __name__ == "__main__":
    src = "lenna.png"
    dst = "lenna_200x200.png"
    dst2 = "lenna_250x200.png"
    dst3 = "lenna_201x200.png"
    dst4 = "lenna4.png"
    dst5 = "lenna_204x200.png"
    res, msg = resize(src,dst,w=200,h=200)
    print(res, "\n", msg,"\n"*3)
    res, msg = resize(src,dst2,w=250,h=200) #NOT OK
    print(res, "\n", msg,"\n"*3)
    res, msg = resize(src,dst3,w=201,h=200) #OK
    print(res, "\n", msg,"\n"*3)
    res, msg = resize(src,dst4) #OK
    print(res, "\n", msg,"\n"*3)
    res, msg = resize(src,dst5,w=205,h=200)
    print(res, "\n", msg,"\n"*3)