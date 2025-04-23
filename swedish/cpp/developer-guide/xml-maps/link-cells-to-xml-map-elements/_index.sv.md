---
title: Länka celler till XML kartans element med C++
linktitle: Länka celler till XML kartelement
type: docs
weight: 50
url: /sv/cpp/link-cells-to-xml-map-elements/
description: Lär dig hur man länkar celler till XML kartans element med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Du kan länka dina celler till XML-kartelement med Aspose.Cells. Använd [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) metoden för detta ändamål.

## **Länka celler till Xml-kartelement**

Följande exempelkod laddar den [käll-excel-filen](5115471.xlsx) som innehåller XML-karta och länkar sedan celler A1, B2, C3, D4, E5 och F6 till XML-kartelementen FIELD1, FIELD2, FIELD4, FIELD5 och FIELD7 respektive och sparar sedan arbetsboken som [utdata-excelfil](5115467.xlsx).

Om du öppnar [utdata excel-filen](5115467.xlsx) och klickar på Developer > Source-knappen, kommer du att se att cellerna är länkade med XML-kartelement och de kommer också att markeras av Microsoft Excel som visas på bilden.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample workbook
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the Xml Map inside it
    XmlMap map = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Map FIELD1 and FIELD2 to cell A1 and B2
    ws.GetCells().LinkToXmlMap(map.GetName(), 0, 0, u"/root/row/FIELD1");
    ws.GetCells().LinkToXmlMap(map.GetName(), 1, 1, u"/root/row/FIELD2");

    // Map FIELD4 and FIELD5 to cell C3 and D4
    ws.GetCells().LinkToXmlMap(map.GetName(), 2, 2, u"/root/row/FIELD4");
    ws.GetCells().LinkToXmlMap(map.GetName(), 3, 3, u"/root/row/FIELD5");

    // Map FIELD7 and FIELD8 to cell E5 and F6
    ws.GetCells().LinkToXmlMap(map.GetName(), 4, 4, u"/root/row/FIELD7");
    ws.GetCells().LinkToXmlMap(map.GetName(), 5, 5, u"/root/row/FIELD8");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
