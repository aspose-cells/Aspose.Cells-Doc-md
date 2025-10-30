--- 
title: Crear imagen transparente de hoja de cálculo de Excel con C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /es/cpp/create-transparent-image-of-excel-worksheet/ 
description: Generar imágenes transparentes de hojas de cálculo de Excel usando Aspose.Cells con C++. 
--- 

{{% alert color="primary" %}} 

A veces, es necesario generar la imagen de la hoja de cálculo como una imagen transparente. Desea aplicar transparencia a todas las celdas que no tienen colores de relleno. Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/) para aplicar transparencia a la imagen de la hoja de cálculo. Cuando esta propiedad es **false**, entonces las celdas sin colores de relleno se dibujan con color blanco, y cuando es **true**, las celdas sin colores de relleno se dibujan transparentes. 

{{% /alert %}} 

En la siguiente imagen de la hoja de cálculo, no se ha aplicado transparencia. Las celdas sin colores de relleno se dibujan de color blanco.

|**Resultado sin transparencia: el fondo de la celda es blanco**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

Mientras que, en la siguiente imagen de la hoja de cálculo, se ha aplicado transparencia. Las celdas sin colores de relleno son transparentes.

|**Resultado con transparencia habilitada**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

El siguiente código de ejemplo genera una imagen transparente a partir de una hoja de cálculo de Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleCreateTransparentImage.xlsx");

    // Apply different image or print options
    ImageOrPrintOptions imgOption;
    imgOption.SetImageType(static_cast<ImageType>(5)); // Png
    imgOption.SetHorizontalResolution(200);
    imgOption.SetVerticalResolution(200);
    imgOption.SetOnePagePerSheet(true);

    // Apply transparency to the output image
    imgOption.SetTransparent(true);

    // Create image after applying image or print options
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOption);
    sr.ToImage(0, outputDir + u"outputCreateTransparentImage.png");

    std::cout << "Image created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
