---
title: Especificar Dígitos Significativos a Almacenar en Archivo de Excel con C++
linktitle: Especificando Dígitos Significativos
type: docs
weight: 30
url: /es/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aprende cómo especificar dígitos significativos para almacenarlos en archivos de Excel usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Por defecto, Aspose.Cells almacena 17 dígitos significativos de valores doble dentro del archivo Excel, a diferencia de MS-Excel que almacena solo 15 dígitos significativos. Puedes cambiar el comportamiento predeterminado de Aspose.Cells de 17 a 15 dígitos significativos usando la propiedad [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/).

## **Especificación de Dígitos Significativos a ser almacenados en un archivo de Excel**

El siguiente código de ejemplo fuerza a Aspose.Cells a usar 15 dígitos significativos al almacenar valores doble dentro del archivo Excel. Comprueba el [archivo Excel de salida](22774105.xlsx). Cambia su extensión a .zip y descomprímelo, verás que solo se almacenan 15 dígitos significativos. La siguiente captura de pantalla explica el efecto de la propiedad [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) en el archivo Excel de salida.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

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

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
