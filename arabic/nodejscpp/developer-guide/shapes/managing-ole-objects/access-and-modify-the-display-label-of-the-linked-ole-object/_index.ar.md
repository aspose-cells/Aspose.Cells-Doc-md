---
title: الوصول وتعديل تسمية العرض للكائن Ole المرتبط باستخدام Node.js عبر C++
linktitle: الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط
type: docs
weight: 100
url: /ar/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: تعلم كيفية الوصول إلى وتعديل تسمية العرض لكائن Ole المرتبط باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

 يسمح لك إكسل بتغيير تسمية العرض لكائن Ole كما هو موضح في لقطة الشاشة التالية. يمكنك أيضًا الوصول إلى أو تعديل تسمية العرض لكائن Ole باستخدام واجهات برمجة التطبيقات Aspose.Cells مع الخاصية [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط**

 يرجى الاطلاع على رمز النموذج التالي، حيث يقوم بتحميل ملف إكسل النموذجي الذي يحتوي على كائن Ole. يتواصل الكود مع كائن Ole ويغير تسميته من Sample APIs إلى Aspose APIs. يرجى مراجعة المخرجات في الكونسول أدناه التي تُظهر تأثير الشفرة النموذجية على ملف إكسل النموذجي كمرجع.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **مخرجات الوحدة**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
