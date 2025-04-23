---  
title: طباعة التعليقات أثناء الحفظ إلى PDF عبر Node.js باستخدام C++  
linktitle: طباعة التعليقات أثناء الحفظ إلى صيغة PDF  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: تعلم كيفية طباعة التعليقات عند حفظ مستندات إكسيل إلى PDF باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

تسمح Microsoft Excel بطباعة التعليقات أثناء الطباعة أو الحفظ في صيغة PDF بالخيارات التالية  

- لا شيء  
- في نهاية الجدول  
- كما هو معروض على الجدول  

توفر Aspose.Cells العد [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) لدعم نفس الميزة. يتضمن عد [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) الأعضاء التالية  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **طباعة التعليقات عند الحفظ إلى PDF**  

يوضح الكود التالي كيفية استخدام [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) لطباعة التعليقات عند الحفظ إلى PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from the source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleWorkbookWithComments.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

/*
* For print no comments use "PrintCommentsType.PrintNoComments"
* and for print the comments as displayed on sheet use "PrintCommentsType.PrintInPlace"
* For Print the comments at the end of sheet we use "PrintCommentsType.PrintSheetEnd"
*/
worksheet.getPageSetup().setPrintComments(AsposeCells.PrintCommentsType.PrintSheetEnd);

// Save workbook in pdf format
workbook.save(path.join(dataDir, "PrintCommentWhileSavingToPdf_out.pdf"));
```  

