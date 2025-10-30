---
title: Crear línea de firma en un libro de Excel con C++ usando Aspose.Cells
linktitle: Crear línea de firma en un libro de trabajo de Excel
type: docs
weight: 150
url: /es/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Este artículo describe cómo crear una línea de firma en un libro de Excel usando códigos C++ con Aspose.Cells for C++.
keywords: Crear línea de firma en un libro de Excel, Cómo crear una línea de firma en un libro de Excel, Cómo agregar una línea de firma, Cómo agregar una línea de firma a un archivo de Excel.
---

## **Introducción**

Microsoft Excel proporciona una función para agregar **Línea de Firma** en libros de Excel. Puedes agregar una Línea de Firma haciendo clic en la pestaña **Insertar** y luego seleccionando **Línea de Firma** del grupo **Texto**.

## **Cómo crear una línea de firma para Excel**

Aspose.Cells también proporciona esta función y ha expuesto la propiedad [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) para este propósito. Este artículo explicará cómo usar esta propiedad para agregar una Línea de Firma usando Aspose.Cells.

El siguiente código de muestra agrega una Línea de Firma usando la propiedad [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) y guarda el libro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
