---
title: Travailler avec ContentTypeProperties avec C++
linktitle: Travailler avec ContentTypeProperties
type: docs
weight: 150
url: /fr/cpp/working-with-contenttypeproperties/
description: Ajouter des ContentTypeProperties personnalisés à un fichier Excel en utilisant Aspose.Cells avec C++.
---

Aspose.Cells fournit la méthode [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) pour ajouter des ContentTypeProperties personnalisés à un fichier Excel. Vous pouvez également rendre la propriété facultative en définissant la propriété [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) à **true**. Le code suivant montre comment ajouter des ContentTypeProperties personnalisés optionnels à un fichier Excel. L’image suivante montre les deux propriétés ajoutées par le code.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Le fichier de sortie généré par le code d'exemple est joint pour référence.

[Fichier de sortie](95584314.xlsx)

## **Code d'exemple**

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
