---
title: Hitta namnet på rot elementet i XML karta med C++
linktitle: Hitta det rotelementnamn för XML karta
type: docs
weight: 30
url: /sv/cpp/find-the-root-element-name-of-xml-map/
description: Lär dig hur man hittar namnet på rot elementet i en XML karta med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan hitta *Rotelementets namn för Xml-karta* med hjälp av Aspose.Cells med [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) egenskap. Följande skärmbild visar rotens elementnamn för XML-kartan i Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Exempelkod**

Följande exempelkod laddar den [sample Excel-filen](55541789.xlsx) och får tillgång till den första XML-kartan och skriver ut dess [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) egenskap. Vänligen se konsolresultatet för provkoden nedan.

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

## **Konsoloutput**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
