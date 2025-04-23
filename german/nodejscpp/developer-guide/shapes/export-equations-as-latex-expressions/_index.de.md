---
title: So exportieren Sie Excel Formeln in andere Ausdrucksformen
linktitle: Gleichung exportieren
type: docs
weight: 100
url: /de/nodejs-cpp/export-equation/
---

Manchmal müssen Sie Excel-Formeln in Ihrem Code in andere Formate exportieren, um Ihren Arbeitsanforderungen gerecht zu werden. Die Aspose.Cells-Bibliothek kann Ihre Anforderungen erfüllen. Der folgende Inhalt stellt einige Methoden vor, wie man Excel-Formeln in andere Formate exportiert. Ich hoffe, diese Methoden sind für Sie hilfreich.

Wir haben Beispielcode vorbereitet, um Ihnen bei der Erreichung Ihrer Ziele mit Aspose.Cells zu helfen. Notwendige Beispieldateien sind ebenfalls bereitgestellt.

Beispiel-Datei: [Sample.xlsx](Sample.xlsx)

## Gleichungen als LaTeX-Ausdrücke exportieren

Wenn Sie Excel-Gleichungen als LaTeX-Ausdrücke exportieren möchten, können Sie die Methode [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) verwenden. 

Der folgende Beispielcode zeigt, wie man die Methode [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) verwendet und die generierten Ergebnisse in HTML einfügt:

### Node.js-Zu-LaTeX

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

## Gleichungen als MathML-Ausdrücke exportieren

Wenn Sie Excel-Gleichungen als MathML-Ausdrücke exportieren möchten, können Sie die Methode [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) verwenden. 

Der folgende Beispielcode zeigt, wie man die Methode [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) verwendet und die generierten Ergebnisse in HTML einfügt:

### Node.js-zu-MathML

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


