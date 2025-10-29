---
title: العمل مع GridJs الجانب العميل
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/client/
keywords: GridJs، مخصص، شعار، إعدادات، API، gridjs، بايثون، تحرير، جدول بيانات، عرض، عارض، محرر، إكسل، واجهة برمجة تطبيقات JS، API للعميل
description: يقدم هذا المقال واجهات برمجة تطبيقات العميل في GridJs.
aliases:
  - /python-net/aspose-cells-gridjs/how-to-use-gridjs-client-api/
  - /python-net/aspose-cells-gridjs/work-with-client-api/
  - /python-net/aspose-cells-gridjs/use-js-api/
  - /python-net/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /python-net/aspose-cells-gridjs/client-api/
  - /python-net/aspose-cells-gridjs/js-api/
  - /python-net/aspose-cells-gridjs/javascript-api/
---

# العمل مع GridJs الجانب العميل
قمنا بتطوير GridJs الجانب العميل بناءً على [x-spreadsheet](https://github.com/myliang/x-spreadsheet).

##  الخطوات الرئيسية هي:

- إنشاء مثيل x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
    // the parameters are:
    id:the html node id ,for example :'#gridjs-demo' for the html  <div id="gridjs-demo"></div>
    options: the load options


for example the below code init a gridjs_spreadsheet object.
	xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
			showContextmenu: true
			})
```
المعاملات لخيارات التحميل:

| المعامل | الوصف | القيمة الافتراضية | اختياري |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | هل تسمح بتحديد النص داخل مربعات النص عند وضع القراءة.<br>القيمة الافتراضية هي خطأ. | `false` | نعم |
| `checkSyntax` | هل تقوم بفحص النحو والتصحيح الإملائي لمدخلات المستخدم لنص المحتوى.<br>يعمل مع setSyntaxCheckUrl.<br>القيمة الافتراضية هي خطأ. | `false` | نعم |
| `loadingGif` | عنوان URL للصورة المتحركة عند تحميل الصور/الأشكال.<br>القيمة الافتراضية هي content/img/updating.gif. | `content/img/updating.gif` | نعم |
| `local` | تعيين معلومات التوطين للقوائم وأشرطة الأدوات، مع دعمMultiple اللغات.<br>القيم الممكنة تشمل:<br>- `en، zh، es، pt، de، ru، nl` (للإنجليزية، الصينية، الإسبانية، البرتغالية، الألمانية، الروسية، الهولندية)<br>- `ar، fr، id، it، ja` (للعربية، الفرنسية، الإندونيسية، الإيطالية، اليابانية)<br>- `ko، th، tr، vi، cht` (لل韩، التايلاندية، التركية، الفيتنامية، الصينية التقليدية) | `en` | نعم |
| `mode` | يمكن أن يكون `read` أو `edit`؛ `read` تعني ورقة عمل للقراءة فقط؛ `edit` تعني أن ورقة العمل يمكن تحريرها. | لا يوجد | لا |
| `isCollaborative` | هل يدعم وضع التعاون . | `false` | نعم |
| `searchHighlightColor` | لون خلفية التحديد لمصطلح البحث.<br>يجب أن يتضمن اللون قناة ألفا للشفافية. | `#dbe71338` | نعم |
| `showCheckSyntaxButton` | هل تظهر أزرار فحص النحو والتصحيح الإملائي في شريط الأدوات.<br>القيمة الافتراضية هي خطأ. | `false` | نعم |
| `showContextmenu` | هل يظهر قائمة السياق عند النقر بزر الماوس الأيمن على خلية.<br>القيمة الافتراضية هي صحيح. | `true` | نعم |
| `showFileName` | هل يظهر اسم الملف. | `true` | نعم |
| `showFormulaExplain` | ما إذا كنت تريد عرض تفسيرات الصيغة المطبقة على هذه الخلية عند تحريك الماوس فوقها.<br>يعمل بالتزامن مع setFormulaExplainUrl.<br>القيمة الافتراضية هي false. | `false` | نعم |
| `showFormulaTip` | ما إذا كنت تريد عرض الصيغة الموجودة المطبقة على هذه الخلية عند تحريك الماوس فوقها.<br>القيمة الافتراضية هي false. | `false` | نعم |
| `showNonEditableSymbolInCell` | ما إذا كنت تريد عرض رمز غير قابل للتحرير على جانب العميل في الخلية.<br>إذا تم تعيينه إلى true، بعد النقر على خيار القائمة السياقية اليمنى "تعطيل التحرير"، ستظهر المنطقة المحددة التي تم تعطيلها رمزًا.<br>القيمة الافتراضية هي false. | `false` | نعم |
| `showToolbar` | ما إذا كنت تريد عرض شريط الأدوات. | `true` | نعم |
| `updateMode` | يدعم حاليا فقط `الخادم`. | `server` | لا |
| `updateUrl` | تعيين عنوان URL الخاص بالخادم لإجراءات التحديث استنادًا إلى JSON. | لا شيء | لا |
| `view` | تعيين حجم العرض للورقة، على سبيل المثال، `{width: () => 1000, height: ()=> 500}`. | `{width: () => عرض النافذة الحالية للمستعرض، height: () => ارتفاع النافذة الحالية للمستعرض}` | نعم |
| `token` | تعيين رمز المصادقة. عندما يكون الرمز غير فارغ، سيتم إضافة رأس `Authorization: Bearer {token}` تلقائيًا إلى رؤوس الطلب. يمكنك استخدام `xs.refreshToken(token)` لتعيين رمز جديد. | لا شيء | نعم | 
| `showBottombarStats` | هل عرض إحصائيات الشريط السفلي.<br>القيمة الافتراضية هي true. | `true` | نعم |   
| `showRowAppenderToolbar` | هل عرض شريط أدوات إضافة الصفوف بالجملة.<br>القيمة الافتراضية هي true. | `true` | نعم |   

