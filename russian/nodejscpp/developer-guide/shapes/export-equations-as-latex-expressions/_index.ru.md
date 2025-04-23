---
title: Как экспортировать формулы Excel в другие форматы выражений
linktitle: экспорт уравнения
type: docs
weight: 100
url: /ru/nodejs-cpp/export-equation/
---

Иногда вам нужно экспортировать формулы Excel в другие форматы в коде для удовлетворения своих рабочих потребностей, тогда библиотека Aspose.Cells сможет помочь. Ниже представлены методы по экспорту формул Excel в другие форматы, надеюсь, эти методы будут полезны для вас.

Мы подготовили пример кода, который поможет вам достичь целей с помощью Aspose.Cells. Также предоставлены необходимые примерные файлы.

Образец файла: [Sample.xlsx](Sample.xlsx)

## Экспорт уравнений как LaTeX выражений

Если вы хотите экспортировать уравнения из Excel в виде выражений LaTeX, используйте метод [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--). 

Пример ниже показывает, как использовать метод [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) и вставить полученные результаты в HTML:

### Node.js - В-LaTeX

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

## Экспорт уравнений как MathML выражений

Если вы хотите экспортировать уравнения из Excel в виде MathML, используйте метод [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--). 

Пример ниже показывает, как использовать метод [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) и вставить полученные результаты в HTML:

### Node.js - В-MathML

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


