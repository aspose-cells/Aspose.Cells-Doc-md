---
title: 使用C++读取具有多种编码的CSV文件
linktitle: 使用多种编码方式读取CSV文件
type: docs
weight: 200
url: /zh/cpp/reading-csv-file-with-multiple-encodings/
description: 学习如何使用 Aspose.Cells for C++ 读取具有多种编码的CSV文件。
---

{{% alert color="primary" %}}

有时，你的CSV文件包含多种编码（Unicode、ANSI、UTF8、UTF7等）。Aspose.Cells 允许你加载此类CSV文件并将其转换为其他格式，例如PDF或XLSX。

{{% /alert %}}

Aspose.Cells 提供了 [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) 属性，你需要将其设置为 **true**，以正确加载多编码的CSV文件。

以下截图显示了一个包含两行的示例CSV文件。第一行为 **ANSI** 编码，第二行为 **Unicode** 编码。

|**输入文件**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下截图显示了未将 [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) 属性设置为 **true** 的情况下，从上述CSV文件转换的XLSX文件。可以看到，Unicode文本没有正确转换。

|**输出文件1：未对多种编码进行处理**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

设置 [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) 属性为 **true** 后，从上述CSV文件转换的XLSX文件已正确转换Unicode文本。

|**输出文件2：IsMultiEncoded设置为true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下是将上述 CSV 文件正确转换为 XLSX 格式的示例代码。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"MultiEncoded.csv";

    // Create TxtLoadOptions and set MultiEncoded property to true
    TxtLoadOptions options;
    options.SetIsMultiEncoded(true);

    // Load the CSV file into Workbook with the specified options
    Workbook workbook(filePath, options);

    // Save the workbook in XLSX format
    workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 相关文章

- [打开 CSV 文件](/cells/zh/cpp/opening-files-with-different-formats/#opening-csv-files)
