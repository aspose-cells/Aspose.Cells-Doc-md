---
title: 使用 Node.js 通过 C++ 读取具有多种编码的 CSV 文件
linktitle: 使用多种编码方式读取CSV文件
type: docs
weight: 200
url: /zh/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 读取具有多种编码的 CSV 文件。
---


{{% alert color="primary" %}}

有时，你的 CSV 文件包含多种编码（Unicode、ANSI、UTF8、UTF7 等）。Aspose.Cells 允许你加载此类 CSV 文件并将其转换为其他格式，例如 PDF 或 XLSX。

{{% /alert %}}

Aspose.Cells 提供了 [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) 属性，你需要将其设置为 **true**，以正确加载多编码的CSV文件。

以下截图显示了一个包含两行的示例CSV文件。第一行是**ANSI**编码，第二行是**Unicode**编码

|**输入文件**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下截图显示了未将 [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) 属性设置为 **true** 的情况下，从上述CSV文件转换的XLSX文件。可以看到，Unicode文本没有正确转换。

|**输出文件1：未对多种编码进行处理**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下截图显示了在将上述 CSV 文件转换为 XLSX 文件后，将 [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) 属性设置为 **true**。可以看到，Unicode 文本现在被正确转换。

|**输出文件2：IsMultiEncoded设置为true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下是将上述 CSV 文件正确转换为 XLSX 格式的示例代码。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## 相关文章

- [打开 CSV 文件](/cells/zh/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="nodejs-cpp" >}}
