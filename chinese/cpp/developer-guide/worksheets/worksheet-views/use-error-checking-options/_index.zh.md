---
title: 使用C++进行错误检查选项
linktitle: 使用错误检查选项
type: docs
weight: 140
url: /zh/cpp/use-error-checking-options/
description: 本文提供了示例代码，演示如何使用C++ API或库以程序化方式启用Excel工作表的错误检查选项，例如将数字作为文本存储。
keywords: 在Excel中以C++存储数字为文本，启用错误检测功能
---

{{% alert color="primary" %}}

Microsoft Excel允许用户定义错误检查选项和规则。当创建公式时，用户通常会看到错误检查，单元格右上角的小三角形突出显示当单元格存在问题时。Excel提供帮助用户纠正常见问题的信息。

{{% /alert %}}

## **错误类型**

表示公式无法返回结果的错误，比如通过零进行数字除法，需要立即关注并在单元格中显示错误值。单击绿色三角形显示一个感叹号，单击打开一个选项列表。

可以通过选项解决错误，也可以选择忽略错误。忽略错误意味着该错误在后续错误检查中不再显示。

Aspose.Cells提供了错误检查选项功能。[**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/)类管理不同类型的错误检查，例如以文本存储的数字、公式计算错误和验证错误。使用[**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/)枚举设置所需的错误检查。

## **作为文本存储的数字**

有时，数字可能被格式化并作为文本存储在单元格中。这可能会导致计算出现问题或产生令人困惑的排序顺序。格式为文本的数字在单元格中是左对齐而不是右对齐的。如果应执行单元格上的公式未返回值，则检查公式引用的单元格中的对齐方式 - 可能是其中一些或全部的单元格被格式为文本。

可以使用错误检查选项快速将作为文本存储的数字转换为实际数字。在Microsoft Excel 2003中：

1. 在“工具”菜单上，单击“选项”。
1. 选择“错误检查”选项卡。
   **将作为文本存储的数字** 选项默认为选中状态。
1. 取消其选中状态。

以下示例代码显示如何使用Aspose.Cells APIs在模板XLS文件中禁用工作表中的文本存储的数字错误检查选项。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
