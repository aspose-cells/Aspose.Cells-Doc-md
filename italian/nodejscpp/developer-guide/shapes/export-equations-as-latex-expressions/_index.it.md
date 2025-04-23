---
title: Come esportare le equazioni di Excel in altri tipi di espressioni
linktitle: esporta equazione
type: docs
weight: 100
url: /it/nodejs-cpp/export-equation/
---

A volte, potresti aver bisogno di esportare le formule di Excel in altri formati nel tuo codice per soddisfare le esigenze del lavoro, quindi la libreria Aspose.Cells può soddisfare le tue necessità. Il contenuto seguente introduce alcuni metodi su come esportare le formule di Excel in altri formati, spero che questi metodi ti saranno utili.

Abbiamo preparato un esempio di codice qui per aiutarti a raggiungere i tuoi obiettivi usando Aspose.Cells. Sono anche forniti i file di esempio necessari.

File di esempio: [Sample.xlsx](Sample.xlsx)

## Esportare equazioni come espressioni LaTeX

Se vuoi esportare le equazioni di Excel come espressioni LaTeX, puoi usare il metodo [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--). 

Il codice di esempio seguente mostra come usare il metodo [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) e inserire i risultati generati in HTML:

### Node.js-Alla-LaTeX

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

## Esportare equazioni come espressioni MathML

Se vuoi esportare le equazioni di Excel come espressioni MathML, puoi usare il metodo [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--). 

Il codice di esempio seguente mostra come usare il metodo [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) e inserire i risultati generati in HTML:

### Node.js-Alla-MathML

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


