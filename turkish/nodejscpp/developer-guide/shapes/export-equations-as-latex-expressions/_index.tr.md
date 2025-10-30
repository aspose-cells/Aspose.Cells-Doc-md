---
title: Excel de formülleri diğer ifade türlerine nasıl dışa aktarabilirsiniz
linktitle: eksen denklem export et
type: docs
weight: 100
url: /tr/nodejs-cpp/export-equation/
---

Bazen, iş ihtiyaçlarınızı karşılamak amacıyla kodunuzda Excel formüllerini diğer biçimlere dışa aktarmanız gerekebilir, bu durumda Aspose.Cells kütüphanesi ihtiyaçlarınızı karşılayabilir. Aşağıdaki içerik, Excel formüllerini diğer biçimlere nasıl dışa aktaracağınızı gösteren bazı yöntemleri tanıtmaktadır, umarım bu yöntemler size faydalı olur.

Burada Aspose.Cells kullanarak hedeflerinize ulaşmanıza yardımcı olacak örnek kodlar hazırlanmıştır. Gerekli örnek dosyalar da sağlanmıştır.

Örnek dosya: [Sample.xlsx](Sample.xlsx)

## Denklemleri LaTeX ifadeleri olarak dışa aktarma

Excel'de denklemleri LaTeX ifadeleri olarak dışa aktarmak istiyorsanız, [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) yöntemini kullanabilirsiniz. 

Aşağıdaki örnek kod, [EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--) yöntemini nasıl kullanacağınızı ve oluşturulan sonuçları HTML’ye nasıl ekleyeceğinizi gösterir:

### Node.js-Tan-LaTeX

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

## Denklemleri MathML ifadeleri olarak dışa aktarma

Excel'de denklemleri MathML ifadeleri olarak dışa aktarmak istiyorsanız, [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) yöntemini kullanabilirsiniz. 

Aşağıdaki örnek kod, [EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--) yöntemini nasıl kullanacağınızı ve oluşturulan sonuçları HTML’ye nasıl ekleyeceğinizi gösterir:

### Node.js-Tan-MathML

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
