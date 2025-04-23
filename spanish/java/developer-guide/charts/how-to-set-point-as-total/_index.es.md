---
title: Cómo establecer un punto como total
description: En algunos gráficos de Excel, por ejemplo, gráfico Waterfall, puede ser necesario establecer un punto como total. Este artículo describe cómo usar Aspose.Cells para hacerlo. 
keywords: Gráfico WaterFall, Punto, Establecer como total.
type: docs
weight: 72
url: /es/java/how-to-set-point-as-total/
---

## ¿Qué es "Establecer punto como total" en el gráfico de Excel?

En algunos gráficos de Excel, por ejemplo, gráficos WaterFall, algunos datos de puntos son la suma de los puntos anteriores, puede que necesite "establecer el punto como total". Mostraremos el código de ejemplo y la ilustración a continuación.

## Un gráfico WaterFall necesita "Establecer punto como total" 

![todo:image_alt_text](set-as-total1.png)

Esta imagen muestra un gráfico WaterFall en Excel. Podemos ver que hay cuatro puntos de datos que comienzan con "Total", y se usan para contar todos los datos anteriores.
En esta imagen, la configuración no es exactamente correcta, cuando seleccionamos un punto "Total 2024" y podemos ver que la opción "Establecer como total" no está marcada en Excel.
Adjunto abajo está el [archivo de Excel de muestra](SampleSheet.xlsx) que necesita ser modificado, y usaremos Aspose.Cells para configurarlo correctamente.

## Usar Aspose.Cells para "Establecer punto como total" 

Usamos el siguiente código para configurar el archivo correctamente:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Set-point-as-total.java" >}}

Puedes obtener el siguiente [archivo de salida correcto](output.xlsx)

Como se muestra en la figura a continuación, los cuatro puntos de datos "Total" están configurados correctamente, y puedes ver la diferencia respecto a la gráfica anterior.

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="java" >}}
