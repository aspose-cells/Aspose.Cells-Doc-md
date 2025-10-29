---
title: Exporter les données XML liées à la cartographie XML à l intérieur du classeur avec C++
linktitle: Exporter les données XML liées à la carte XML à l intérieur du classeur
type: docs
weight: 20
url: /fr/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Apprenez comment exporter les données XML liées aux cartographies XML dans votre classeur en utilisant Aspose.Cells for C++.
---

## **Exporter des données XML liées à la carte XML à l'intérieur du classeur**

Veuillez utiliser la méthode [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) pour exporter les données XML liées à vos cartographies XML dans votre classeur. Le code d'exemple suivant exporte les données XML de toutes les cartographies XML du classeur une par une. Veuillez vérifier le [fichier Excel d'exemple](5115497.xlsx) utilisé dans ce code et les [données XML exportées de la première cartographie XML](5472487.xml).

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
