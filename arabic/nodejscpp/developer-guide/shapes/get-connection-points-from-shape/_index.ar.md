---  
title: الحصول على نقاط الاتصال من الشكل باستخدام Node.js عبر C++  
linktitle: الحصول على نقاط الاتصال من الشكل  
type: docs  
weight: 3500  
url: /ar/nodejs-cpp/get-connection-points-from-shape/  
description: تعلم كيفية استرجاع نقاط الاتصال من الأشكال في Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

تقدم Aspose.Cells ميزات غنية لإدارة الأشكال في ورقة العمل. أحيانًا، هناك حاجة للحصول على نقاط اتصال الشكل لموازنة أو وضع الأشكال في المكان المناسب. لهذا الغرض، يلزم جميع نقاط الاتصال. يمكن استخدام الكود التالي للحصول على قائمة نقاط اتصال شكل معين باستخدام خاصية [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--)

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Instantiate a new Workbook.
const newWorkbook = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const worksheet = newWorkbook.getWorksheets().get(0);

// Add a new textbox to the collection.
const textboxIndex = worksheet.getTextBoxes().add(2, 1, 160, 200);

// Access your text box which is also a shape object from shapes collection
const shape = newWorkbook.getWorksheets().get(0).getShapes().get(0);

// Get all the connection points in this shape
const connectionPoints = shape.getConnectionPoints();

// Display all the shape points
connectionPoints.forEach(pt => {
console.log(`X = ${pt[0]}, Y = ${pt[1]}`);
```  

