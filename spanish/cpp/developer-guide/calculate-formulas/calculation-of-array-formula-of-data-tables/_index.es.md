---
title: Cálculo de Fórmulas de Matrices de Tablas de Datos con C++
linktitle: Cálculo de la fórmula de arreglo de tablas de datos
description: Cómo usar la biblioteca Aspose.Cells para calcular fórmulas de matriz en una tabla de datos en Microsoft Excel con C++. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar el método proporcionado por Aspose.Cells para calcular la fórmula de matriz de la tabla de datos y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en disco.
keywords: Aspose.Cells, Excel, tablas de datos, fórmulas de matriz, cálculos, C++
type: docs
weight: 70
url: /es/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Puede crear una tabla de datos en Microsoft Excel utilizando Datos > Análisis ¿Y si? > Tabla de datos.... Ahora Aspose.Cells le permite calcular la fórmula de arreglo de una tabla de datos. Por favor, use [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) como normal para calcular cualquier tipo de fórmulas.

{{% /alert %}}

En el siguiente código de ejemplo, usamos el [archivo de Excel de origen](5115535.xlsx). Si cambia el valor de la celda B1 a 100, los valores de la tabla de datos que están llenos con color amarillo se convertirán en 120 como se muestra en las siguientes imágenes. El código de ejemplo genera el [PDF de salida](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

A continuación se muestra el código de ejemplo utilizado para generar el [PDF de salida](5115538.pdf) a partir del [archivo de Excel de origen](5115535.xlsx). Por favor, lea los comentarios para más información.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
