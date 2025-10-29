---  
title: تعيين حدود النطاق باستخدام Node.js عبر C++  
linktitle: تعيين حدود النطاق  
type: docs  
weight: 600  
url: /ar/nodejs-cpp/set-range-border/  
---  

## **سيناريوهات الاستخدام المحتملة**  
عندما تريد تعيين حدود لنطاق، لا تحتاج إلى تعيين كل خلية بشكل فردي. يمكنك تعيين الحدود على النطاق. يقدم Aspose.Cells for Node.js via C++ هذه الميزة.  
يوفر هذا المقال رمز عينة يستخدم Aspose.Cells for Node.js via C++ لضبط حدود النطاق.  

## **تعيين حدود النطاق في Excel**  
لتعيين الحدود لنطاق في Excel، يمكنك اتباع هذه الخطوات:  
1. حدد نطاق الخلايا التي ترغب في تطبيق الحد لها.  
2. في علامة التبويب "الرئيسية" في الشريط، ابحث عن مجموعة "الخط".  
3. ضمن مجموعة "الخط"، انقر فوق زر القائمة المنسدلة "الحدود".  
<br>  
<img src="border.png" />  
4. اختر نوع الحد الذي ترغب في تطبيقه من الخيارات المتاحة في القائمة المنسدلة. يمكنك اختيار أنماط الحدود المعدة مسبقًا أو تخصيص حدودك الخاصة.  
5. بمجرد اختيارك لنمط الحد المطلوب، سيتم تطبيق الحد على النطاق المحدد من الخلايا.  

## **تعيين حدود النطاق باستخدام Aspose.Cells for Node.js via C++**  
يوضح هذا المثال كيف:  

1. إنشاء دفتر عمل.  
2. إضافة البيانات إلى خلايا في ورقة العمل الأولى.  
3. إنشاء [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. تعيين الحدود الداخلية للنطاق.  
5. تعيين الحدود الخارجية للنطاق.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