- تحميل بيانات json
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- تعيين ورقة نشطة حسب اسم الورقة
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
- تعيين ورقة نشطة حسب الهوية
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

- تعيين خلية نشطة
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

- تفعيل لعدة مثيلات 
```javascript
xs.setActiveForMultipleInstance(isacitve);
// the parameters are:
	isacitve: whether need to do edit operation at this xs instanse 
// when there are more than one GridJs instances in one page, we need to call this method.
// we only support do edit operation for one instances at a page.
// for example,if we have two instances: xs1 and xs2 in one html page.
// if we need to keep edit operation in xs1,
// we shall call:
xs1.setActiveForMultipleInstance(true);
xs2.setActiveForMultipleInstance(false);

// if we need not do any edit operation for both,
// we shall call:
xs1.setActiveForMultipleInstance(false);
xs2.setActiveForMultipleInstance(false);

```
- تعيين تنبيه مخصص
```javascript
xs.customToast(customToastFunction);
// the parameter is:
	customToastFunction: user defined function to toast message,it shall have three parameters :title, content,callback
	if set to null,it will use the default build-in toast.

    for example: 
            function myCustomToast(title, content, callback) {
	    //.....
	    }
            xs.customToast(myCustomToast);
```

- تعيين معلومات لشكل/عمليات الصور لإجراءات الجانب الخادم
```javascript
xs.setImageInfo(imageGetActionUrl, imageAddByUploadActionUrl, imageAddByUrlActionUrl, imageCopyActionUrl, zindex, loadingGif);
// the parameters are:
	imageGetActionUrl: the get image action URL in the server side controller
	imageAddByUploadActionUrl: the upload image action  URL in the server side controller
	imageAddByUrlActionUrl: the add image from URL action  URL in the server side controller
	imageCopyActionUrl: the copy image action  URL in the server side controller
	zindex: the minimum zindex of the image in the canvas
	loadingGif (optional): the loading gif url when loading the image/shape .it is optional,the default value is:content/img/updating.gif
    for example: 
            const imageurl = "/GridJs2/imageurl";
            const imageuploadurl1 = "/GridJs2/AddImage";
            const imageuploadurl2 = "/GridJs2/AddImageByURL";
            const imagecopyurl = "/GridJs2/CopyImage";  
	    const basiczorder = 5678;
    xs.setImageInfo(imageurl, imageuploadurl1, imageuploadurl2, imagecopyurl, basiczorder);
```

