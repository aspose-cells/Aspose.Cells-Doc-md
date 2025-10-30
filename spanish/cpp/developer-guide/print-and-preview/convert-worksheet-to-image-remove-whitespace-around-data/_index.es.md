---
title: Convertir Hoja de cálculo a Imagen  Eliminar Espacio en Blanco alrededor de los Datos con C++
linktitle: Convertir Hoja de cálculo a Imagen  Eliminar Espacio en Blanco alrededor de los Datos
type: docs
weight: 40
url: /es/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Aprende cómo convertir una hoja de cálculo a una imagen y eliminar espacios en blanco alrededor de los datos usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, es necesario presentar imágenes de hojas de cálculo en aplicaciones o páginas web. Por ejemplo, puede que necesites insertar imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint, u otro documento. Básicamente, quieres renderizar una hoja de cálculo como una imagen para poder pegarla en otras aplicaciones. Aspose.Cells te permite convertir hojas de cálculo de Excel en imágenes.

{{% /alert %}}

## **Eliminar espacios en blanco alrededor de los datos**

El API [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) convierte una hoja de cálculo en un archivo de imagen con atributos especificados, por ejemplo, formato de imagen, hojas paginadas, etc. Se admiten varios formatos de imagen, incluyendo BMP, GIF, JPG, TIFF y EMF.

Cuando utilizas la función de hoja a imagen, la imagen de salida tiene espacios en blanco, es decir, un borde, por defecto. Puedes eliminar esto configurando los márgenes de configuración de página superior, inferior, izquierdo y derecho de la hoja fuente a 0 y especificando los atributos [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) en consecuencia.

El siguiente fragmento de código elimina los espacios en blanco alrededor de los datos en la imagen de salida.

```c++
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

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
