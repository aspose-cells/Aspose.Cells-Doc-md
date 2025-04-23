---
title: كيفية عمل التحميل الكسول في GridJs  
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: تصفيرح هذه المقالة كيفية تنفيذ التحميل الكسول في GridJs.
keywords: GridJs،التحميل الكسول،التحميل عند الطلب،
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

---

## حول التحميل الكسول 
عند التعامل مع ملف جدول بيانات يحتوي على العديد من أوراق العمل، يمكننا تحسين عملية التحميل عن طريق تحميل ورقة العمل النشطة فقط في البداية.

هذه الاستراتيجية تضمن أن استجابة JSON من جانب السيرفر تشمل البيانات ذات الصلة بورقة العمل المختارة فقط في البداية.  

نتيجة لذلك، يقل حركة المرور الأولية بشكل كبير، مما يعزز تجربة المستخدم عن طريق تقليل أوقات التحميل.  

علاوة على ذلك، صُمم GridJs للاستجابة بشكل ديناميكي لتفاعلات المستخدم. تحديدًا، عندما ينقر المستخدم على ورقة عمل مختلفة،

يقوم GridJs بشكل ذكي بإرسال طلب إلى الخادم للحصول على البيانات المتعلقة بتلك الورقة فقط.  

هذه الآلية للتحميل عند الطلب لا تقلل فقط من نقل البيانات غير الضروري، بل تضمن أيضًا أن يكون لدى المستخدم دائمًا أحدث المعلومات الخاصة بورقة العمل التي يعمل عليها حاليًا.  

باتباع هذا النهج، لا نعمل فقط على تحسين وقت التحميل الأولي، بل نحافظ أيضًا على تطبيق سريع وفعال يتكيف جيدًا مع زيادة عدد أوراق العمل في ملف الجدول.

# لتنفيذ التحميل الكسول في GridJs، الخطوات هي
## ضبط خيار التكوين للتحميل الكسول.
على سبيل المثال:
```python 
       Config.set_lazy_loading(True)
```
## ضبط عنوان URL للإجراء للتحميل الكسول.
على سبيل المثال:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
بعد نقر المستخدم على ورقة عمل أخرى غير النشطة، يتم تشغيل عملية استعلام البيانات تلقائيًا بواسطة تطبيق الجدول الإلكتروني. 

## تنفيذ إجراء التحميل الكسول في وحدة التحكم على جانب الخادم.
على سبيل المثال:
```python
@app.route('/GridJs2/LazyLoading', methods=['POST'])
def lazy_loading():
    sheet_name = request.form.get('name', '')
    uid = request.form.get('uid', '')
    if not sheet_name:
        return jsonify({'error': 'sheet_name is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400

    wbj = GridJsWorkbook()
    try:

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
             wbj.lazy_loading_stream(gzip_stream,uid, sheet_name)


        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)
```





