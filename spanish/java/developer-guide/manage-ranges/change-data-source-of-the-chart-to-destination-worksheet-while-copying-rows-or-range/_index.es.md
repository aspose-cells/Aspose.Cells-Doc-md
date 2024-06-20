---
title: Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango
type: docs
weight: 850
url: /es/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Escenarios de uso posibles**
Cuando copias filas o un rango que contiene gráficos a una nueva hoja de trabajo, entonces la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Hoja1!$A$1:$B$4, entonces después de copiar filas o un rango a una nueva hoja de trabajo, la fuente de datos seguirá siendo la misma es decir =Hoja1!$A$1:$ B$4. Todavía se refiere a la hoja de trabajo antigua, es decir, Hoja1. Este también es el comportamiento de Microsoft Excel. Pero si quieres que se refiera a la nueva hoja de trabajo de destino, entonces por favor usa la propiedad CopyOptions.ReferToDestinationSheet y configúrala en verdadero al llamar al método Cells.CopyRows(). Ahora si tu hoja de trabajo de destino es DestSheet, entonces la fuente de datos de tu gráfico cambiará de =Hoja1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.
## **Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**
El siguiente código de muestra explica el uso de la propiedad CopyOptions.ReferToDestinationSheet al copiar filas o rango que contienen un gráfico a una nueva hoja de trabajo. El código utiliza el [archivo de Excel de muestra](5472284.xlsx) y genera el [archivo de Excel de salida](5472283.xlsx). La captura de pantalla muestra que la fuente de datos del gráfico en el [archivo de Excel de salida](5472283.xlsx) ahora se refiere a DestSheet en lugar de Hoja1.

![todo:image_alt_text](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






