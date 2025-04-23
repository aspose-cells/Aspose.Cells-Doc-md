---
title: Convertir datos numéricos de texto a número con C++
linktitle: Convertir Datos Numéricos de Texto a Número
type: docs
weight: 900
url: /es/cpp/convert-text-numeric-data-to-number/
description: Aprende cómo convertir números almacenados como texto en Excel a números usando la API Aspose.Cells for C++.
keywords: convertir texto a número en Excel, convertir texto a número en Excel c++, convertir datos numéricos de texto a número en Excel, convertir datos numéricos de texto a número en Excel c++, convertir texto numérico a número en Excel, convertir texto numérico a número en Excel c++, convertir texto numérico a número con C++, convertir texto numérico a número en Excel con C++, convertir texto numérico en Excel a número en C++, convertir cadena numérica a número en Excel con C++, convertir datos numéricos de texto a número en Excel c++, convertir cadena numérica en Excel a número c++
---

## **Escenarios de uso posibles**
A veces, deseas convertir datos numéricos ingresados como texto a números. Puedes ingresar números como texto en Microsoft Excel poniendo un apóstrofe antes de un número, por ejemplo **'12345**. Entonces, Excel trata el número como una cadena. Aspose.Cells te permite convertir cadenas a números.

## Cómo convertir números almacenados como texto a números en Excel
Puede convertir números almacenados como texto a números siguiendo unos pocos pasos simples.
1. Seleccione cualquier celda individual o rango de celdas que tenga un indicador de error en la esquina superior izquierda.
1. Junto a la celda o rango de celdas seleccionado, haga clic en el botón de error que aparece. En el menú, haga clic en Convertir a Número. 
<br>
<img src="4.png" width=70% />
1. Si el botón de alerta no está disponible, seleccione una columna con este problema. Si no desea convertir toda la columna, puede seleccionar una o más celdas en su lugar. Asegúrese de que las celdas que seleccione estén en la misma columna, de lo contrario este proceso no funcionará. El botón Texto en Columnas se usa típicamente para dividir una columna, pero también se puede usar para convertir una sola columna de texto a números. En la pestaña Datos, haga clic en Texto en Columnas.
<br>
<img src="1.png" width=70% />
1. Haga clic en el botón Finalizar en el cuadro emergente.
<br>
<img src="2.png" width=70% />
1. Los números almacenados como texto se transforman en números.
<br>
<img src="3.png" width=70% />

## Cómo convertir números almacenados como texto en números usando Aspose.Cells for C++
Aspose.Cells proporciona el método [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) que se puede utilizar para convertir todos los datos numéricos de texto o cadena en números.

La siguiente captura de pantalla muestra números de cadena en las celdas **A1:A17**. Los números de cadena están alineados a la izquierda.
<br>
<img src="5.png" width=70% />

Estos números de cadena se han convertido en números utilizando [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) en la siguiente captura de pantalla. Como se puede ver, ahora están alineados a la derecha.
<br>
<img src="6.png" width=70% />

## Código en C++ para convertir datos numéricos en cadena en números reales

El siguiente código de muestra ilustra cómo convertir todos los datos numéricos de cadena en números reales en todas las hojas de cálculo.

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

    // Instantiate workbook object with an Excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";
    Workbook workbook(inputFilePath);

    // Iterate through all worksheets and convert string values to numeric
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        workbook.GetWorksheets().Get(i).GetCells().ConvertStringToNumericValue();
    }

    // Save the Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
