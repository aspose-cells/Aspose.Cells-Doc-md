---
title: Exportiere XML Daten, die mit XML Karten im Arbeitsbuch verbunden sind, mit C++
linktitle: Exportieren von XML Daten, die mit der XML Map innerhalb der Arbeitsmappe verknüpft sind
type: docs
weight: 20
url: /de/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Lernen Sie, wie Sie XML Daten, die mit XML Karten in Ihrem Arbeitsbuch verbunden sind, mithilfe von Aspose.Cells for C++ exportieren.
---

## **Exportieren Sie XML-Daten, die mit der XML-Map in der Arbeitsmappe verknüpft sind**

Bitte verwenden Sie die [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/)-Methode, um XML-Daten, die mit Ihren XML-Karten in Ihrem Arbeitsbuch verbunden sind, zu exportieren. Der folgende Beispielcode exportiert die XML-Daten aller XML-Karten aus dem Arbeitsbuch nacheinander. Bitte überprüfen Sie die [Beispieldatei Excel](5115497.xlsx), die in diesem Code verwendet wird, und die [exportierten XML-Daten der ersten XML-Karte](5472487.xml).

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get XML maps from the workbook
    auto xmlMaps = workbook.GetWorksheets().GetXmlMaps();

    // Export all XML data from all XML Maps from the Workbook
    for (int i = 0; i < xmlMaps.GetCount(); i++)
    {
        // Access the XML Map
        XmlMap map = xmlMaps.Get(i);

        // Exports its XML Data to file
        workbook.ExportXml(map.GetName(), outDir + map.GetName() + u".xml");
    }

    std::cout << "XML data exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
