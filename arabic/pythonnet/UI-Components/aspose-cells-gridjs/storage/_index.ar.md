---
title: العمل مع تخزين GridJs
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/storage/
description: يصف هذا المقال المعالجة العامة لـ Aspose.Cells.GridJs.
keywords: تخزين ملف ، تخزين ، جريدجس ، تخزين جريدجس ، معرف جريدجس ، تنزيل ، معرف فريد ، ذاكرة التخزين المؤقت ، المحرر ، تحرير ، جدول بيانات ، إكسل
---


# العمل مع تخزين GridJs
##  عملية الملف العامة 
بعد استيراد ملف جدول بيانات ،

سيقوم GridJs بإنشاء ملف ذاكرة تخزين مؤقت مع معرّف محدد في مجلد **`Config.file_cache_directory`**،

بصيغة [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")،

سيحفظ GridJs أيضًا جميع الأشكال/الصور في ملف أرشيف مضغوط في مجلد **`Config.file_cache_directory`** لعرض الأشكال/الصور في واجهة المستخدم الخاصة في وقت لاحق.

وبعد كل عملية تحديث في واجهة المستخدم،

على سبيل المثال تعيين قيمة الخلية ، تعيين نمط الخلية، وما إلى ذلك،

سيقوم جافا سكريبت الجانب الخادمي لـ GridJs بإجراء مكالمة ajax لإجراء عملية تحديث الخلية.

في هذا العمل يحدث حفظ مرة أخرى إلى الملف المؤقت أثناء طريقة التحديث الخلية.
```python  
# update action :/GridJs2/UpdateCell
@app.route('/GridJs2/UpdateCell', methods=['POST'])
def update_cell():
    # get request param 
    p = request.form.get('p')
    uid = request.form.get('uid')

    gwb = GridJsWorkbook()

    ret = gwb.update_cell(p, uid)

    return Response(ret, content_type='text/plain; charset=utf-8')
```

### كيفية الحصول على ملف النتيجة المحدث
#### 1. معرّف محدد للملف 
تأكد من وجود توافق تعيين خريطة محددة بين الملف ومعرف اليوسيدي، 

يمكنك دائمًا الحصول على نفس معرف اليوسيدي لاسم ملف محدد، ليس من توليد عشوائي.

على سبيل المثال، ما عليك سوى استخدام اسم الملف.
```python  

...
# get json info from : /GridJs2/DetailFileJsonWithUid?filename=&uid=
@app.route('/GridJs2/DetailFileJsonWithUid', methods=['GET'])
def detail_file_json_with_uid():
    filename = request.args.get('filename')
    uid = request.args.get('uid')
    if not filename:
        return jsonify({'error': 'filename is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400
    gwb = GridJsWorkbook()
    file_path = os.path.join(FILE_DIRECTORY, filename)

    # check file
    if not os.path.isfile(file_path):
        return jsonify({'error': 'file not found:'+file_path}), 404
    try:
        sb = gwb.get_json_str_by_uid(uid, filename)
        if sb == None:
            gwb.import_excel_file(uid, file_path)
            sb = gwb.export_to_json(filename)
        response = Response(sb, status=200, mimetype='text/plain')
        response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        return response

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

```

#### 2. مزامنة مع عملية واجهة المستخدم للعميل
في الواقع، بالنسبة لبعض عمليات واجهة المستخدم الخاصة بالعميل،

على سبيل المثال:

تبديل الورقة النشطة إلى أخرى،

تغيير موقع الصورة،

تدوير/تغيير حجم الصورة، إلخ.

لن تتم تفعيل إجراء تحديث الخلية.

بالتالي، إذا كنا نريد الحصول على ملف محدث تمامًا كما يظهر واجهة المستخدم الخاصة بالعميل،

نحتاج إلى القيام بعملية دمج قبل إجراء توصية بحفظ لمزامنة تلك العمليات واجهة المستخدم الخاصة بالعميل.
```javascript
//in the js
  function save() {
            if (!xs.buffer.isFinish()) {
              alert('updating is inprogress,please try later');
                return;
            }
            let datas = xs.datas;
            delete datas.history;
            delete datas.search;
            delete datas.images;
            delete datas.shapes;

        var jsondata = {
          sheetname: xs.sheet.data.name,
          actrow: xs.sheet.data.selector.ri,
          actcol: xs.sheet.data.selector.ci,
          datas: xs.getUpdateDatas(),
        };

        const data = {
          p: JSON.stringify(jsondata),
          uid: uniqueid,
        };
		....
		//go on to do ajax post to trigger controller action
```
```python
# in download route action 
        gwb = new GridJsWorkbook();
        gwb.merge_excel_file_from_json(uid, p)
        # after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
        gwb.save_to_cache_with_file_name(uid, filename, None);
```         

#### 3. الحصول على الملف من الذاكرة المؤقتة
على سبيل المثال: في إجراء الحصول_الملف، يمكنك فقط الحصول عليه من دليل الذاكرة المؤقتة بواسطة معرّف اليوسيدي.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

للمزيد من المعلومات التفصيلية، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
