---
title: Excel a HTML  Usa la opción PresentationPreference para una mejor distribución con C++
linktitle: De Excel a HTML  Usa la Opción PresentationPreference para un Mejor Diseño
type: docs
weight: 220
url: /es/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: Aprende a renderizar mejor la distribución al guardar archivos de Excel en HTML con C++.
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona una útil propiedad HtmlSaveOptions.PresentationPreference para desarrolladores que necesitan renderizar un mejor diseño al guardar un archivo de Microsoft Excel en formato HTML o MHT. El valor predeterminado de la propiedad es false. Recomendamos establecer esta propiedad en true para obtener una presentación más atractiva de los informes de Excel.

{{% /alert %}} 

Por favor mira el código de muestra abajo que demuestra cómo renderizar un archivo HTML desde un informe de Excel con preferencia de presentación.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
