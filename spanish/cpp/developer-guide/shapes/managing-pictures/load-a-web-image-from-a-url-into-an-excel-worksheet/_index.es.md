---
title: Cargar una imagen web desde una URL en una hoja de cálculo de Excel con C++
linktitle: Cargar una Imagen Web desde una URL en una Hoja de Excel
type: docs
weight: 30
url: /es/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Aprenda cómo convertir una imagen desde URL a imagen incrustada en Excel usando C++ y API Aspose.Cells for C++.
keywords: Excel mostrar imagen desde URL, url a imagen en Excel, mostrar imagen en Excel desde URL, insertar imagen en Excel desde URL, convertir URL a imagen en Excel, imagen en Excel desde URL, cargar imagen desde URL en Excel, C++, Excel
---

## Cargar una imagen desde una URL en una hoja de Excel

La API Aspose.Cells for C++ proporciona un método sencillo para cargar imágenes desde URLs en hojas de Excel. Este artículo explica cómo descargar datos de imagen en un flujo de memoria e insertarla en la hoja utilizando Aspose.Cells. La imagen se incrusta en el archivo de Excel y no requiere descargas externas al abrirse.

## Código de Muestra

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Para escenarios que requieren imágenes siempre actualizadas desde una URL, use el método descrito en [Insertar una imagen vinculada desde web] (/cells/es/cpp/insert-a-linked-picture-from-web-address/). Este método carga la imagen desde la URL cada vez que se abre la hoja.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
