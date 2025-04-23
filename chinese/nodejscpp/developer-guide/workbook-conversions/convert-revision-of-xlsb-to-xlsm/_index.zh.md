---  
title: 用 Node.js 通过 C++ 将 XLSB 文件的修订转换为 XLSM 格式  
linktitle: 将XLSB文件的修订版本转换为XLSM  
type: docs  
weight: 290  
url: /zh/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: 学习如何用 Aspose.Cells for Node.js via C++ 完整转换 XLSB 文件的修订为 XLSM 格式。  
---  

{{% alert color="primary" %}}  

Aspose.Cells 现支持完全将 XLSB 文件的修订转换为 XLSM 文件。修订存放在路径 \xl\revisions 内。将 XLSB 文件扩展名改为 ZIP 后可查看这些修订。\xl\revisions 路径内包含以 .bin 结尾的文件。  

当你使用 Aspose.Cells 将 XLSB 文件转换为 XLSM 文件时，这些 .bin 文件会成功转换为 .xml 文件，效果如这两张截图所示。  

{{% /alert %}}  

以下代码示例演示如何使用 Aspose.Cells for Node.js via C++ 将 XLSB 文件转换为 XLSM 格式。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

