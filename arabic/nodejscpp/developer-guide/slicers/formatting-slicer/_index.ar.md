---  
title: تنسيق المقسم باستخدام Node.js عبر C++  
linktitle: تنسيق المنقي  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/formatting-slicer/  
---  

## **سيناريوهات الاستخدام المحتملة**  

 يمكنك تنسيق المقسم في Microsoft Excel عن طريق ضبط عدد الأعمدة أو عبر إعداد النمط الخاص به، وغيرها. يتيح لك Aspose.Cells for Node.js via C++ أيضًا القيام بذلك باستخدام خصائص [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) و[**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--).  

## **تنسيق المنقي**  

يرجى الاطلاع على الكود التالي، يحمل [ملف إكسل عينة](67338473.xlsx) الذي يحتوي على قالب تصفية. يدخل إلى قالب التصفية ويحدد عدد الأعمدة ونوع النمط الخاص به ثم يحفظه باسم [ملف إكسل الناتج](67338474.xlsx). يوضح اللقطة الشاشة مظهر قالب التصفية بعد تنفيذ الكود العينة.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
