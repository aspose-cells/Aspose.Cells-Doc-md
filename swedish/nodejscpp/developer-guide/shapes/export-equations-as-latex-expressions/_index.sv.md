---
title: Hur man exporterar Excel ekvationer till andra typer av uttryck
linktitle: exportera ekvationsuttryck
type: docs
weight: 100
url: /sv/nodejs-cpp/export-equation/
---

Ibland kan du behöva exportera Excel-formler till andra format i din kod för att möta dina arbetsbehov, då kan Aspose.Cells-biblioteket möta dina behov. Följande innehåll introducerar några metoder för hur man exporterar Excel-formler till andra format, jag hoppas att dessa metoder kommer att vara till hjälp för dig.

Vi har förberett exempel på kod här för att hjälpa dig att uppnå dina mål med Aspose.Cells. Nödvändiga exempeldata finns också tillgängliga.

Exempelfil: [Sample.xlsx](Sample.xlsx)

## Exportera ekvationer som LaTeX-uttryck

Om du vill exportera ekvationer i Excel som LaTeX-uttryck kan du använda [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) metoden. 

Följande exempel visar hur du använder [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) metoden och infogar de genererade resultaten i HTML:

### Node.js-Till-LaTeX

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

## Exportera ekvationer som MathML-uttryck

Om du vill exportera ekvationer i Excel som MathML-uttryck kan du använda [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) metoden. 

Följande exempel visar hur du använder [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) metoden och infogar de genererade resultaten i HTML:

### Node.js-Till-MathML

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


