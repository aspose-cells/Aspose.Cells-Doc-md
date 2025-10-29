---
title: Настройка XML ленты с помощью C++
linktitle: Настроить меню Excel
type: docs
weight: 1500
url: /ru/cpp/customizing-the-ribbon-xml/
description: Научитесь настраивать XML ленты в файлах Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}} 

Microsoft Office заменил меню и панели инструментов на ленту в верхней части окна приложения с Office 2007. Лента настраиваема. 
Aspose.Cells позволяет вам:

- Сохранить Ribbon XML без его разбора,
- Читать и записывать Ribbon XML без его разбора,
- Получать и устанавливать данные Ribbon XML.

Если вы хотите изменить XML-ленту, вам нужно его проанализировать с помощью парсера XML или другого инструмента для работы с XML-лентой.

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