- تعيين معلومات لعملية التنزيل لإجراءات الجانب الخادم
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- تعيين معلومات لعملية الكائن الـ OLE لإجراءات الجانب الخادم
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
- تعيين معلومات للتحقق من الصيغة وتصحيح الأخطاء الإملائية لعملية على جانب الخادم
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

- تعيين معلومات لشرح الصيغة لعملية على جانب الخادم
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## واجهات برمجة التطبيقات الأخرى المفيدة
- عرض العرض
```javascript
xs.reRender()
```

-  الحصول على معرف الورقة النشطة
```javascript
xs.getActiveSheet()
```

-  إضافة ورقة عمل جديدة
```javascript
xs.addSheet(name,isactive,tabcolor,fontcolor)
// the parameters are:
	name:the sheet name
	isactive:whether set this sheet as active sheet
	tabcolor:the background color for the sheet in the tab bottom menu
	fontcolor:the font color for the sheet name in the tab bottom menu
   for example:
    xs.addSheet('hello',true,'#12ee5b','#2c5d3b')
```
-  تعديل اسم الورقة
```javascript
xs.modifySheetName(oldName,newName)
// the parameters are:
	oldName:the sheet name
	newName:the new desired name
   for example:
     xs.modifySheetName('Sheet1','student');
```
-  حذف الورقة
```javascript
xs.deleteSheet(name)
// the parameters is:
	name:the sheet name
   for example:
        xs.deleteSheet('Sheet1');

```

- تعيين مستوى التكبير
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

- تعيين اسم الملف 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```
-   إعداد وظيفة الاتصال قبل الحفظ 
```javascript
xs.setBeforeSaveFunction(func)
// the parameters is:
	func:This function is called before the save action. If it returns true, the save will proceed; otherwise, the save will not proceed.
   for example:
	xs.setBeforeSaveFunction(()=>{console.log('hello before save');return true;});
```

- وظيفة الارتباط لميزة إرسال البريد الإلكتروني.
```javascript
xs.setEmailSendCallFunction(callback)
// the parameters is:
	callback: the callback function to handle email sending, receives a mailObj parameter
		callback: function(mailObj) {
			// mailObj properties:
			// mailObj.receiver: the email address of the receiver, e.g., 'example@gmail.com'
			// mailObj.type: the format of the file to be sent, can be 'html', 'xlsx', or 'pdf'
		}
```

-  ما إذا كان يتعين تمكين حدث مفتاح النافذة لـ GridJs
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

-  إلغاء تشبيك جميع الأحداث المرتبطة بـ GridJs، بما في ذلك حدث مفتاح النافذة وحدث تغيير حجم النافذة.
```javascript
xs.destroy()
```

-  إعداد إعدادات التعاون في وضع التعاون، تأكد من تعيين إعدادات التعاون قبل تعيين المعرف الفريد  
```javascript
xs.setCollaborativeSetting(url,wsendpoint,wsapp,wsuser,wstopic)
    //the parameters are:
         url: the basic action URL in the server side controller to get history messages ,the default is '/GridJs2/msg'
	 wsendpoint: the websocket endpoint in the server side , the default is '/ws'
	 wsapp: the websocket destinations prefixed with "/app", the default is '/app/opr'
	 wsuser: the websocket for user-specific queues prefixed with "/usr", the default is '/user/queue'
	 wstopic: the websocket destinations prefixed with "/topic", the default is '/topic/opr'


```

-  تعيين عامل تصفية مرئي للصورة/الشكل
```javascript
xs.setVisibleFilter((sheet,s) =>{})
    //  to set a function which return true(for visible) or false(for invisible) for the visible filter with the below parameters :
	sheet:the sheet instance
	s:the image or shape instance
    for example: 
	//this will make visible for image/shape in sheet with name 'Sheet3' and 'Sheet1' except for the 'Rectangle' type
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet3'||sheet.data.name==='Sheet1') return s.type!=='Rectangle';  return false; })
	//this will make visible for image/shape in sheet with name  'Sheet1' 
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet1') return true;  return false; })
	//this will make invisible for image/shape in all sheets 
		xs.setVisibleFilter((sheet,s) => {  return false; })
	//if all the image/shape is already loaded and you want to change the visible filter at runtime,you can call the below code to trigger a reload for image/shape
		xs.reRender()
