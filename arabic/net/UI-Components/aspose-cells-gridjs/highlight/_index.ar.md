---
title: العمل مع ميزة GridJs Highlight
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/highlight/
description: توضح هذه المقالة كيفية استخدام GridJs لتمييز نص الخلية ونطاقات الخلايا والأشكال والصور.
keywords: highlight, highlight spreadsheet,redaction,remarks
---
#  العمل مع ميزة GridJs Highlight
 نحن ندعم واجهات برمجة التطبيقات JS أدناه لميزة Highlight


-  قم بتمكين التمييز وتعيين نمط التمييز، ولن يتم تفعيل جميع واجهات برمجة التطبيقات الخاصة بالتمييز إلا بعد تعيين نمط التمييز في ورقة العمل النشطة
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  قم بتحديث نمط التمييز المحدد في ورقة العمل النشطة
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


-  تعطيل التمييز في ورقة العمل النشطة
```javascript
xs.sheet.hideHighlights()
```
-  أضف نص خلية لتمييزه في ورقة العمل النشطة
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  إزالة التمييز لنص الخلية في الصفيف في ورقة العمل النشطة
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- احصل على مصفوفة لتمييز نص الخلية في ورقة العمل النشطة
```javascript
xs.sheet.getHighlightTexts()
```

-  أضف نطاق خلايا لتمييزه في ورقة العمل النشطة
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  إزالة التمييز لنطاق الخلايا في الصفيف في ورقة العمل النشطة
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  احصل على مصفوفة لتسليط الضوء على نطاق الخلايا في ورقة العمل النشطة
```javascript
xs.sheet.getHighlightRanges()
```

-  قم بتعيين نطاق الخلايا لعكس التمييز في ورقة العمل النشطة
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  قم بإزالة التمييز من أجل التمييز العكسي في ورقة العمل النشطة
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  احصل على نطاق خلايا التمييز العكسي في ورقة العمل النشطة
```javascript
xs.sheet.getHighlightInverseRange()
```


-  أضف شكلاً لتمييز المصفوفة في ورقة العمل النشطة
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  قم بإزالة شكل التمييز في الصفيف في ورقة العمل النشطة
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  احصل على مصفوفة لشكل التمييز في ورقة العمل النشطة
```javascript
xs.sheet.getHighlightShaps()
```

-  أضف مربع نص لتسليط الضوء عليه، مربع النص هو نوع خاص من الأشكال وخاصية النوع هي:"TextBox"، في ورقة العمل النشطة
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  إزالة نطاق التمييز في مربع النص، مربع النص هو نوع خاص من الأشكال التي تكون خاصية النوع هي:"TextBox"، في ورقة العمل النشطة
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  أضف صورة لتسليط الضوء على المصفوفة في ورقة العمل النشطة
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- قم بإزالة الصورة المميزة في الصفيف في ورقة العمل النشطة
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  الحصول على مجموعة لتسليط الضوء على الصورة
```javascript
xs.sheet.getHighlightImages()
```

-  قم بتعيين ما إذا كان سيتم تمييز كافة الكائنات في ورقة العمل النشطة، بما في ذلك جميع الأشكال والصور وكل منطقة ورقة العمل
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  تعيين وظيفة تسليط الضوء على الصورة المخصصة
```javascript
xs.sheet.setCustomHighlightImgFunc(func)
   // the parameters are:
   func: the custom highlight image function, it shall take two parameters ,first is ishighlight,the second one is the fabric image object 
   //we use fabric js to manage image object, please refer to http://fabricjs.com/image-filters to check more info
   below is an example for the decleare function: 
   const customHighlightImage = (ishighlight, imgobj) => {
            imgobj.filters[0] = ishighlight ? new fabric.Image.filters.Sepia() : false;
            imgobj.applyFilters();
        }
    
```

-  مسح إعداد التمييز لورقة العمل النشطة
```javascript
xs.sheet.clearHighlights()

```

###  تسليط الضوء على كائن مربع النص
مربع النص هو نوع خاص من الأشكال وخاصية النوع هي:"TextBox"،
على سبيل المثال: سيوضح الكود أدناه الشكل الذي يمثله مربع النص

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  إضافة تمييز لكائن مربع النص
```javascript
    addHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox

//for example,we assume shape 0 is a textbox object
const textbox=xs.sheet.data.shapes[0];
//first we shall add to highlight shape to enable the highlight for the textbox shape object,it support multiple range postion 
 xs.sheet.addHighlightShape(textbox.id);
 textbox.addHighlight(5,10);
 textbox.addHighlight(18,28);
```

-  إزالة التمييز لكائن مربع النص
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  الحصول على تسليط الضوء على كائن مربع النص
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  تغيير لون الخلفية لكائن مربع النص
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  قم بتغيير لون الخلفية ولون النص تلقائيًا للحصول على تأثير مرئي نشط
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  إخفاء/إظهار محتوى النص في كائن مربع النص
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



يمكنك العثور على المزيد في صفحتنا التجريبية على github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
