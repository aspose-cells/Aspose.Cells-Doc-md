---
title: Den Wurzelelementnamen der XML Karte mit C++ finden
linktitle: Ermitteln Sie den Root Elementnamen der XML Map
type: docs
weight: 30
url: /de/cpp/find-the-root-element-name-of-xml-map/
description: Lernen Sie, wie Sie den Namen des Wurzelelements einer XML Karte mit Aspose.Cells for C++ finden.
---

## **Mögliche Verwendungsszenarien**

Sie können den *Root-Elementnamen der Xml-Map* mit Aspose.Cells und der Eigenschaft [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) finden. Der folgende Screenshot zeigt den Root-Elementnamen der XML-Map in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Beispielcode**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](55541789.xlsx) und greift auf die erste XML-Map zu und gibt ihre [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/)-Eigenschaft aus. Bitte beachten Sie die Ausgabe in der Konsole des folgenden Beispielcodes.

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

## **Konsolenausgabe**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
