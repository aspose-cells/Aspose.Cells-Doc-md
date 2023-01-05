---
title: Cambie la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango
type: docs
weight: 440
url: /es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Posibles escenarios de uso**

Cuando copia filas o rangos que contienen gráficos en una nueva hoja de trabajo, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Hoja1!$A$1:$B$4, luego de copiar las filas o el rango a la nueva hoja de trabajo, la fuente de datos seguirá siendo la misma, es decir, =Hoja1!$A$1:$B$4. Todavía se refiere a la hoja de trabajo anterior, es decir, Sheet1. Este es también el comportamiento en Microsoft Excel. Pero si desea que se refiera a la nueva hoja de cálculo de destino, utilice el[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)propiedad y establecerlo en**verdadero** mientras llama al[**Cells.Copiar filas()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)método. Ahora, si su hoja de cálculo de destino es DestSheet, la fuente de datos de su gráfico cambiará de =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Cambie la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**

 El siguiente código de ejemplo explica el uso de[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) propiedad al copiar filas o rangos que contienen gráficos a una nueva hoja de trabajo. El código utiliza el[ejemplo de archivo de Excel](5113699.xlsx) y genera la[archivo de salida de Excel](5113697.xlsx).

![todo:imagen_alternativa_texto](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
