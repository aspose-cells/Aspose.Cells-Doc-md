---
title: 在使用C++通过Node.js加载文件时自动调整行高
linktitle: 在加载文件时自动调整行高
type: docs
weight: 120
url: /zh/nodejs-cpp/autofit-row-height/
description: 学习如何在加载文件时自动调整未自定义高度的行，使用Aspose.Cells for Node.js via C++。
keywords: 加载文件时自动调整行高（Node.js通过C++），在打开Excel文件时自动调整行高。 
---

## **可能的使用场景**
行高会自动匹配内容的字体，但当缓存的行高与文件中的内容高度不一致时，MS Excel在加载文件时会自动调整行高，而Aspose.Cells for Node.js via C++不会为了提高性能自动调整。如果需要使用Aspose.Cells在加载文件时自动匹配行高，可以通过参数[setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-)实现。

请参考以下图片数据。可以观察到第11行的缓存行高为15，但Excel在加载文件时自动调整了行高。
<br>
<img src="1.png" width=70% />

## **使用Aspose.Cells for Node.js via C++调整行高**
如果直接加载文件并保存为PDF，数据可能无法全部显示在PDF中，因为其缓存行高仅为15。
<br>
<img src="2.png" width=70% />
<br>
如果在加载文件时将[setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-)参数设为true，Aspose.Cells会自动调整行高。调整后的行高可以有效满足文本显示需求。
<br>
<img src="3.png" width=70% />

## **Node.js示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
