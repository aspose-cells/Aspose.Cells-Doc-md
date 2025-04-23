---
title: إدراج صورة استنادًا إلى مرجع خلية باستخدام Node.js عبر C++
linktitle: إدراج صورة بناءً على مرجع الخلية
type: docs
weight: 150
url: /ar/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: تعلم كيفية إدراج صورة في ورقة عمل استنادًا إلى مرجع خلية باستخدام Aspose.Cells for Node.js via C++. عرض بيانات الخلية في صورة.
---

{{% alert color="primary" %}}
أحيانًا يكون لديك صورة فارغة وتحتاج إلى عرض البيانات أو المحتويات في الصورة عن طريق تحديد إشارة للخلية في شريط الصيغة. تدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).
{{% /alert %}}

## إدراج صورة بناءً على إشارة الخلية

يدعم Aspose.Cells for Node.js via C++ عرض محتويات خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. بما أن الخلية أو نطاق الخلايا مرتبطين بالكائن الرسومي، فإن التغييرات التي تجريها على البيانات في تلك الخلية أو النطاق تظهر تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل من خلال استدعاء طريقة [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) من مجموعة [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (الم encapsulated في عنصر [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). حدد نطاق الخلية باستخدام سمة [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) من الكائن [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).

### مثال على الكود

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

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
