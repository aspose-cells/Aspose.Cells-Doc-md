---
title: Configuración de fórmula compartida con C++
linktitle: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/cpp/setting-shared-formula/
description: Aprenda cómo establecer fórmulas compartidas en hojas de cálculo de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Si desea agregar una función en una hoja de cálculo que realice cálculos, este artículo explica cómo lograr esta tarea usando Aspose.Cells.

{{% /alert %}}

## Estableciendo fórmula compartida usando Aspose.Cells

Supongamos que tienes una hoja de trabajo llena de datos con el formato que se muestra en la siguiente hoja de cálculo de ejemplo.

|Archivo de entrada con una columna de datos|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Quieres agregar una función en B2 que calculará el impuesto sobre las ventas para la primera fila de datos. El impuesto es del **9%**. La fórmula que calcula el impuesto sobre las ventas es: **"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

Aspose.Cells te permite especificar una fórmula utilizando la propiedad [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/). Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, y así sucesivamente) en la columna.

O haga lo que hizo para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de la celda en consecuencia (A3*0.09, A4*0.09, A5*0.09 y así sucesivamente). Esto requiere que las referencias de celda para cada fila se actualicen. También requiere que Aspose.Cells analice cada fórmula individualmente, lo cual puede ser lento para hojas de cálculo grandes y fórmulas complejas. Además, agrega líneas adicionales de código, aunque los bucles pueden reducirlas en cierta medida.

Otro enfoque es usar una **fórmula compartida**. Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. El método [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo.

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
