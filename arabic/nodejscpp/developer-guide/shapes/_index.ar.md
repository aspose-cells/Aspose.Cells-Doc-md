---  
title: إضافة صور وأشكال لملفات Excel باستخدام Node.js عبر C++  
linktitle: الأشكال  
type: docs  
weight: 140  
url: /ar/nodejs-cpp/insert-shapes/  
description: إدارة الصور والكائنات OLE والأشكال في ملفات Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
أحيانًا تحتاج إلى إدراج بعض الأشكال الضرورية في ورقة العمل. قد تحتاج إلى إدراج نفس الشكل في مواقع مختلفة من ورقة العمل. أو تحتاج إلى إدراج العديد من الأشكال دفعة واحدة في ورقة العمل.  
لا تقلق! [Aspose.Cells](https://products.aspose.com/cells/) تدعم جميع هذه العمليات.  
{{% /alert %}}  

الأشكال في Excel مقسمة بشكل رئيسي إلى الأنواع التالية:  
- **الصور**  
- **الكائنات OLE**  
- **الخطوط**  
- **المستطيلات**  
- **الأشكال الأساسية**  
- **السهام البلوكية**  
- **أشكال المعادلة**  
- **رسوم بيانية لسير العمل**  
- **النجوم والرايات**  
- **التلويحات**  

سيختار هذا المستند التعليمي شكلين أو شكل واحد من كل نوع لإنشاء عينات. من خلال هذه الأمثلة، ستتعلم كيفية استخدام [Aspose.Cells](https://products.aspose.com/cells/) لإدراج الشكل المحدد في ورقة العمل.  

## **إضافة صور في ورقة عمل Excel باستخدام Node.js**  

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:  
ببساطة استدعِ طريقة [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) من مجموعة [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). تأخذ طريقة [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) المعلمات التالية:  

- **فهرس الصف الأعلى الأيسر**، فهرس الصف الأعلى.  
- **فهرس العمود الأعلى الأيسر**، فهرس العمود الأعلى.  
- **اسم ملف الصورة**، اسم ملف الصورة، مع المسار الكامل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **إدراج كائنات OLE في ورقة عمل Excel باستخدام Node.js**  

يدعم Aspose.Cells إضافة واستخراج والتعامل مع كائنات OLE في أوراق العمل. لهذا السبب، يحتوي Aspose.Cells على فئة [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)، المستخدمة لإضافة كائن OLE جديد إلى قائمة التجميع. فئة أخرى، [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject)، تمثل كائن OLE. لديها بعض الأعضاء المهمة:  

- تحدد الخاصية [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) بيانات الصورة (الأيقونة) من نوع مصفوفة البايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.  
- تحدد الخاصية [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) بيانات الكائن على شكل مصفوفة البايت. سيتم عرض هذه البيانات في البرنامج المعني عند النقر المزدوج على أيقونة كائن OLE.  

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **إدراج خط في ورقة عمل Excel باستخدام Node.js**  

ينتمي شكل الخط إلى فئة **الخطوط**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي تريد إدراج الخط فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر الخط من 'الأشكال المستخدمة مؤخرًا' أو 'الخطوط'  

![](line.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج خط في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape) ميراث.  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج خط في ورقة العمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](line2.png)  

## **إدراج سهم خطي في ورقة عمل Excel باستخدام Node.js**  

شكل سهم السطر ينتمي إلى فئة **الخطوط**. وهو حالة خاصة من الخط.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي تريد إدراج سهم الخط فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر سهم السطر من 'الأشكال المُستخدمة مؤخرًا' أو 'الخطوط'  

![](line_arrow1.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج سهم خط في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape) ميراث.  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج سهم خطي في ورقة عمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](line_arrow2.png)  

## **إدراج مستطيل في ورقة عمل إكسل باستخدام Node.js**  

ينتمي شكل المستطيل إلى فئة **المستطيلات**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي تريد إدراج المستطيل فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر المستطيل من 'الأشكال المُستخدمة مؤخرًا' أو 'المستطيلات'  

![](rectangle.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج مستطيل في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape) ميراث.  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج مستطيل في ورقة عمل.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](rectangle2.png)  

## **إدراج مكعب في ورقة عمل إكسل باستخدام Node.js**  

ينتمي شكل المكعب إلى فئة **الأشكال الأساسية**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي تريد إدراج المكعب فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر المكعب من **الأشكال الأساسية**  

