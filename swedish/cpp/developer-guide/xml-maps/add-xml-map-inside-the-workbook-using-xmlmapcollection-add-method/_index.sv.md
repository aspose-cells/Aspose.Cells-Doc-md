---
title: Lägg till XML karta i arbetsboken med XmlMapCollection.Add metoden med C++
linktitle: Lägg till XML karta i arbetsboken med XmlMapCollection.Add metoden
type: docs
weight: 10
url: /sv/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: Lägg till XML karta i arbetsboken med XmlMapCollection.Add metoden med C++.
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) metod som du kan använda för att importera din XML-karta inuti arbetsboken.

## **Lägg till XML-karta i arbetsboken med XmlMapCollection.Add-metoden**

Följande exempelkod lägger till XML-karta inuti arbetsboken med hjälp av [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) metoden och sparar den som [utdata excelfil](5115434.xlsx). Skärmbilden visar den XML-karta som har importerats från [sample.xml](5115433.xml) inuti den resulterande excelfilen.

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
