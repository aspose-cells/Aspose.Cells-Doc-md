---
title: Comment exporter des équations Excel vers d autres types d expressions
linktitle: exporter une équation
type: docs
weight: 100
url: /fr/nodejs-cpp/export-equation/
---

Parfois, vous pouvez avoir besoin d’exporter les formules Excel vers d’autres formats dans votre code pour répondre à vos besoins professionnels, alors la bibliothèque Aspose.Cells peut répondre à vos besoins. Le contenu suivant présente quelques méthodes pour exporter des formules Excel vers d’autres formats, j’espère que ces méthodes vous seront utiles.

Nous avons préparé un code d'exemple ici pour vous aider à atteindre vos objectifs en utilisant Aspose.Cells. Les fichiers d'échantillon nécessaires sont également fournis.

Fichier d'exemple : [Sample.xlsx](Sample.xlsx)

## Exporter des équations en expressions LaTeX

Si vous souhaitez exporter des équations dans Excel en tant qu’expressions LaTeX, vous pouvez utiliser la méthode [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--). 

Le code d’exemple suivant montre comment utiliser la méthode [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) et insérer les résultats générés dans HTML :

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

## Exporter des équations en expressions MathML

Si vous souhaitez exporter des équations dans Excel en tant qu’expressions MathML, vous pouvez utiliser la méthode [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--). 

Le code d’exemple suivant montre comment utiliser la méthode [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) et insérer les résultats générés dans HTML :

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