![](cube.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج مكعب في الورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
الطريقة ترجع كائن [شكل](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج مكعب في ورقة عمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](cube2.png)  

## **إدراج سهم ناتئ رباعي لورقة عمل إكسل باستخدام Node.js**  

ينتمي شكل سهم ناتئ رباعي إلى فئة **السهم الكتلي**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي تريد إدراج سهم المربعي الدعوة فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر سهم ناتئ رباعي من **السهم الكتلي**  

![](callout_quad_arrow.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج سهم رباعي الاتصال في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
الطريقة ترجع كائن [شكل](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج سهم ناتئ رباعي في ورقة عمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](callout_quad_arrow2.png)  

## **إدراج علامة ضرب لورقة عمل إكسل باستخدام Node.js**  

ينتمي شكل علامة الضرب إلى فئة **أشكال المعادلة**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي ترغب في إدراج علامة الضرب فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر علامة الضرب من **أشكال المعادلة**  

![](multiplication_sign.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج علامة الضرب في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
الطريقة ترجع كائن [شكل](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج علامة ضرب في ورقة عمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](multiplication_sign2.png)  

## **إدراج مستند متعدد في ورقة عمل إكسل باستخدام Node.js**  

ينتمي شكل المستند المتعدد إلى فئة **مخططات التدفق**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي ترغب في إدراج مستند متعدد الوثائق فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر المستند متعدد من **مخططات التدفق**  

![](multidocument.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج مستند متعدد الوثائق في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
الطريقة ترجع كائن [شكل](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج مستند متعدد في ورقة عمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](multidocument2.png)  

## **إدراج نجم ذو خمس نقاط في ورقة عمل إكسل باستخدام Node.js**  

شكل النجمة ذات الخمس نقاط ينتمي إلى فئة **النجوم والرايات**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي ترغب في إدراج النجمة المؤلفة من خمس نقاط فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر النجمة ذات الخمس نقاط من **النجوم والرايات**  

![](star_5_points.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الأسلوب التالي لإدراج نجمة ذات خمس نقاط في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
الطريقة ترجع كائن [شكل](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج نجمة ذات خمس نقاط في ورقة العمل.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](star_5_points2.png)  

## **إدراج سحابة فقاعة الفكر إلى ورقة إكسل باستخدام Node.js**  

شكل سحابة فقاعة الفكر ينتمي إلى فئة **التعليقات**.  

***في Microsoft Excel (على سبيل المثال 2007):***  

- حدد الخلية التي تريد إدراج سحابة الفكر فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر سحابة فقاعة الفكر من **التعليقات**  

![](thought_bubble_cloud.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الأسلوب التالي لإدراج سحابة فكرية في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
الطريقة ترجع كائن [شكل](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج سحابة فقاعة الفكر في ورقة العمل.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](thought_bubble_cloud2.png)  

## **مواضيع متقدمة**  
- [تغيير قيم التعديل للشكل](/cells/ar/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [نسخ الأشكال بين أوراق العمل](/cells/ar/nodejs-cpp/copy-shapes-between-worksheets/)  
- [البيانات في شكل غير مبدل](/cells/ar/nodejs-cpp/data-in-non-primitive-shape/)  
- [العثور على الموضع المطلق للشكل داخل الورقة العمل](/cells/ar/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [الحصول على نقاط الاتصال من الشكل](/cells/ar/nodejs-cpp/get-connection-points-from-shape/)  
- [إدارة الضوابط](/cells/ar/nodejs-cpp/managing-controls/)  
- [إضافة رموز إلى ورقة العمل](/cells/ar/nodejs-cpp/insert-svg-to-excel/)  
- [إدارة كائنات OLE](/cells/ar/nodejs-cpp/managing-ole-objects/)  
- [إدارة الصور](/cells/ar/nodejs-cpp/managing-pictures/)  
- [إدارة الذكاء الفني](/cells/ar/nodejs-cpp/managing-smartart/)  
- [إدارة مربع النص](/cells/ar/nodejs-cpp/managing-textbox-of-excel/)  
- [إضافة كلمة WaterArt كعلامة مائية إلى ورقة العمل](/cells/ar/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [تحديث القيم للأشكال المرتبطة](/cells/ar/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل](/cells/ar/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [إدارة خيارات الشكل](/cells/ar/nodejs-cpp/managing-shape-options/)  
- [إدارة خيارات نص الشكل](/cells/ar/nodejs-cpp/managing-shape-text-options/)  
- [ملحقات الويب - إضافات الأوفيس](/cells/ar/nodejs-cpp/web-extensions-office-add-ins/)  


