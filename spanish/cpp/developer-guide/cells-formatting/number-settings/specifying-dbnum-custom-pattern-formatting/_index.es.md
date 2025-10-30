---
title: Especificando formato de patrón personalizado DBNum con C++
linktitle: Especificar Formato de Patrón Personalizado DBNum
description: Aspose.Cells es una librería en C++ para trabajar con archivos de hojas de cálculo que soporta formatear fechas y números usando patrones de formato personalizados. Este artículo mostrará cómo usar la librería Aspose.Cells para especificar el patrón de formato personalizado dbnum para que los usuarios tengan más control sobre cómo se muestran los números.
keywords: Aspose.Cells, librería C++, hoja de cálculo electrónica, patrón de formato personalizado, formateo, dbnum , control de visualización
type: docs
weight: 110
url: /es/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Escenarios de uso posibles**

Aspose.Cells soporta el formateo de patrones personalizados *DBNum*. Por ejemplo, si el valor de tu celda es 123 y especificas su formato personalizado como [DBNum2][$-804]General, se mostrará como 壹佰贰拾叁. Puedes especificar tu formato personalizado usando el método [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) y la propiedad [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/).

## **Código de muestra**

El siguiente código de ejemplo ilustra cómo especificar el formato de patrón personalizado *DBNum*. Por favor, revisa su [archivo PDF de salida](43352081.pdf) para más ayuda.

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
