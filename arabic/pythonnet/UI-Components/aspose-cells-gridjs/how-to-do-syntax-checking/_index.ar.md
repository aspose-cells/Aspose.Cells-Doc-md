---
title: التحقق من بناء الجمل وتصحيح الإملاء لـ GridJs  
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: تصف هذه المقالة كيفية إضافة التحقق من بناء الجمل وتصحيح الإملاء لـ GridJs.
keywords: GridJs،التحقق من بناء الجمل،تصحيح الإملاء،بناء الجمل،إملاء،فحص القواعد،تدقيق النحو
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
---


# لتنفيذ فحص الصياغة وتصحيح الإملاء على إدخال المستخدم ، الخطوات هي
## تعيين خيارات التحميل.
على سبيل المثال:
```javascript
 const option = {
     ...
     //set showCheckSyntaxButton to true
    showCheckSyntaxButton:true,
    //set checkSyntax to true
    checkSyntax:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## تعيين عنوان URL للإجراء لفحص الصياغة وتصحيح الإملاء.
على سبيل المثال:
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
بعد أن يدخل المستخدم محتوى نصيًا في خلية ، سيتم تفعيل عملية فحص الصياغة تلقائيًا بواسطة تطبيق جدول البيانات 

## تنفيذ فحص الصياغة وتصحيح الإملاء في جانب الخادم.
على سبيل المثال:
```python
# The logic for invoking syntax checking here can be implemented through a third-party library or custom logic.
def correct_syntax(text, locale):  
# replace your logic  here     
    return text  

@app.route('/GridJs2/CheckSyntax', methods=['POST'])  
def check_syntax():  
    text = request.form.get('v')  
    locale = request.form.get('locale')  

    if not text:  
        return jsonify({  
            'Success': False,  
            'v': ''  
        }), 200  

    corrected_content = correct_syntax(text, locale)  

    return jsonify({  
        'Success': True,  
        'v': corrected_content  
    }), 200  
```





