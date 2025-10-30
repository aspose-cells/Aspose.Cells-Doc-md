---
title: Expandir texto de derecha a izquierda al exportar archivo de Excel a HTML con C++
linktitle: Expandir texto de derecha a izquierda al exportar archivo Excel a HTML
type: docs
weight: 60
url: /es/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Aprende cómo expandir texto de derecha a izquierda al exportar archivos de Excel en HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Ahora Aspose.Cells for C++ soporta expandir texto de derecha a izquierda al exportar archivos de Excel a HTML. Esta función ha sido implementada desde la versión v8.9.0.0. Si tu archivo de Excel contiene texto que se expande de derecha a izquierda, Aspose.Cells lo exportará correctamente a HTML.

{{% /alert %}} 

## **Expandir texto de derecha a izquierda al exportar archivo Excel a HTML**

El siguiente código de ejemplo convierte el archivo de Excel [de ejemplo](5115502.xlsx) en HTML. Esta captura muestra cómo se ve en Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Esta captura muestra el [HTML de salida generado con una versión anterior](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Esta captura muestra el [HTML de salida generado con una versión más reciente](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Como puedes ver en las capturas, la versión más reciente expande correctamente el texto alineado a la derecha hacia la izquierda, igual que en Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
