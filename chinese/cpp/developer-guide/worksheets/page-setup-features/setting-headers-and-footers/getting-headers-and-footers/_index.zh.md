---
title: 使用 C++ 获取页眉或页脚
linktitle: 获取页眉或页脚
type: docs
weight: 30
url: /zh/cpp/get-headers-or-footers/
description: 本文介绍如何使用 C++ API 或库以编程方式获取Excel或OpenOffice文件中的页眉和页脚。
---

{{% alert color="primary" %}}

页眉和页脚只出现在页面布局视图、打印预览和打印页面上。 

如果要同时查看多个工作表的页眉或页脚，也可以使用页面设置对话框。 

对于其他工作表类型，如图表工作表或图表，只能通过使用页面设置对话框来插入页眉和页脚。

{{% /alert %}}

## **在MS Excel中获取页眉和页脚**
1. 单击要查看或更改页眉或页脚的工作表。
2. 在“视图”选项卡的“工作簿视图”组中，点击“页面布局”。
  Excel会以页面布局视图显示工作表。
3. 要查看或编辑页眉或页脚，请单击工作表页面顶部或底部的左侧、中间或右侧页眉或页脚文本框（在页眉下方或在页脚上方）。


## **使用 Aspose.Cells for C++ 获取页眉和页脚**
使用 [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) 和 [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/) 方法，C++ 开发者可以轻松获取文件中的页眉和页脚。

1.构建工作簿以打开文件。
2. 获取要从中获取页眉或页脚的工作表。
3. 获取具有特定部分ID的页眉或页脚。

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **解析页眉和页脚为命令列表**
页眉或页脚文本可以包含特殊命令，例如页码的占位符，当前日期或文本格式属性。

特殊命令由带有前导“&”的单个字母表示。

标题和页脚字符串采用 ABNF 语法构建。不使用查看器很难理解。

Aspose.Cells for C++ 提供 [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) 方法来解析标题和页脚为命令列表。

以下代码显示了如何将标题或页脚解析为命令列表并处理命令：

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
