---
title: Zellen mit Elementen der XML Karte verknüpfen mit C++
linktitle: Zellen mit XML Map Elementen verknüpfen
type: docs
weight: 50
url: /de/cpp/link-cells-to-xml-map-elements/
description: Lernen Sie, wie Sie Zellen mit Elementen der XML Karte mithilfe von Aspose.Cells mit C++ verknüpfen.
---

## **Mögliche Verwendungsszenarien**

Sie können Ihre Zellen mit XML-Map-Elementen mit Aspose.Cells verknüpfen. Bitte verwenden Sie die Methode [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) für diesen Zweck.

## **Zellen mit Xml-Map-Elementen verknüpfen**

Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115471.xlsx), die eine XML-Map enthält, und verknüpft dann die Zellen A1, B2, C3, D4, E5 und F6 mit den XML-Map-Elementen FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 und FIELD8 und speichert anschließend die Arbeitsmappe in der [Ausgabe-Excel-Datei](5115467.xlsx).

Wenn Sie die [Ausgabe-Excel-Datei](5115467.xlsx) öffnen und auf die Schaltfläche Entwickler > Quelle klicken, sehen Sie, dass die Zellen mit XML-Map-Elementen verknüpft sind und sie auch von Microsoft Excel hervorgehoben werden, wie in diesem Bild gezeigt.

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
