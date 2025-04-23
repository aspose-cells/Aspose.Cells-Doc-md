---
title: Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango
description: Aprenda cómo cambiar la fuente de datos de un gráfico a una hoja de cálculo de destino al copiar filas o un rango en Aspose.Cells for .NET. Nuestra guía le mostrará cómo actualizar el rango de datos del gráfico y vincularlo a la hoja de cálculo de destino, asegurándose de que las filas o el rango copiados se reflejen con precisión en el gráfico.
keywords: Aspose.Cells for .NET, graficación, fuente de datos, hoja de cálculo de destino, filas, rango, copiar, actualizar, rango de datos, vinculación.
type: docs
weight: 440
url: /es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Escenarios de uso posibles**

Cuando copia filas o un rango que contiene gráficos a una nueva hoja de cálculo, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Sheet1!$A$1:$B$4, entonces después de copiar filas o un rango a una nueva hoja de cálculo, la fuente de datos seguirá siendo la misma, es decir, =Sheet1!$A$1:$B$4. Todavía se refiere a la hoja de cálculo antigua, es decir, Sheet1. Esto también es el comportamiento en Microsoft Excel. Pero si desea que haga referencia a la nueva hoja de cálculo de destino, entonces por favor utilice la propiedad [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) y ajústela a **true** al llamar al método [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index). Ahora, si su hoja de cálculo de destino es DestSheet, entonces la fuente de datos de su gráfico cambiará de =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**

El siguiente código de ejemplo explica el uso de la propiedad [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) al copiar filas o un rango que contiene gráficos a una nueva hoja de cálculo. El código utiliza el [archivo de Excel de ejemplo](5113699.xlsx) y genera el [archivo de Excel de salida](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
