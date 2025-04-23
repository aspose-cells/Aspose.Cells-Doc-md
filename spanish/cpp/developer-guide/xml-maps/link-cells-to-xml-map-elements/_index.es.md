---
title: Vincular celdas a elementos de mapas XML con C++
linktitle: Vincular celdas a elementos del mapa XML
type: docs
weight: 50
url: /es/cpp/link-cells-to-xml-map-elements/
description: Aprenda cómo vincular celdas a elementos de mapas XML usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Puede vincular sus celdas a elementos de mapa XML utilizando Aspose.Cells. Utilice el método [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) para este propósito.

## **Vincular celdas a elementos de mapa Xml**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115471.xlsx) que contiene un mapa XML y luego vincula las celdas A1, B2, C3, D4, E5 y F6 a los elementos de mapa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 y FIELD8 respectivamente, y luego guarda el libro de trabajo en el [archivo de Excel de salida](5115467.xlsx).

Si abre el [archivo de Excel de salida](5115467.xlsx) y hace clic en el botón Desarrollador > Origen, verá que las celdas están vinculadas con elementos de mapa XML y también serán resaltadas por Microsoft Excel como se muestra en esta imagen.

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
