---
title: Lägg till ikoner i kalkblad med C++
linktitle: Hantera ikoner
type: docs
weight: 100
url: /sv/cpp/insert-svg-to-excel/
description: Lär dig hur du lägger till ikoner i Excel kalkblad med Aspose.Cells och C++.
---

## Lägg till ikoner i arbetsboken med hjälp av Aspose.Cells

Om du behöver använda [Aspose.Cells](https://products.aspose.com/cells/) för att lägga till 'ikoner' i en Excelfil, kan detta dokument ge dig hjälp.

Gränssnittet för Excel som motsvarar infogning av ikoner är följande:

![](1.png)

- Välj positionen för ikonen som ska infogas i arbetsboken
- Vänsterklicka på *Infoga*->*Ikoner*
- I fönstret som öppnas väljer du ikonen i rutan med röd ram i figuren ovan
- Vänsterklicka *Infoga*, den kommer att infogas i Excel-filen.

Effekten är följande:

![](2.png)

Här har vi förberett *exempelkod* för att hjälpa dig att infoga ikoner med [Aspose.Cells](https://products.aspose.com/cells/). Det finns också en nödvändig [exempelfil](sample.xlsx) och en ikon [resursfil](icon.zip). Vi använde Excel-gränssnittet för att infoga en ikon med samma visningseffekt som [resursfilen](icon.zip) i [exempelfilen](sample.xlsx).

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

När du utför ovanstående kod i ditt projekt kommer du att få följande resultat:

![](3.png)
