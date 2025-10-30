---  
title: Cambiar la fuente de datos del gráfico a la hoja de destino mientras se copian filas o rango con Golang a través de C++  
description: Aprende cómo cambiar la fuente de datos de un gráfico a una hoja de destino mientras copias filas o un rango en Aspose.Cells for C++. Nuestra guía te mostrará cómo actualizar el rango de datos del gráfico y enlazarlo a la hoja de destino, asegurando que las filas o rango copiados se reflejen con precisión en el gráfico.  
keywords: Aspose.Cells for C++, gráficos, fuente de datos, hoja de destino, filas, rango, copiar, actualizar, rango de datos, enlace.  
type: docs  
weight: 440  
url: /es/go-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Escenarios de uso posibles**

Cuando copias filas o rango que contiene gráficos a una nueva hoja, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Sheet1!$A$1:$B$4, después de copiar filas o rango a una nueva hoja, la fuente de datos permanecerá igual, es decir, =Sheet1!$A$1:$B$4. Sigue refiriéndose a la hoja antigua, es decir, Sheet1. Este es también el comportamiento en Microsoft Excel. Pero si deseas que se refiera a la nueva hoja de destino, usa la propiedad [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) y configúrala en **true** al llamar al método [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). Ahora, si tu hoja de destino es DestSheet, la fuente de datos de tu gráfico cambiará de =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**

El siguiente código de ejemplo explica cómo usar la propiedad [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) al copiar filas o rangos que contienen gráficos a una nueva hoja. El código usa el [archivo de ejemplo en Excel](5113699.xlsx) y genera el [archivo de salida en Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeDataSourceOfTheChartToDestinationWorksheetWhileCopyingRowsOrRange.go" >}}
