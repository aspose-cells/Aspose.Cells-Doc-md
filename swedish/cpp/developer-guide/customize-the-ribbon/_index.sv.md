---
title: Anpassa Ribbon XML med C++
linktitle: Anpassa Excel meny
type: docs
weight: 1500
url: /sv/cpp/customizing-the-ribbon-xml/
description: Lär dig att anpassa Ribbon XML i Excel filer med hjälp av Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

Microsoft Office ersatte menyer och verktygsfält med en Band som finns högst upp i applikationsfönstret sedan Office 2007. Ribbon är anpassningsbar. 
Aspose.Cells tillåter dig att:

- Behåll Ribbon XML utan att analysera det,
- Läs och skriv Ribbon XML utan att analysera det,
- Hämta och ange Ribbon XML-data.

Om du vill ändra Ribbon XML måste du analysera den med en XML-parser eller annat Ribbon XML-verktyg.

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
{{< app/cells/assistant language="cpp" >}}
