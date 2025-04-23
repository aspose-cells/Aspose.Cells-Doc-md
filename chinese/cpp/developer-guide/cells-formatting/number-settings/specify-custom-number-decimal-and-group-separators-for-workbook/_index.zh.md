---
title: 用C++指定工作簿的自定义数字小数点和组分隔符
linktitle: 指定自定义数字小数点和组分隔符
type: docs
weight: 110
url: /zh/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 通过使用Aspose.Cells for C++ API，在MS Excel中和用C++代码修改数字的十进制和分组分隔符。
keywords: 指定自定义小数点分隔符Excel，指定自定义小数点分隔符Excel C++，指定自定义组分隔符Excel，指定自定义组分隔符Excel C++，指定自定义十进制和组分隔符Excel，指定自定义十进制和组分隔符Excel C++，更改Excel的十进制和分组分隔符，更改十进制和分组分隔符Excel，更改十进制分隔符Excel，更改十进制分隔符Excel C++，更改组分隔符Excel，更改组分隔符Excel C++
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在“高级Excel选项”中指定自定义十进制和千位分隔符，而不是使用系统分隔符，如下面的屏幕截图所示。

Aspose.Cells提供[**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/)和[**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/)属性，以设置数字的自定义分隔符进行格式化/解析。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

下面的屏幕截图显示了“高级Excel选项”，并突出显示了指定“自定义分隔符”的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用Aspose.Cells指定自定义分隔符**

下面的示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。它将十进制和组分隔符分别指定为点和空格。

### 用C++指定自定义数字的小数点和分组分隔符的代码

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

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
