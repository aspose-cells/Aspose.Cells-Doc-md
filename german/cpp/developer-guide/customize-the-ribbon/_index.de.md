---
title: Anpassen des Ribbon XML mit C++
linktitle: Excel Menü anpassen
type: docs
weight: 1500
url: /de/cpp/customizing-the-ribbon-xml/
description: Erfahren, wie man das Ribbon XML in Excel Dateien mit Aspose.Cells und C++ anpasst.
---

{{% alert color="primary" %}} 

Microsoft Office hat Menüleisten und Symbolleisten seit Office 2007 durch das Ribbon ersetzt, das oben im Anwendungsfenster erscheint. Das Ribbon ist anpassbar. 
Aspose.Cells ermöglicht es Ihnen, zu:

- Ribbon-XML ohne Analyse beizubehalten,
- Ribbon-XML ohne Analyse zu lesen und zu schreiben,
- Ribbon-XML-Daten zu erhalten und zu setzen.

Wenn Sie das Ribbon-XML ändern möchten, müssen Sie es mit einem XML-Parser oder einem anderen Ribbon-XML-Tool analysieren.

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
