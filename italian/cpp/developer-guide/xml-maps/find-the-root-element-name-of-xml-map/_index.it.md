---
title: Trova il nome dell elemento radice della mappa XML con C++
linktitle: Trova il nome dell elemento radice della mappa XML
type: docs
weight: 30
url: /it/cpp/find-the-root-element-name-of-xml-map/
description: Impara come trovare il nome dell elemento radice di una mappa XML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

È possibile trovare il *Nome dell'elemento radice della mappa XML* utilizzando Aspose.Cells con la proprietà [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). La seguente schermata mostra il nome dell'elemento radice della mappa XML in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Codice di Esempio**

Il seguente codice di esempio carica il [file Excel di esempio](55541789.xlsx) e accede alla prima mappa XML e stampa la proprietà [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). Si prega di vedere l'output della console del codice di esempio qui sotto.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
