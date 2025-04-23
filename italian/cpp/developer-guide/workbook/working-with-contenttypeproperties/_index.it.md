---
title: Lavorare con ContentTypeProperties con C++
linktitle: Lavorare con ContentTypeProperties
type: docs
weight: 150
url: /it/cpp/working-with-contenttypeproperties/
description: Aggiungi proprietà ContentTypePersonalizzate a un file Excel usando Aspose.Cells con C++.
---

Aspose.Cells fornisce il metodo [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) per aggiungere proprietà ContentTypePersonalizzate a un file Excel. Puoi anche rendere la proprietà opzionale impostando la proprietà [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) su **true**. Il seguente frammento di codice dimostra come aggiungere proprietà ContentTypePersonalizzate opzionali a un file Excel. L'immagine seguente mostra entrambe le proprietà aggiunte dal codice di esempio.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Il file di output generato dal codice di esempio è allegato per riferimento.

[File di Output](95584314.xlsx)

## **Codice di Esempio**

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
