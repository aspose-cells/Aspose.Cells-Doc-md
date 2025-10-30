---
title: Extraer imágenes de hojas de cálculo usando opciones ImageOrPrint con C++
linktitle: Extraer imágenes de hojas de cálculo
type: docs
weight: 140
url: /es/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Aprende cómo extraer imágenes de hojas de cálculo de Excel y guardarlas en una unidad local usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Los usuarios de Microsoft Excel pueden agregar imágenes a hojas de cálculo. Con Aspose.Cells, es posible leer imágenes de archivos de Microsoft Excel y guardarlas en una unidad local. Este artículo muestra cómo hacerlo.

{{% /alert %}} 

El código de muestra a continuación muestra cómo extraer imágenes de un archivo de Excel y guardarlas.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
