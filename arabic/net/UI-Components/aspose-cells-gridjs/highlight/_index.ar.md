---
title: العمل مع ميزة GridJs Highlight
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/highlight/
description: توضح هذه المقالة كيفية استخدام GridJs لتمييز نص الخلية ونطاقات الخلايا والأشكال والصور.
keywords: highlight, highlight spreadsheet
---
#  العمل مع ميزة GridJs Highlight
 نحن ندعم JS APIs أدناه لميزة Highlight


-  قم بتمكين التمييز وتعيين نمط الإبراز ، لن تسري جميع واجهات برمجة التطبيقات المميزة إلا بعد تعيين نمط التمييز
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  تعطيل التمييز
```javascript
xs.hideHighlights()
```
-  أضف نص خلية لتمييزه
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  قم بإزالة التمييز لنص الخلية في المصفوفة
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  الحصول على مصفوفة لتمييز نص الخلية
```javascript
xs.sheet.getHighlightTexts()
```

-  أضف نطاق خلايا لتمييزه
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  قم بإزالة التمييز لنطاق الخلايا في المصفوفة
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  احصل على صفيف لتمييز نطاق الخلايا
```javascript
xs.sheet.getHighlightRanges()
```

-  اضبط نطاق الخلايا على عكس الضوء
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  إزالة التمييز لعكس الضوء
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  الحصول على نطاق خلية تمييز معكوس
```javascript
xs.sheet.getHighlightInverseRange()
```


-  أضف شكلًا لإبراز المصفوفة
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  إزالة شكل التمييز في المصفوفة
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  احصل على مجموعة لإبراز الشكل
```javascript
xs.sheet.getHighlightShaps()
```

-  إضافة مربع نص لإبرازه ، مربع النص هو نوع خاص من الأشكال التي تكون خاصية الكتابة هي: "TextBox" ،
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- قم بإزالة نطاق التمييز في مربع النص ، مربع النص هو نوع خاص من الأشكال التي تكون خاصية الكتابة هي: "TextBox" ،
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  إضافة صورة لتسليط الضوء على مجموعة
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  قم بإزالة صورة التمييز في المصفوفة
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  الحصول على مجموعة لتسليط الضوء على الصورة
```javascript
xs.sheet.getHighlightImages()
```

-  قم بتعيين ما إذا كنت تريد تمييز كل ورقة العمل ، وتضمين جميع الأشكال والصور
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

###  تسليط الضوء على كائن مربع النص
مربع النص هو نوع خاص من الأشكال حيث تكون خاصية الكتابة هي: "TextBox" ،
على سبيل المثال: سيُظهر الرمز أدناه الشكل الذي يمثل مربع نص

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  أضف تسليط الضوء على كائن مربع النص
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

-  الحصول على تمييز لكائن مربع النص
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

-  إخفاء / إظهار محتوى النص في كائن مربع النص
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



يمكنك العثور على المزيد في صفحة العرض التوضيحي الخاصة بنا على github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
