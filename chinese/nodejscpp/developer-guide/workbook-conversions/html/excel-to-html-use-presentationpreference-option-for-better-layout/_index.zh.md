---
title: Excel 转 HTML  使用 PresentationPreference 选项优化布局，配合 C++ 通过 Node.js
linktitle: 将Excel转换为HTML  使用PresentationPreference选项以获得更好的布局
type: docs
weight: 220
url: /zh/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells 提供了一个有用的 HtmlSaveOptions.presentationPreference 属性，供开发者在将 Microsoft Excel 文件保存为 HTML 或 MHT 格式时渲染更好的布局。该属性的默认值为 false。建议将其设置为 true，以获得更吸引人的 Excel 报表展示效果。

{{% /alert %}} 

请查看下面的示例代码，演示如何根据展示偏好渲染Excel报告中的HTML文件。



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
