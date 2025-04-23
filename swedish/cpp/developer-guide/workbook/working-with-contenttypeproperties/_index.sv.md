---
title: Arbeta med ContentTypeProperties med C++
linktitle: Arbeta med ContentTypeProperties
type: docs
weight: 150
url: /sv/cpp/working-with-contenttypeproperties/
description: Lägg till anpassade ContentTypeProperties till en Excel fil med Aspose.Cells och C++.
---

Aspose.Cells tillhandahåller [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) metod för att lägga till anpassade ContentTypeProperties i en Excel-fil. Du kan också göra egenskapen valfri genom att sätta [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) egenskapen till **true**. Följande kodavsnitt demonstrerar att lägga till valfria anpassade ContentTypeProperties i en Excel-fil. Bilden nedan visar båda egenskaperna som tillfogades av kodexemplet.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Utdatafilen som genererats av exempelkoden bifogas för referens.

[Utdatafil](95584314.xlsx)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook with XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Add content type properties
    int index = workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(false);

    // Get current date and time
    time_t now = time(nullptr);
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%S", localtime(&now));
    U16String dateTime(buffer);

    // Add another content type property with current date and time
    index = workbook.GetContentTypeProperties().Add(u"MK32", dateTime, u"DateTime");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(true);

    // Save the workbook
    workbook.Save(outDir + u"WorkingWithContentTypeProperties_out.xlsx");

    std::cout << "Content type properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
