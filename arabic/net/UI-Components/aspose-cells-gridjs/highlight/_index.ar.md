---
title: العمل مع ميزة GridJs Highlight
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/highlight/
description: توضح هذه المقالة كيفية استخدام GridJs لتمييز نص الخلية ونطاقات الخلايا والأشكال والصور.
keywords: highlight, highlight spreadsheet
---
# العمل مع ميزة GridJs Highlight
 نحن ندعم JS APIs أدناه لميزة Highlight


- قم بتمكين التمييز وتعيين نمط الإبراز ، لن تسري جميع واجهات برمجة التطبيقات المميزة إلا بعد تعيين نمط التمييز
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- تعطيل التمييز
```javascript
xs.hideHighlights()
```
- أضف نص خلية لتمييزه
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- قم بإزالة التمييز لنص الخلية في المصفوفة
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

- أضف نطاق خلايا لتمييزه
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- قم بإزالة التمييز لنطاق الخلايا في المصفوفة
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

- اضبط نطاق الخلايا على عكس الضوء
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- إزالة التمييز لعكس الضوء
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  الحصول على نطاق خلية تمييز معكوس
```javascript
xs.sheet.getHighlightInverseRange()
```


- إضافة شكل لتمييز المصفوفة
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- إزالة شكل التمييز في المصفوفة
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  احصل على مجموعة لإبراز الشكل
```javascript
xs.sheet.getHighlightShaps()
```


- إضافة صورة لتسليط الضوء على مجموعة
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- قم بإزالة صورة التمييز في المصفوفة
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


- تعيين وظيفة تسليط الضوء على الصورة المخصصة
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

يمكنك العثور على المزيد في صفحة العرض التوضيحي الخاصة بنا على github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
