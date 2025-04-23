---
title: 在使用 C++ 通过 Node.js 保存为 HTML 时启用 CSS 自定义属性
linktitle: 在保存为HTML时启用CSS自定义属性
type: docs
weight: 320
url: /zh/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: 学习如何在将 Excel 文件保存为 HTML 时启用 CSS 自定义属性，使用 Aspose.Cells for Node.js via C++。 
---

## **可能的使用场景**

当您将您的 Excel 文件保存为 HTML 时，对于存在多次出现的同一基础图片的场景，使用自定义属性可以仅保存一次图片数据，从而提升生成 HTML 的性能。请使用 [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) 属性并在保存为 HTML 时将其设置为 **true**。
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **在保存为HTML时启用CSS自定义属性**

以下示例代码展示了 [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) 属性的用法。截图显示了未将此属性设置为 **true** 时的效果。请下载此代码用的[示例 Excel 文件](50528260.xlsx) 和生成的[输出 HTML](50528261.zip) 以供参考。



## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
