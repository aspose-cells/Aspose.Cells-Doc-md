---
title: Cambie la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango
type: docs
weight: 850
url: /es/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Posibles escenarios de uso**
Cuando copia filas o rangos que contienen gráficos en una nueva hoja de trabajo, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es =Hoja1!$A$1:$B$4, luego de copiar las filas o el rango a la nueva hoja de trabajo, la fuente de datos seguirá siendo la misma, es decir, =Hoja1!$A$1:$B$4. Todavía se refiere a la hoja de trabajo anterior, es decir, Sheet1. Este es también el comportamiento de Excel Microsoft. Pero si desea que se refiera a una nueva hoja de cálculo de destino, utilice la propiedad CopyOptions.ReferToDestinationSheet y configúrela como verdadera mientras llama al método Cells.CopyRows(). Ahora, si su hoja de cálculo de destino es DestSheet, la fuente de datos de su gráfico cambiará de =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.
## **Cambie la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**
 El siguiente código de ejemplo explica el uso de la propiedad CopyOptions.ReferToDestinationSheet al copiar filas o rangos que contienen un gráfico en una nueva hoja de trabajo. El código utiliza el[ejemplo de archivo de Excel](5472284.xlsx) y genera la[archivo de salida de Excel](5472283.xlsx) . La captura de pantalla muestra que la fuente de datos del gráfico en[archivo de salida de Excel](5472283.xlsx) ahora se refiere a DestSheet en lugar de Sheet1.

![todo:imagen_alternativa_texto](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






