---
title: Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango
description: Aprende cómo cambiar la fuente de datos de un gráfico a una hoja de cálculo de destino mientras copias filas o un rango en Aspose.Cells para Python via .NET. Nuestra guía te mostrará cómo actualizar el rango de datos del gráfico y enlazarlo a la hoja de cálculo de destino, asegurando que las filas o rangos copiados se reflejen con precisión en el gráfico.
keywords: Aspose.Cells para Python via .NET, gráficos, fuente de datos, hoja de cálculo de destino, filas, rango, copiar, actualizar, rango de datos, enlace.
type: docs
weight: 440
url: /es/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Escenarios de uso posibles**

Cuando copia filas o un rango que contiene gráficos a una nueva hoja de cálculo, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Sheet1!$A$1:$B$4, entonces después de copiar filas o un rango a una nueva hoja de cálculo, la fuente de datos seguirá siendo la misma, es decir, =Sheet1!$A$1:$B$4. Todavía se refiere a la hoja de cálculo antigua, es decir, Sheet1. Esto también es el comportamiento en Microsoft Excel. Pero si desea que haga referencia a la nueva hoja de cálculo de destino, entonces por favor utilice la propiedad [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) y ajústela a **true** al llamar al método [**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows). Ahora, si su hoja de cálculo de destino es DestSheet, entonces la fuente de datos de su gráfico cambiará de =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**

El siguiente código de ejemplo explica el uso de la propiedad [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) al copiar filas o un rango que contiene gráficos a una nueva hoja de cálculo. El código utiliza el [archivo de Excel de ejemplo](5113699.xlsx) y genera el [archivo de Excel de salida](5113697.xlsx).

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
