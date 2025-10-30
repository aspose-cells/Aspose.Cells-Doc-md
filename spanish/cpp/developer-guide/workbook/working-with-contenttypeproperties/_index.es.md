---
title: Trabajando con ContentTypeProperties con C++
linktitle: Trabajando con ContentTypeProperties
type: docs
weight: 150
url: /es/cpp/working-with-contenttypeproperties/
description: Agrega características de tipo de contenido personalizadas a un archivo de Excel usando Aspose.Cells con C++.
---

Aspose.Cells proporciona el método [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) para agregar ContentTypeProperties personalizados a un archivo de Excel. También puedes hacer que la propiedad sea opcional configurando la propiedad [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) a **true**. El siguiente fragmento de código demuestra cómo agregar propiedades ContentTypeProperties opcionales a un archivo de Excel. La siguiente imagen muestra ambas propiedades que fueron agregadas por el código de muestra.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

El archivo de salida generado por el código de ejemplo se adjunta para referencia.

[Archivo de Salida](95584314.xlsx)

## **Código de muestra**

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
