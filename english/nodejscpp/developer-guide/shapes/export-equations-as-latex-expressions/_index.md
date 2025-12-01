---
title: How to export excel equations to other types of expressions
linktitle: export equation
type: docs
weight: 100
url: /nodejs-cpp/export-equation/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Sometimes you may need to export Excel formulas to other formats in your code to meet your work needs, then Aspose.Cells library can meet your needs. The following content introduces some methods on how to export Excel formulas to other formats, I hope these methods will be helpful to you.

We have prepared sample code here to help you achieve your goals using Aspose.Cells. Necessary sample files are also provided.

Sample file: [Sample.xlsx](Sample.xlsx)

## Export equations as LaTeX expressions

If you want to export equations in Excel as LaTeX expressions, you can use the [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) method. 

The following sample code shows how to use the [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) method and insert the generated results into HTML:

### Node.js-To-LaTeX

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

## Export equations as MathML expressions

If you want to export equations in Excel as MathML expressions, you can use the [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) method. 

The following sample code shows how to use the [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) method and insert the generated results into HTML:

### Node.js-To-MathML

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
