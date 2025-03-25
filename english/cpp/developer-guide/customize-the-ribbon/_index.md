---
title: Customizing the Ribbon XML with C++
linktitle: Customize Excel Menu
type: docs
weight: 1500
url: /cpp/customizing-the-ribbon-xml/
description: Learn how to customize the Ribbon XML in Excel files using Aspose.Cells with C++.
---

{{% alert color="primary" %}} 

Microsoft Office replaced menus and toolbars with a Ribbon at the top of the application window since Office 2007. The Ribbon is customizable. 
Aspose.Cells allows you to:

- Keep Ribbon XML without parsing it,
- Read and write Ribbon XML without parsing it,
- Get and set Ribbon XML data.

If you want to change the Ribbon XML, you have to parse it with an XML parser or other Ribbon XML tool.

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