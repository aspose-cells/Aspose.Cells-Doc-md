---
title: Lier les cellules aux éléments de la cartographie XML avec C++
linktitle: Lier les cellules aux éléments de la carte XML
type: docs
weight: 50
url: /fr/cpp/link-cells-to-xml-map-elements/
description: Apprenez comment lier des cellules aux éléments de la cartographie XML en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez lier vos cellules aux éléments de la carte XML en utilisant Aspose.Cells. Veuillez utiliser la méthode [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) à cette fin.

## **Lier des cellules aux éléments de la carte Xml**

Le code d'exemple suivant charge le [fichier Excel source](5115471.xlsx) qui contient une carte XML, puis lie les cellules A1, B2, C3, D4, E5 et F6 aux éléments de la carte XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 et FIELD8 respectivement, puis enregistre le classeur dans le [fichier Excel de sortie](5115467.xlsx).

Si vous ouvrez le [fichier Excel de sortie](5115467.xlsx) et cliquez sur le bouton Développeur > Source, vous verrez que les cellules sont liées aux éléments de la carte XML et seront également mises en évidence par Microsoft Excel comme montré dans cette image.

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
{{< app/cells/assistant language="cpp" >}}
