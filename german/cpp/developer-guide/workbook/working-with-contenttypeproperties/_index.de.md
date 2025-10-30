---
title: Arbeiten mit ContentTypeProperties mit C++
linktitle: Arbeiten mit ContentTypeProperties
type: docs
weight: 150
url: /de/cpp/working-with-contenttypeproperties/
description: Fügen Sie einem Excel Dokument mithilfe von Aspose.Cells mit C++ benutzerdefinierte ContentTypeProperties hinzu.
---

Aspose.Cells bietet die [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)-Methode zum Hinzufügen benutzerdefinierter ContentTypeProperties zu einer Excel-Datei. Sie können die Eigenschaft auch optional machen, indem Sie die [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/)-Eigenschaft auf **true** setzen. Das folgende Codebeispiel demonstriert das Hinzufügen optionaler benutzerdefinierter ContentTypeProperties zu einer Excel-Datei. Das folgende Bild zeigt beide Eigenschaften, die durch den Beispielcode hinzugefügt wurden.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Die durch den Beispielcode generierte Ausgabedatei ist als Referenz angehängt.

[Ausgabedatei](95584314.xlsx)

## **Beispielcode**

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
{{< app/cells/assistant language="cpp" >}}
