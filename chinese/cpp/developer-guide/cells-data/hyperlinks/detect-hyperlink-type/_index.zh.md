---
title: 使用C++检测超链接类型
linktitle: 检测超链接类型
type: docs
weight: 160
url: /zh/cpp/detect-hyperlink-type/
description: 通过Aspose.Cells for C++ API学习如何检测超链接类型。
keywords: 检测超链接类型，检测超链接的类型，获取超链接的类型
---

## **检测超链接类型**

Excel文件可以有不同类型的超链接，例如外部链接、单元格引用、文件路径等。Aspose.Cells支持检测超链接类型的功能。超链接的类型由[**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)枚举表示。[**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)枚举具有以下成员。

- 外部：外部链接
- 文件路径：文件/文件夹的本地和完整路径。
- 电子邮件：邮件
- 单元格引用：链接到单元格或命名范围。

要检查超链接的类型，[**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) 类提供了一个返回类型为 [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) 的 [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) 属性。以下代码片段演示了如何使用 [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) 属性，通过使用此[source excel file](94896195.xlsx)。

### 源代码

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

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

以下是上述代码片段生成的输出。

### 控制台输出
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
