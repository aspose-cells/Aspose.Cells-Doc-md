---
title: 用C++自定义带有Ribbon XML的Excel文件
linktitle: 自定义Excel菜单
type: docs
weight: 1500
url: /zh/cpp/customizing-the-ribbon-xml/
description: 学习如何使用C++和Aspose.Cells自定义Excel文件中的Ribbon XML。
---

{{% alert color="primary" %}} 

自2007 年版起，Microsoft Office 用 Ribbon 替代菜单栏和工具栏，并且 Ribbon 可以自定义。 
Aspose.Cells 允许你：

- 保留Ribbon XML而无需解析它，
- 读取和写入Ribbon XML而无需解析它，
- 获取和设置Ribbon XML数据。

如果要更改Ribbon XML，则必须使用XML解析器或其他Ribbon XML工具解析它。

{{% /alert %}} 

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb(srcDir + u"aspose-sample.xlsx");

    std::ifstream file((srcDir + u"CustomUI.xml").ToUtf8());
    if (!file.is_open())
    {
        std::cerr << "Failed to open CustomUI.xml" << std::endl;
        return -1;
    }

    std::string ribbonXml((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    std::u16string utf16Xml = converter.from_bytes(ribbonXml);
    U16String xmlStr(reinterpret_cast<const char16_t*>(utf16Xml.c_str()));

    wb.SetRibbonXml(xmlStr);

    std::cout << "Ribbon XML set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
