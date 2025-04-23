---
title: Especificar autor al proteger escritura del libro con C++
linktitle: Especificar Autor al proteger un libro de trabajo
type: docs
weight: 40
url: /es/cpp/specify-author-while-write-protecting-workbook/
description: Aprende a especificar un nombre de autor al proteger un libro en escritura usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puedes especificar el nombre del autor al proteger la escritura de tu libro de trabajo usando la API de Aspose.Cells. Por favor, usa la propiedad [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) para este propósito.

## **Especificar Autor al Proteger la Escritura del Libro de Trabajo**

El siguiente ejemplo de código explica el uso de la propiedad [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/). El código crea un libro de trabajo vacío, lo protege con contraseña, especifica el nombre del autor y lo guarda como un [archivo de Excel de salida](67338582.xlsx). La siguiente captura de pantalla ilustra el efecto del código de muestra en el archivo de Excel resultante para referencia.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
