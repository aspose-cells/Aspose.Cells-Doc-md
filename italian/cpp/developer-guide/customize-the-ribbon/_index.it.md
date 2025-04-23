---
title: Personalizzare l XML della barra multifunzione con C++
linktitle: Personalizzare il Menu di Excel
type: docs
weight: 1500
url: /it/cpp/customizing-the-ribbon-xml/
description: Impara come personalizzare l XML della barra multifunzione nei file Excel utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Microsoft Office ha sostituito i menu e le barre degli strumenti con una barra multifunzione nella parte superiore della finestra dell'applicazione dal 2007. La barra multifunzione è personalizzabile. 
Aspose.Cells ti permette di:

- Mantenere il Ribbon XML senza analizzarlo,
- Leggere e scrivere Ribbon XML senza analizzarlo,
- Ottenere e impostare i dati del Ribbon XML.

Se si desidera modificare il Ribbon XML, è necessario analizzarlo con un analizzatore XML o altro strumento Ribbon XML.

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
