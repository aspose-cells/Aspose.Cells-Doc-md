---
title: 如何将 Excel 方程导出为其他类型的表达式
linktitle: 导出公式
type: docs
weight: 100
url: /zh/nodejs-cpp/export-equation/
---

有时，您可能需要在代码中将 Excel 公式导出为其他格式以满足工作需要，Aspose.Cells 库可以满足您的需求。以下内容介绍一些将 Excel 公式导出到其他格式的方法，希望对您有所帮助。

这里提供了示例代码，帮助您使用Aspose.Cells实现目标，同时也提供了必要的示例文件。

示例文件：[Sample.xlsx](Sample.xlsx)

## 将公式导出为LaTeX表达式

如果您想将Excel中的方程作为 LaTeX 表达式导出，可以使用 [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) 方法。 

以下示例代码演示如何使用 [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) 方法，并将生成的结果插入HTML：

### Node.js 到 LaTeX

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

## 将公式导出为MathML表达式

如果您想将 Excel 中的方程导出为 MathML 表达式，可以使用 [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) 方法。 

以下示例代码演示如何使用 [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) 方法，并将生成的结果插入HTML：

### Node.js 到 MathML

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


