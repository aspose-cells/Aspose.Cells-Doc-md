---  
title: Cambiar la Fuente de Datos del Gráfico a la Hoja de Destino al copiar filas o rango con C++  
description: Aprende cómo cambiar la fuente de datos de un gráfico a una hoja de destino mientras copias filas o un rango en Aspose.Cells for C++. Nuestra guía te mostrará cómo actualizar el rango de datos del gráfico y enlazarlo a la hoja de destino, asegurando que las filas o rango copiados se reflejen con precisión en el gráfico.  
keywords: Aspose.Cells for C++, gráficos, fuente de datos, hoja de destino, filas, rango, copiar, actualizar, rango de datos, enlace.  
type: docs  
weight: 440  
url: /es/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Escenarios de uso posibles**

Cuando copias filas o rango que contiene gráficos a una nueva hoja, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Sheet1!$A$1:$B$4, después de copiar filas o rango a una nueva hoja, la fuente de datos permanecerá igual, es decir, =Sheet1!$A$1:$B$4. Sigue refiriéndose a la hoja antigua, es decir, Sheet1. Este es también el comportamiento en Microsoft Excel. Pero si deseas que se refiera a la nueva hoja de destino, usa la propiedad [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) y configúrala en **true** al llamar al método [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). Ahora, si tu hoja de destino es DestSheet, la fuente de datos de tu gráfico cambiará de =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**

El siguiente código de ejemplo explica cómo usar la propiedad [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) al copiar filas o rangos que contienen gráficos a una nueva hoja. El código usa el [archivo de ejemplo en Excel](5113699.xlsx) y genera el [archivo de salida en Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
