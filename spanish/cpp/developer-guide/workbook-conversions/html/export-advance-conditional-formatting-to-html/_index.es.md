---
title: Exportar formato condicional DataBar, Escala de Colores y Conjunto de Iconos durante la conversión de Excel a HTML con C++
linktitle: Exportar formato condicional a HTML
type: docs
weight: 30
url: /es/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Aprenda cómo exportar formato condicional DataBar, ColorScale y IconSet al convertir archivos de Excel a HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Puedes exportar formato condicional DataBar, ColorScale y IconSet al convertir tu archivo de Excel en HTML. Esta función es parcialmente compatible con Microsoft Excel pero Aspose.Cells for C++ la soporta completamente.

{{% /alert %}} 

## **Exportar formato condicional DataBar, ColorScale y IconSet durante la conversión de Excel a HTML**
La siguiente captura de pantalla muestra el [archivo de Excel de muestra](5115558.xlsx) con formato condicional DataBar, ColorScale y IconSet. Puedes descargar el [archivo de Excel de muestra](5115558.xlsx) desde el enlace proporcionado.

![todo:image_alt_text](conversion_1.png)

La siguiente captura de pantalla muestra el archivo HTML generado por Aspose.Cells con formato condicional DataBar, ColorScale y IconSet. Como puedes ver, se ve exactamente como el [archivo de Excel de muestra](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **Código de muestra**
El siguiente código de ejemplo convierte el archivo de Excel de muestra en HTML, lo cual es simplemente una conversión normal de [Excel a HTML](/cells/es/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).

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

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
