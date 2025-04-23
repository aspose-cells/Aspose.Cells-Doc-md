---
title: Especificar el idioma del archivo Excel usando propiedades de documento integradas con C++
linktitle: Especificar el idioma del archivo Excel
type: docs
weight: 30
url: /es/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Aprende cómo cambiar programáticamente el idioma de un archivo Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puedes cambiar el idioma de un archivo Excel haciendo clic derecho en el archivo, seleccionando Propiedades > Detalles y editando el campo Idioma. Por favor, usa la propiedad [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) para cambiarlo programáticamente usando las APIs de Aspose.Cells.

## **Especificar el idioma del archivo de Excel mediante propiedades de documento integradas**

El siguiente ejemplo de código crea un libro de trabajo y cambia su propiedad de documento integrada llamada Idioma. Por favor, mira el [archivo Excel de salida](64716891.xlsx) generado por el código y la captura que muestra el campo Idioma modificado por la propiedad [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

```c++
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

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
