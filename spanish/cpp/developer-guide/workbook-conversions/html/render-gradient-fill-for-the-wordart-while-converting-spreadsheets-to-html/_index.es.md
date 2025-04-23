---
title: Renderizar relleno de degradado para WordArt al convertir hojas de cálculo a HTML con C++
linktitle: Renderizar relleno degradado para WordArt al convertir hojas de cálculo a HTML
type: docs
weight: 90
url: /es/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Aprende a renderizar relleno de degradado para WordArt al convertir hojas de cálculo a HTML con C++.
---

## **Escenarios de uso posibles**
Antes de Aspose.Cells 17.1, Aspose.Cells no renderizaba el relleno degradado del arte de palabras cuando el archivo de Excel se convertía al formato HTML. Desde el lanzamiento de Aspose.Cells 17.1, se admite el relleno degradado del arte de palabras. La siguiente captura de pantalla compara el efecto en el relleno degradado al convertir el archivo de Excel usando Aspose.Cells 17.1 y la versión anterior.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **Renderizar relleno degradado para WordArt al convertir hojas de cálculo a HTML**
El siguiente código de ejemplo convierte el [archivo de Excel fuente](22774111.xlsx) en [formato HTML de salida](22774109.zip). El archivo de Excel fuente contiene un objeto WordArt con relleno degradado como se muestra en la captura de pantalla anterior.
## **Código de muestra**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
