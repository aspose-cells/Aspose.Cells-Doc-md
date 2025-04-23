---
title: Exportar rango de celdas en una hoja de cálculo a imagen con C++
linktitle: Exportar rango de celdas a imagen
type: docs
weight: 60
url: /es/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Aprende cómo exportar un rango específico de celdas en una hoja de cálculo a una imagen usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Puede hacer una imagen de una hoja de cálculo utilizando Aspose.Cells. Sin embargo, a veces necesita exportar solo un rango de celdas en una hoja de cálculo a una imagen. Este artículo explica cómo lograrlo.

## **Exportar un rango de celdas en una hoja de cálculo a una imagen**

Para tomar una imagen de un rango, establezca el área de impresión en el rango deseado y luego establezca todos los márgenes en 0. También establezca [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) a **true**. El siguiente código toma una imagen del rango D8:G16. A continuación se muestra una captura de pantalla del [archivo de Excel de muestra](47153160.xlsx) utilizado en el código. Puede probar el código con cualquier archivo de Excel.

## **Captura de pantalla del archivo de Excel de muestra y su imagen exportada**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Al ejecutar el código se crea una imagen del rango D8:G16 solamente.

**![todo:image_alt_text](Output-Image.png)**

## **Código de muestra**

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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
