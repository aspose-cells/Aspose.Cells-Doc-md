---  
title: كيفية تغيير لون خط التعليق باستخدام Node.js عبر C++  
linktitle: كيفية تغيير لون الخط في التعليق  
type: docs  
weight: 180  
url: /ar/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
يتيح Microsoft Excel للمستخدمين إضافة تعليقات إلى الخلايا لإضافة معلومات إضافية وتسليط الضوء على البيانات. قد يحتاج المطورون إلى تخصيص التعليق لتحديد إعدادات المحاذاة واتجاه النص ولون الخط، إلخ. تقدم Aspose.Cells for Node.js via C++ APIs لإنجاز المهمة.  
{{% /alert %}}  

توفر Aspose.Cells for Node.js via C++ خاصية [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) لتعيين لون خط التعليق. يوضح الكود التالي استخدام الخاصية [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) لضبط اتجاه النص في التعليق.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add some text in cell A1
worksheet.getCells().get("A1").putValue("Here");

// Add a comment to A1 cell
const commentIndex = worksheet.getComments().add("A1");
const comment = worksheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set the Comment note
comment.setNote("This is my Comment Text. This is Test.");

const shape = worksheet.getComments().get("A1").getCommentShape();

shape.getFill().getSolidFill().setColor(AsposeCells.Color.Black);
const font = shape.getFont();
font.setColor(AsposeCells.Color.White);
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setFontColor(true);
shape.getTextBody().format(0, shape.getText().length, font, styleFlag);

// Save the Excel file
workbook.save(path.join(outputDir, "outputChangeCommentFontColor.xlsx"));
```  

الملف الناتج (102662195.xlsx) الذي تم إنشاؤه بواسطة الكود أعلاه مرفق للرجوع إليه.  
