---
title: Collega celle agli elementi della mappa XML con C++
linktitle: Collega le celle agli elementi della mappa XML
type: docs
weight: 50
url: /it/cpp/link-cells-to-xml-map-elements/
description: Impara come collegare le celle agli elementi delle Maps XML usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

È possibile collegare le tue celle agli elementi della mappa XML utilizzando Aspose.Cells. Si prega di utilizzare il metodo [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) a questo scopo.

## **Collega le celle agli elementi della mappa XML**

Il seguente codice di esempio carica il [file Excel di origine](5115471.xlsx) che contiene la mappa XML e quindi collega le celle A1, B2, C3, D4, E5 e F6 agli elementi della mappa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 e FIELD8 rispettivamente e quindi salva il workbook in [file Excel di output](5115467.xlsx).

Se si apre il [file Excel di output](5115467.xlsx) e si fa clic sul pulsante Sviluppatore > Origine, si vedrà che le celle sono collegate agli elementi della mappa XML e saranno anche evidenziate da Microsoft Excel come mostrato in questa immagine.

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
