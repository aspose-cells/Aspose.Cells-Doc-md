---
title: كيفية تصدير معادلات Excel إلى أنواع أخرى من التعبيرات
linktitle: تصدير المعادلة
type: docs
weight: 100
url: /ar/nodejs-cpp/export-equation/
---

أحيانًا، قد تحتاج إلى تصدير دالات Excel إلى تنسيقات أخرى في الشيفرة الخاصة بك لتلبية احتياجات عملك، ثم يمكن لمكتبة Aspose.Cells تلبية احتياجاتك. يتناول المحتوى التالي بعض الطرق حول كيفية تصدير معادلات Excel إلى تنسيقات أخرى، آمل أن تكون مفيدة لك.

لقد أعددنا رمزًا نموذجيًا هنا لمساعدتك على تحقيق أهدافك باستخدام Aspose.Cells. كما يتم توفير ملفات العينة اللازمة.

ملف عينة: [Sample.xlsx](Sample.xlsx)

## تصدير المعادلات كتعابير LaTeX

إذا كنت تريد تصدير معادلات في Excel كتعابير LaTeX، يمكنك استخدام الدالة [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--). 

يعرض الكود النموذجي التالي كيفية استخدام الدالة [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) وإدراج النتائج التي تم توليدها في HTML:

### Node.js-إلى-LaTeX

```javascript
try 
{
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_equation.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

let sb = [
"<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n    <meta charset=\"UTF-8\">\r\n    <title>Title</title>\r\n    <script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML\"></script>\r\n    <script type=\"text/x-mathjax-config\">\r\n        MathJax.Hub.Config({\r\n\t    tex2jax: {\r\n\t        inlineMath: [['$','$'], ['\\\\(','\\\\)']],\r\n\t        processEscapes: true\r\n\t    }\r\n\t
```

## تصدير المعادلات كتعابير MathML

إذا كنت تريد تصدير المعادلات في Excel كتعابير MathML، يمكنك استخدام الدالة [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) 

يعرض الكود النموذجي التالي كيفية استخدام الدالة [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) وإدراج النتائج التي تم توليدها في HTML:

### Node.js-إلى-MathML

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dirPath = path.join(__dirname, "data");;
const filePath = path.join(dirPath, "Sample_equation.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

let sb = [];
sb.push("<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n    <meta charset=\"UTF-8\">\r\n    <title>Title</title>\r\n    <script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML\"></script>\r\n</head>\r\n<body>");

const shapes = workbook.getWorksheets().get(0).getShapes();
const textBox = shapes.get(0);
if (textBox instanceof AsposeCells.TextBox)
{
const mathNode = textBox.getEquationParagraph().getChild(0);
sb.push(mathNode.toMathML());
sb.push("</body>\r\n</html>");
}        

const fs = require("fs");
fs.writeFileSync("result.html", sb.join(""));
```


{{< app/cells/assistant language="nodejs-cpp" >}}
