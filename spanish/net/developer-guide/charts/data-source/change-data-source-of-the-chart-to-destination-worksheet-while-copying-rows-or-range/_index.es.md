---
title: Cambie la fuente de datos del gráfico a la hoja de trabajo de destino mientras copia filas o rango
description: Aprenda cómo cambiar la fuente de datos de un gráfico a una hoja de cálculo de destino mientras copia filas o un rango en Aspose.Cells for .NET. Nuestra guía le mostrará cómo actualizar el rango de datos del gráfico y vincularlo a la hoja de cálculo de destino, asegurándose de que las filas copiadas o El rango se refleja con precisión en el gráfico.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **Posibles escenarios de uso**

Cuando copia filas o rangos que contienen gráficos a una nueva hoja de trabajo, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Hoja1!$A$1:$B$4, luego de copiar filas o rango a una nueva hoja de trabajo, la fuente de datos seguirá siendo la misma, es decir, =Hoja1!$A$1:$B$4. Todavía hace referencia a la hoja de trabajo antigua, es decir, la Hoja1. Este también es el comportamiento en Microsoft Excel. Pero si desea que se refiera a la nueva hoja de trabajo de destino, utilice el[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)propiedad y configúrelo en**verdadero** mientras llama al[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)método. Ahora, si su hoja de trabajo de destino es DestSheet, entonces la fuente de datos de su gráfico cambiará de =Hoja1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

##  **Cambie la fuente de datos del gráfico a la hoja de trabajo de destino mientras copia filas o rango**

El siguiente código de muestra explica el uso de[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) propiedad al copiar filas o rangos que contienen gráficos a una nueva hoja de trabajo. El código utiliza el[archivo de excel de muestra](5113699.xlsx) y genera el[archivo de excel de salida](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
