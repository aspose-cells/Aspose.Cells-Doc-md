---
title: Icons zum Arbeitsblatt mit C++ hinzufügen
linktitle: Symbole verwalten
type: docs
weight: 100
url: /de/cpp/insert-svg-to-excel/
description: Erfahren Sie, wie Sie mit Aspose.Cells in C++ Icons zu Excel Arbeitsblättern hinzufügen.
---

## Symbole zum Arbeitsblatt in Aspose.Cells hinzufügen

Wenn Sie [Aspose.Cells](https://products.aspose.com/cells/) verwenden müssen, um 'Symbole' in eine Excel-Datei hinzuzufügen, kann Ihnen dieses Dokument einige Hilfe bieten.

Die Excel-Benutzeroberfläche für die Einfüge-Symbol-Operation sieht wie folgt aus:

![](1.png)

- Wählen Sie die Position des Symbols, das in das Arbeitsblatt eingefügt werden soll
- Klicken Sie links auf *Einfügen*->*Symbole*
- In dem sich öffnenden Fenster wählen Sie das Symbol im roten Rechteck in der obigen Abbildung aus
- Linksklick *Einfügen*, es wird in die Excel-Datei eingefügt.

Der Effekt ist wie folgt:

![](2.png)

Hier haben wir *Beispiellcode* vorbereitet, um Ihnen beim Einfügen von Symbolen mit [Aspose.Cells](https://products.aspose.com/cells/) zu helfen. Es gibt auch eine notwendige [Beispiel-Datei](sample.xlsx) und eine Symbol [Ressourcendatei](icon.zip). Wir haben die Excel-Oberfläche benutzt, um ein Symbol mit dem gleichen Anzeigeeffekt wie die [Ressourcendatei](icon.zip) in der [Beispiel-Datei](sample.xlsx) einzufügen.

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Wenn Sie den obigen Code in Ihrem Projekt ausführen, erhalten Sie die folgenden Ergebnisse:

![](3.png)
{{< app/cells/assistant language="cpp" >}}
