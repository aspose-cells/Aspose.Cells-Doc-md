---  
title: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل باستخدام Node.js عبر C++  
linktitle: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل  
type: docs  
weight: 1500  
url: /ar/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: تعلم كيفية ضبط هوامش التعليقات أو الأشكال داخل ورقة عمل إكسل باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

يسمح Aspose.Cells لك بضبط هوامش أي شكل أو تعليق باستخدام خاصية [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/). تعيد هذه الخاصية كائن من فئة [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment) الذي يحتوي على خصائص مختلفة مثل [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--)، [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--)، [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--)، [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--)، وغيرها، والتي يمكن استخدامها لضبط الهوامش العليا، اليسرى، السفلى واليمنى.  

## **تعيين هوامش التعليق أو الشكل داخل ورقة العمل**  

يرجى الاطلاع على الكود عينة التالي. يقوم بتحميل [ملف Excel عيني](61767851.xlsx) الذي يحتوي على شكلين. يقوم الكود بالوصول إلى الأشكال واحد تلو الآخر ويضبط هوامشها العلوية واليسرى والسفلية واليمنى. يرجى الاطلاع على [ملف Excel الناتج](61767852.xlsx) الذي تم إنشاؤه بواسطة الكود ولقطة شاشة توضح تأثير الكود على ملف Excel الناتج.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  

