---
title: Excelから数式を他のタイプにエクスポートする方法
linktitle: 数式をエクスポート
type: docs
weight: 100
url: /ja/nodejs-cpp/export-equation/
---

Excelの数式を他の形式にエクスポートする必要がある場合や、作業ニーズに応じてAspose.Cellsライブラリが役立ちます。以下の内容では、Excelの数式を他の形式にエクスポートする方法についていくつかの方法を紹介します。これらの方法が役立つことを願っています。

Aspose.Cellsを使用して目標を達成するためのサンプルコードを準備しています。必要なサンプルファイルも提供します。

サンプルファイル：[Sample.xlsx](Sample.xlsx)

## 数式をLaTeX表現としてエクスポート

Excelの式をLaTeX形式としてエクスポートしたい場合は、[EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--)メソッドを使用できます。 

以下のサンプルコードは、[EquationNode.toLaTeX()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toLaTeX--)メソッドの使い方と生成された結果をHTMLに挿入する方法を示しています。

### Node.js-用-LaTeX

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

## 数式をMathML表現としてエクスポート

Excelの式をMathML形式としてエクスポートしたい場合は、[EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--)メソッドを使用できます。 

以下のサンプルコードは、[EquationNode.toMathML()](https://reference.aspose.com/cells/nodejs-cpp/equationnode/#toMathML--)メソッドの使い方と、生成した結果をHTMLに挿入する方法を示しています。

### Node.js-用-MathML

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
