---
title: Personnaliser le XML du ruban avec C++
linktitle: Personnaliser le menu Excel
type: docs
weight: 1500
url: /fr/cpp/customizing-the-ribbon-xml/
description: Apprenez comment personnaliser le XML du ruban dans les fichiers Excel avec Aspose.Cells en utilisant C++.
---

{{% alert color="primary" %}} 

Microsoft Office a remplacé les menus et barres d'outils par un ruban en haut de la fenêtre de l'application depuis Office 2007. Le ruban est personnalisable. 
Aspose.Cells vous permet de :

- Conserver Ribbon XML sans l'analyser,
- Lire et écrire Ribbon XML sans l'analyser,
- Obtenir et définir les données de Ribbon XML.

Si vous souhaitez modifier le Ribbon XML, vous devez l'analyser avec un analyseur XML ou un autre outil Ribbon XML.

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
