---
title: Especificar la versión del documento del archivo Excel usando propiedades de documento integradas con C++
linktitle: Especificar la versión del documento
type: docs
weight: 20
url: /es/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Aprende cómo especificar la versión del documento de un archivo Excel usando propiedades de documento integradas con Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puedes cambiar el **Número de versión** de un archivo Excel haciendo clic derecho en el archivo y seleccionando Propiedades > Detalles y editando el campo **Número de versión**. Por favor, usa la propiedad [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) para cambiarlo programáticamente usando las APIs de Aspose.Cells.

## **Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas**

El siguiente ejemplo de código crea un libro de trabajo y cambia sus propiedades de documento integradas que incluyen Título, Autor y Número de versión. Por favor, mira el [archivo Excel de salida](64716811.xlsx) generado por el código y la captura que muestra el número de versión modificado mediante la propiedad [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
