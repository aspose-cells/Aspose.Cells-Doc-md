---
title: Aggiungi una mappa XML all interno del Workbook usando il metodo XmlMapCollection.Add con C++
linktitle: Aggiungi mappa XML all interno del foglio di lavoro utilizzando il metodo XmlMapCollection.Add
type: docs
weight: 10
url: /it/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: Aggiungi una mappa XML all interno del workbook usando il metodo XmlMapCollection.Add con C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce il metodo [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) che puoi utilizzare per importare la tua mappa XML all'interno del workbook.

## **Aggiungi mappa XML all'interno del foglio di lavoro utilizzando il metodo XmlMapCollection.Add**

Il seguente codice di esempio aggiunge una mappa XML all'interno del workbook utilizzando il metodo [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) e lo salva come [file Excel di output](5115434.xlsx). La schermata mostra la mappa XML che è stata importata dal file [sample.xml](5115433.xml) all'interno del file Excel di output.

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
{{< app/cells/assistant language="cpp" >}}
