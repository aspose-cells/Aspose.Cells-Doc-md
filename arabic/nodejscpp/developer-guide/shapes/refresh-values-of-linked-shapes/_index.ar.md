---  
title: تحديث قيم الأشكال المرتبطة باستخدام Node.js عبر C++  
linktitle: تحديث قيم الأشكال المرتبطة  
type: docs  
weight: 3200  
url: /ar/nodejs-cpp/refresh-values-of-linked-shapes/  
description: تعلم كيفية تحديث قيم الأشكال المرتبطة في Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

أحيانًا، يكون لديك شكل مرتبط في ملف Excel الخاص بك مرتبط بخانة معينة. في Microsoft Excel، يؤدي تغيير قيمة الخانة المرتبطة أيضًا إلى تغيير قيمة الشكل المرتبط. ويعمل هذا بشكل جيد مع Aspose.Cells for Node.js via C++ إذا كنت تريد حفظ المصنف بصيغة XLS أو XLSX. ومع ذلك، إذا أردت حفظ المصنف بصيغة PDF أو HTML، فستحتاج إلى استدعاء طريقة [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) لتحديث قيمة الشكل المرتبط.  

{{% /alert %}}  

## مثال  

يظهر لقطة الشاشة التالية ملف إكسل المصدر المستخدم في الشفرة أدناه. يحتوي على صورة مرتبطة مرتبطة بخلايا A1 إلى E4. سنغير قيمة الخلية B4 باستخدام Aspose.Cells ثم نستدعي طريقة [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) لتحديث قيمة الصورة وحفظها بتنسيق PDF.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

يمكنك تنزيل [ملف إكسل المصدر](95584291.xlsx) و [ملف PDF الناتج](95584292.pdf) من الروابط المعطاة.  

### رمز Node.js لتحديث قيم الأشكال المرتبطة  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
