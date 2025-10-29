---  
title: إدارة الصور باستخدام Node.js عبر C++  
linktitle: إدارة الصور  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/managing-pictures/  
description: تعلم كيفية إضافة الصور وتحديد موقعها في جداول البيانات باستخدام Aspose.Cells for Node.js via C++.  
---  

يسمح Aspose.Cells للمطورين بإضافة الصور إلى جداول البيانات في وقت التشغيل. علاوة على ذلك، يمكن التحكم في تحديد موضع هذه الصور في وقت التشغيل، والأمر الذي يتم مناقشته بتفصيل أكثر في الأقسام القادمة.

يشرح هذا المقال كيفية إضافة الصور وكيفية إدراج صورة تظهر محتوى خلايا معينة.

## **إضافة الصور**

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:  
ببساطة استدعِ طريقة [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) من مجموعة [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). تأخذ طريقة [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) المعلمات التالية:

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

## **تحديد مواقع الصور**

هناك طريقتان ممكنتان للتحكم في تحديد موقع الصور باستخدام Aspose.Cells:

- تحديد موقع نسبي: تعريف موقع نسبي لارتفاع الصف والعرض.
- التمركز المطلق: تحديد الموقع الدقيق على الصفحة حيث سيتم إدراج الصورة، على سبيل المثال، 40 بكسل إلى اليسار و20 بكسل أسفل حافة الخلية.

### **التحديد النسبي**

يمكن للمطورين وضع الصور بنسبة متناسبة مع ارتفاع الصف وعرض العمود باستخدام خصائص [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) و [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) من كائن [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). يمكن الحصول على كائن [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) من مجموعة [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) من خلال تمرير فهرس الصورة الخاص به. يُضع هذا المثال صورة في خلية F6.

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
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **التحديد المطلق**

يمكن للمطورين أيضًا وضع الصور بشكل مطلق باستخدام خصائص [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) و [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) من كائن [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). يضع هذا المثال صورة في الخلية F6، على بعد 60 بكسل من اليسار و 10 بكسل من أعلى الخلية.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **إدراج صورة بناءً على مرجع الخلية**

يتيح Aspose.Cells عرض محتويات خلية ورق العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي ترغب في عرضها. نظرًا لأن الخلية، أو نطاق الخلية، مرتبط بالكائن الرسومي، فإن التغييرات التي تقوم بها في البيانات في تلك الخلية أو نطاق الخلية ستظهر تلقائيًا في الكائن الرسومي.

أضف صورة إلى ورقة العمل عن طريق استدعاء طريقة [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) من مجموعة [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). حدد نطاق الخلايا باستخدام سمة [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) من كائن [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **مواضيع متقدمة**
- [إضافة مجموعة رموز مشروطة مع نص الخلية](/cells/ar/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [إدراج صورة بناءً على مرجع الخلية](/cells/ar/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [تحميل صورة ويب من عنوان URL إلى ورقة عمل Excel](/cells/ar/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="nodejs-cpp" >}}
