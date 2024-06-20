---
title: العمل مع ميزة تحديد في GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/highlight/
description: يوضح هذا المقال كيفية استخدام التسليط في نص الخلية ونطاقات الخلايا، الأشكال والصور في GridJs
keywords: GridJs, تسليط الضوء، تسليط الجدول الإلكتروني، حجب المعلومات، تعليقات
---

# العمل مع ميزة تحديد في GridJs 
نحن ندعم واجهات برمجة تطبيقات JavaScript (JS APIs) التالية لميزة التحديد 


- تمكين التحديد وتعيين نمط التحديد، ستطبق جميع واجهات برمجة التطبيقات (APIs) المتعلقة بالتحديد فقط بعد تعيين نمط التحديد في ورقة العمل النشطة 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- تحديث نمط التحديد المضبوط في ورقة العمل النشطة 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- تعطيل التحديد في ورقة العمل النشطة    
```javascript
xs.sheet.hideHighlights()
```
- إضافة نص الخلية للتحديد في ورقة العمل النشطة 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  إزالة التمييز لنص الخلية في مصفوفة في ورقة العمل النشطة 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

-  الحصول على مصفوفة لتمييز نص الخلية في ورقة العمل النشطة   
```javascript
xs.sheet.getHighlightTexts()
```

-  إضافة نطاق الخلية للتمييز في ورقة العمل النشطة 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  إزالة التمييز لنطاق الخلية في المصفوفة في ورقة العمل النشطة 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  الحصول على مصفوفة لتمييز نطاق الخلية في ورقة العمل النشطة   
```javascript
xs.sheet.getHighlightRanges()
```

-  تعيين نطاق الخلية للتمييز العكسي في ورقة العمل النشطة 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  إزالة التمييز العكسي في ورقة العمل النشطة 
```javascript
xs.sheet.removeHighlightInverseRange()

```

-  الحصول على مصفوفة التمييز العكسي لنطاق الخلية في ورقة العمل النشطة 
```javascript
xs.sheet.getHighlightInverseRange()
```


-  إضافة شكل لمصفوفة التمييز في ورقة العمل النشطة 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  إزالة التمييز لشكل في المصفوفة في ورقة العمل النشطة 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  الحصول على مصفوفة لتمييز الشكل في ورقة العمل النشطة  
```javascript
xs.sheet.getHighlightShaps()
```

-  إضافة مربع نص للتمييز، المربع نص هو نوع خاص من الشكل الذي يكون خاصيته النوعية:"TextBox", في ورقة العمل النشطة 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  إزالة نطاق التمييز في مربع النص، المربع النص هو نوع خاص من الشكل الذي يكون خاصيته النوعية:"TextBox", في ورقة العمل النشطة 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  إضافة صورة لمصفوفة التمييز في ورقة العمل النشطة 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  إزالة تمييز الصورة في المصفوفة في ورقة العمل النشطة 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  الحصول على مصفوفة لتمييز الصورة  
```javascript
xs.sheet.getHighlightImages()
```

- تعيين ما إذا كان يتعين تمييز جميع الكائنات في ورقة العمل النشطة، بما في ذلك جميع الأشكال والصور وجميع منطقة ورقة العمل
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  تحديد وظيفة تمييز الصور المخصصة
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

- مسح إعداد التمييز لورقة العمل النشطة
```javascript
xs.sheet.clearHighlights()

```

### تمييز لكائن مربع النص
صندوق النص هو نوع خاص من الشكل وخاصيته نوعه: "TextBox"
على سبيل المثال: سيعرض الكود أدناه أي نوع شكل لصندوق النص

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- إضافة تمييز لكائن صندوق النص
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

- إزالة التمييز عن كائن صندوق النص 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- الحصول على تمييز لكائن صندوق النص 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




يمكنك العثور على المزيد في صفحة العرض التوضيحي لدينا على github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
