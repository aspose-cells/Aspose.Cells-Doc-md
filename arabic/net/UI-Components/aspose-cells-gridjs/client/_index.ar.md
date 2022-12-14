---
title: العمل مع جانب عميل GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/client/
---
# العمل مع جانب عميل GridJs
قمنا بتطوير عميل GridJs على أساس[x- جدول](https://github.com/myliang/x-spreadsheet).

## الخطوات الرئيسية هي:

- إنشاء مثيل x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
```
- تحميل بيانات json
```javascript
xs.loadData(jsondata.data)
```
- تعيين ورقة نشطة
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- تعيين خلية نشطة
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

على سبيل المثال ، يقوم الكود أدناه بتهيئة كائن x_spreadsheet.
```javascript
 xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
            showContextmenu: true
        }).loadData(sheets)
```
 // معلمات الخيارات:
 updateMode: حاليًا نحن ندعم فقط "الخادم"
 updateUrl: اضبط عنوان url من جانب الخادم لإجراء التحديث بناءً على json
 الوضع: القراءة تعني للقراءة فقط ورقة الانتشار / التحرير يعني أنه يمكننا تحرير ورقة الانتشار
 showToolbar: يعني ما إذا كنت تريد إظهار شريط الأدوات
 showFileName: إظهار اسم الملف
 محلي: دعم لغات متعددة للقوائم ، يمكن أن تكون اللغة: en ، cn ، es ، pt ، de ، ru ، nl للغة الإنجليزية ، الصينية ، الإسبانية ، البرتغالية ، ألمانيا ، الروسية ، الهولندية
 showContextmenu: يعني ما إذا كنت تريد إظهار قائمة السياق عند النقر بزر الماوس الأيمن على خلية
## 

___
## واجهات برمجة تطبيقات أخرى مفيدة
- تقديم العرض
```javascript
xs.reRender()
```
- الحصول على الصورة / الشكل المختار� إذا لم يتم تحديد أي شيء سيعود فارغًا
```javascript
xs.sheet.selector.getObj()
```

- احصل على كائن الخلية
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- احصل على نمط الخلية
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- عيّن قيمة الخلية
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- الحصول على / تعيين نطاق الخلايا المحدد
```javascript
xs.sheet.data.selector.range
```
- عيّن قيمة الخلية للخلية أو منطقة الخلية المحددة
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- عيّن النمط للخلية أو منطقة الخلية المحددة
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- دمج منطقة الخلية المحددة
```javascript
xs.sheet.data.merge()
```

- قم بإلغاء دمج منطقة الخلية المحددة
```javascript
xs.sheet.data.unmerge()
```
-  احذف الخلية المحددة
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- اضبط جزء التجميد
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  أدخل صفًا أو أعمدة في الخلية المحددة
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  احذف صفًا أو أعمدة في الخلية المحددة
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- اضبط عرض العمود
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  احصل على عرض العمود
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- اضبط ارتفاع الصف
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  احصل على ارتفاع الصف
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- الحصول على / تعيين اتجاه العرض
```javascript
xs.sheet.data.displayRight2Left
```



للحصول على معلومات تفصيلية ، يمكنك التحقق من المثال هنا
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
