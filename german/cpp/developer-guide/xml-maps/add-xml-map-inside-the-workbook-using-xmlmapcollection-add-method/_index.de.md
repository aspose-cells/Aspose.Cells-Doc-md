---
title: XML Karten in die Arbeitsmappe mit der Methode XmlMapCollection.Add in C++ einfügen
linktitle: XML Map innerhalb der Arbeitsmappe mit der XmlMapCollection.Add Methode hinzufügen
type: docs
weight: 10
url: /de/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: XML Karte in die Arbeitsmappe mit der Methode XmlMapCollection.Add in C++ einfügen.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet die Methode [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/), die Sie verwenden können, um Ihre XML-Map in die Arbeitsmappe zu importieren.

## **XML Map innerhalb der Arbeitsmappe mit der XmlMapCollection.Add Methode hinzufügen**

Der folgende Beispielcode fügt mithilfe der Methode [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) eine XML-Map in die Arbeitsmappe ein und speichert sie als [Ausgabedatei](5115434.xlsx). Der Screenshot zeigt die XML-Map, die aus [sample.xml](5115433.xml) in die Ausgabedatei importiert wurde.

![add-xml-map](add-xml-map.png)

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

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
