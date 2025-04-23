---
title: Agregar propiedades personalizadas visibles en el Panel de Información del Documento con C++
linktitle: Agregar Propiedades Personalizadas visibles dentro del Panel de Información del Documento
type: docs
weight: 300
url: /es/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aprende cómo agregar propiedades personalizadas visibles en el Panel de Información del Documento usando Aspose.Cells con C++.
---

## **Agregar propiedades personalizadas visibles dentro del Panel de información del documento**

Aspose.Cells se puede utilizar para agregar propiedades personalizadas dentro del objeto del libro que son visibles dentro del Panel de Información del Documento. Puede abrir el Panel de Información del Documento en Microsoft Excel usando los comandos del menú Archivo > Información > Propiedades > Mostrar panel de documentos.

Utilice el método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) para agregar una propiedad personalizada que será visible en el Panel de Información del Documento.

El siguiente ejemplo de código añade dos propiedades personalizadas. La primera propiedad no tiene ningún tipo y la segunda tiene un tipo como DateTime. Cuando abras el archivo de Excel generado por este código, verás estas dos propiedades dentro del Panel de Información del Documento.

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

    // Create workbook object with specified format
    Workbook workbook(FileFormatType::Xlsx);

    // Add simple property without any type
    workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");

    // Add date time property with type
    workbook.GetContentTypeProperties().Add(u"MK32", u"04-Mar-2015", u"DateTime");

    // Save the workbook
    workbook.Save(srcDir + u"AddingCustomPropertiesVisible_out.xlsx");

    std::cout << "Custom properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Artículo Relacionado**

{{% alert color="primary" %}}

- [Usar Partes de XML Personalizadas en Aspose.Cells](/cells/es/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
