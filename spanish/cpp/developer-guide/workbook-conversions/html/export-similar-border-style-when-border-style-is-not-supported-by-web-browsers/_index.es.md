---
title: Exportar estilo de borde similar cuando el estilo de borde no sea compatible con navegadores web con C++
linktitle: Exportar un Estilo de Borde Similar cuando el Estilo de Borde no es compatible con los Navegadores Web
type: docs
weight: 70
url: /es/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Aprenda cómo exportar estilos de borde similares cuando no sean compatibles con navegadores web usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Microsoft Excel soporta algunos tipos de bordes discontinuos que no son compatibles con navegadores web. Cuando conviertes dicho archivo de Excel en HTML usando Aspose.Cells, dichos bordes se eliminan. Sin embargo, Aspose.Cells también puede soportar mostrar estos bordes usando la propiedad [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/). Configure su valor en **true** y los bordes no soportados también se exportarán en el archivo HTML.

## **Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716806.xlsx) que contiene algunos bordes no soportados, como se muestra en la siguiente captura de pantalla. La captura ilustra además el efecto de la propiedad [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/) en el [HTML de salida](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