```

-  الحصول على الصورة/الشكل المحدد، إذا لم يتم تحديد أي شيء سيتم إرجاع قيمة فارغة
```javascript
xs.sheet.selector.getObj()
```
- عرض أو إخفاء عنصر HTML في موضع خلية معين
```javascript
xs.sheet.showHtmlAtCell(isShow, html, ri, ci, deltaX, deltaY)

    //the parameters are:
      isShow: Boolean value indicating whether to show or hide the HTML content.
      html: The HTML string to be displayed.
      ri: Row index of the target cell.
      ci: Column index of the target cell.
      deltaX: (Optional) Relative X-position adjustment from the top-left corner of the cell.
      deltaY: (Optional) Relative Y-position adjustment from the top-left corner of the cell.

    for example: 
    // Show HTML at cell A1
    xs.sheet.showHtmlAtCell(true, "<span>html span</span><input length='30' id='myinput'>test</input>", 0, 0);

    // Hide the HTML node
    xs.sheet.showHtmlAtCell(false);

    // Note: When an HTML node is shown, the default GridJS event handling is disabled to allow interaction with the HTML content.
    // This means you cannot select any cells or perform edit operations until the HTML node is hidden.
```

- تعيين الحالة القابلة للاختيار للصورة/الشكل 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```


-  إدراج صفوف
```javascript
xs.sheet.insertRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be inserted
```
-  إدراج أعمدة 
```javascript
xs.sheet.insertColumns(start, n)
    // the parameters are:
	start: start column id
	n:how many columns will be inserted
```
-  حذف الصفوف 
```javascript
xs.sheet.deleteRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be deleted
```
-  حذف الأعمدة 
```javascript
xs.sheet.deleteColumns(start, n)
    // the parameters are:
	start: start column id 
	n:how many columns will be deleted
```
-  تحديد لوحة التجميد
```javascript
xs.sheet.freeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- إلغاء تجميد القسم
```javascript
xs.sheet.freeze(0,0)
```

- تحديد النطاق القابل للتحرير / القراءة فقط
```javascript
xs.sheet.setEditableRange(range,isenable)
    // the parameters are:
	range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	isenable:when set to true,the range is editable.other wise,the range is readonly.
```

- إخفاء الصفوف 
```javascript
xs.sheet.hideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- إظهار الصفوف المخفية
```javascript
xs.sheet.unhideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- إخفاء الأعمدة 
```javascript
xs.sheet.hideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```

- إظهار الأعمدة المخفية
```javascript
xs.sheet.unhideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```


-  تعيين الارتفاع للصف
```javascript
xs.sheet.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
-  تعيين الارتفاع للصفوف
```javascript
xs.sheet.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

-  تعيين الارتفاع لكل الصفوف
```javascript
xs.sheet.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```

-  تعيين العرض للعمود
```javascript
xs.sheet.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
-  تعيين العرض للأعمدة
```javascript
xs.sheet.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

-  تعيين العرض لجميع الأعمدة
```javascript
xs.sheet.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

- تعيين التعليق على الخلية
```javascript
xs.sheet.setComment(ri,ci,author,note)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
	author:the author for the comment
	note:the content for the comment
```

- إزالة التعليق من الخلية
```javascript
xs.sheet.removeComment(ri,ci)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
```


-  الحصول على كائن الخلية
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  الحصول على نمط الخلية
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  تعيين قيمة الخلية
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

-  الحصول/تعيين نطاق الخلية المحدد
```javascript
xs.sheet.data.selector.range
```
-  تعيين قيمة الخلية للخلية المحددة أو منطقة الخلية
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  تعيين النمط للخلية المحددة أو منطقة الخلية
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- تعيين نمط لمنطقة الخلايا المطلوبة
```javascript
xs.sheet.data.setRangeAttr(range,attributename,value)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
   for example:
        xs.sheet.data.setRangeAttr({sri:0,sci:0,eri:2,eci:2},'bgcolor','#11ee2a');
```


-  دمج منطقة الخلية المحددة
```javascript
xs.sheet.data.merge()
```

