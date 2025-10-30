---
title: Cómo exportar ecuaciones de Excel a otros tipos de expresiones
linktitle: exportar ecuación
type: docs
weight: 100
url: /es/nodejs-cpp/export-equation/
---

A veces, es posible que necesites exportar fórmulas de Excel a otros formatos en tu código para cumplir con tus necesidades laborales, entonces la biblioteca Aspose.Cells puede satisfacer tus necesidades. El contenido siguiente introduce algunos métodos sobre cómo exportar fórmulas de Excel a otros formatos, espero que estos métodos te sean útiles.

Aquí hemos preparado un código de ejemplo para ayudarte a lograr tus objetivos usando Aspose.Cells. También se proporcionan los archivos de muestra necesarios.

Archivo de ejemplo: [Sample.xlsx](Sample.xlsx)

## Exportar ecuaciones como expresiones LaTeX

Si desea exportar ecuaciones en Excel como expresiones LaTeX, puede usar el método [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--). 

El siguiente código de ejemplo muestra cómo usar el método [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) e insertar los resultados generados en HTML:

### Node.js-A-LaTeX

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

## Exportar ecuaciones como expresiones MathML

Si desea exportar ecuaciones en Excel como expresiones MathML, puede usar el método [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--). 

El siguiente código de ejemplo muestra cómo usar el método [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) e insertar los resultados generados en HTML:

### Node.js-A-MathML

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
