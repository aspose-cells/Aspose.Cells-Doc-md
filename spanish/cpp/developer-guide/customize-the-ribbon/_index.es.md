---
title: Personalización del XML de la Cinta con C++
linktitle: Personalizar el menú de Excel
type: docs
weight: 1500
url: /es/cpp/customizing-the-ribbon-xml/
description: Aprenda cómo personalizar el XML de la Cinta en archivos de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Microsoft Office reemplazó menús y barras de herramientas con una Cinta en la parte superior de la ventana de la aplicación desde Office 2007. La Cinta es personalizable. 
Aspose.Cells te permite:

- Mantener el XML de la cinta sin analizarlo,
- Leer y escribir el XML de la cinta sin analizarlo,
- Obtener y establecer datos XML de la cinta.

Si desea cambiar el XML de la cinta, debe analizarlo con un analizador XML u otra herramienta XML de la cinta.

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