-  إلغاء دمج منطقة الخلية المحددة
```javascript
xs.sheet.data.unmerge()
```
- حذف محتوى الخلية أو مسح النمط في الخلية المحددة  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```

- حذف محتوى الخلية أو مسح النمط في المنطقة المطلوبة للخلية
```javascript
xs.sheet.data.deleteRange(range,type)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```



-  الحصول على العرض للعمود 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```



-  الحصول على الارتفاع للصف 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

-  الحصول/تعيين اتجاه العرض
```javascript
xs.sheet.data.displayRight2Left
```

## استدعاء الحدث الرد
-  يمكننا تتبع الأحداث أدناه
```javascript
 xs.on('cell-selected', (cell, ri, ci) => {
                console.log('cell selected:', cell, ', ri:', ri, ', ci:', ci);
                if (ci === -1) {
                    console.log('ci === -1 means a row selected ',ri);
                }
                if (ri === -1) {
                    console.log('ri === -1 means a column selected',ci);
                }
            }).on('cells-selected', (cell, range) => {
                console.log('range   selected:', cell, ', rang:', range);
            }).on('object-selected', (shapeOrImageObj) => {
                console.log('shape or image selected id:', shapeOrImageObj.id, ', type: ', shapeOrImageObj.type);
            }).on('sheet-selected', (id,name) => {
                console.log('sheet selected id:', id, ', name: ',name);
            }).on('sheet-loaded', (id,name) => {
                console.log('sheet load finished:', id, ', name: ',name);
            }).on('cell-edited', (text, ri, ci) => {
	        //just edit the cell
                console.log('text:', text, ', ri: ', ri, ', ci:', ci);
            }).on('cells-updated', (name, cells) => {
	       //cell value got updated
                console.log('cells updated for sheet name:', name);
                cells.forEach((acell, index, array) => {
                console.log('acell got updated:', acell);
            })
            }).on('cells-deleted', (range) => {
                console.log('cells deleted :', range);
            }).on('rows-deleted', (ri, n) => {
                console.log('rows-deleted :', ri, ",size", n);

            }).on('columns-deleted', (ci, n) => {
                console.log('columns-deleted :', ci, ",size", n);

            }).on('rows-inserted', (ri, n) => {
                console.log('rows-inserted :', ri, ",size", n);

            }).on('columns-inserted', (ci, n) => {
                console.log('columns-inserted :', ci, ",size", n);

            });
```
- حدث فحص مسبق
  إذا كانت النتيجة خاطئة، فلن تستمر عملية الإدراج/الحذف.
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## التخصيص

-  تعيين رمز المنزل والرابط
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
-  إظهار شريط القائمة
```javascript
xs.sheet.menubar.show()
```

-  إخفاء شريط القائمة
```javascript
xs.sheet.menubar.hide()
```
## واجهات برمجة التطبيقات لكائن الشكل
- تغيير لون الخلفية لكائن الشكل
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 existed,this will set the background color to Yellow 
     const ashape=xs.sheet.data.shapes[0];
     ashape.setBackgroundColor('#FFFF00');
```

## واجهات برمجة التطبيقات لكائن مربع النص
TextBox هو نوع خاص من الشكل والذي تكون خاصيته نوعه: "TextBox".
على سبيل المثال: سيعرض الكود أدناه أي نوع شكل لصندوق النص

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- تطبيق إعدادات الخط على كائن مربع النص
```javascript
    setFont(fontsettings)
    // the parameter is:
        fontsettings:   {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00', 'italic':true} ,the properties are 'name', 'size', 'bold', 'color', 'italic',they are all optional.
    //for example,we assume shape 0 is a textbox object,this will set the font color to Yellow ,and font size to 12pt,and bold the font. 
     const textbox=xs.sheet.data.shapes[0];
     const fontsettings= {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00'}; 
     textbox.setFont(fontsettings);
```
- تغيير اللون الخلفي تلقائيًا ولون النص للحصول على تأثير نشط بصريًا
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

- إخفاء/إظهار محتوى النص في كائن المربع
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

لمزيد من المعلومات التفصيلية ، يمكنك التحقق من المثال هنا
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>





