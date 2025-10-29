---
title: 如何使用Node.js通过C++将HTML转换为PDF
linktitle: 如何将 HTML 转换为 PDF
type: docs
weight: 80
url: /zh/nodejs-cpp/convert-html-to-pdf/
description: 本主题向你展示如何使用Aspose.Cells for Node.js via C++将HTML转换为PDF和MHTML转换为PDF。
keywords: 通过Node.js用C++将HTML转换为PDF和MHTML的教程 
---

## **概述**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>将 HTML 转换为 PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML转PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript 转换 HTML 为 PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript 如何将 HTML 转换为 PDF</a></li>
</ul>

## **Node.js 中的 HTML 转 PDF 转换**
如何将 HTML 转换为 PDF？使用 [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) 库，您可以轻松用几行代码实现 HTML 转 PDF 转换。Aspose.Cells for Node.js via C++ 能够构建跨平台应用，具有生成、修改、转换、渲染和打印所有 Excel 文件的能力。

## **JavaScript 转换 HTML 为 PDF**
以下 JavaScript 代码示例展示了如何使用 [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) 将 HTML 文档转换为 PDF。

1. 创建 [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/) 类的实例。
1. 初始化 [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) 对象。
1. 通过调用Workbook.save()方法保存输出PDF文档。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.html");

// Loads the workbook which contains hidden external links
const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
const book = new AsposeCells.Workbook(filePath, options);
book.save("out.pdf");
```

## **尝试在线将HTML转换为PDF**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML转PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
{{< app/cells/assistant language="nodejs-cpp" >}}
