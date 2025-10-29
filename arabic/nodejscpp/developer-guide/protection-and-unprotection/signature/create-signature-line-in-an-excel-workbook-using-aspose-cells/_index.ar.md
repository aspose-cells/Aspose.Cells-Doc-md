---  
title: إنشاء سطر توقيع في دفتر الأستاذ Excel باستخدام Aspose.Cells for Node.js via C++  
linktitle: إنشاء سطر توقيع في سجل Excel باستخدام Aspose.Cells  
type: docs  
weight: 150  
url: /ar/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: يصف هذا المقال كيفية إنشاء سطر توقيع في دفتر أستاذ Excel باستخدام رمز Node.js مع Aspose.Cells for Node.js via C++.  
keywords: إنشاء سطر توقيع في دفتر أستاذ Excel باستخدام Node.js عبر C++، كيفية إنشاء سطر توقيع في دفتر أستاذ Excel، كيفية إضافة سطر توقيع، كيفية إضافة سطر توقيع إلى ملف Excel.  
---  

## **مقدمة**  

توفر Microsoft Excel ميزة إضافة **سطر توقيع** في سجل Excel. يمكنك إضافة سطر توقيع عن طريق النقر فوق علامة **إدراج** ثم تحديد **سطر توقيع** من مجموعة **نص**.  

## **كيفية إنشاء خط توقيع لإكسل**  

يقدم Aspose.Cells for Node.js via C++ أيضًا هذه الميزة ووفقًا لهذا الاستخدام الخاص به. سيشرح هذا المقال كيفية استخدام هذه الخاصية لإضافة سطر توقيع باستخدام Aspose.Cells.  

يضيف رمز النموذج التالي سطر توقيع باستخدام خاصية [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) ويحفظ المصنف.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
