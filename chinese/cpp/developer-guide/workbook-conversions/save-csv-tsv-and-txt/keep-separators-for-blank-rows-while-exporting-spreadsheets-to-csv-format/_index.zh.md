---
title: 在将电子表格导出为CSV格式时，保持空白行的分隔符（使用C++）
linktitle: 在将电子表格导出为CSV格式时保留空行的分隔符
type: docs
weight: 160
url: /zh/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: 学习如何在使用Aspose.Cells与C++导出CSV格式时保持空白行的分隔符。
---

## **在将电子表格导出为CSV格式时保留空行的分隔符**

Aspose.Cells 提供在转换电子表格为CSV格式时保持行分隔符的能力。为此，你可以使用 [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/) 类的 [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) 属性。[**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) 是一个布尔属性。要在把Excel文件转换为CSV时保持空白行的分隔符，请将 [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) 属性设置为 **true**。

以下示例代码加载 [源Excel文件](84378743.xlsx)，将 [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) 属性设置为 **true** 并保存为 [output.csv](84378744.csv)。屏幕截图显示源Excel文件、转换成csv时生成的默认输出以及设置 [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) 为 **true** 时的输出的对比。

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(inputFilePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
    options.SetKeepSeparatorsForBlankRow(true);

    // Save the file with the options
    workbook.Save(outDir + u"output.csv", options);

    std::cout << "File saved successfully as output.csv!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
