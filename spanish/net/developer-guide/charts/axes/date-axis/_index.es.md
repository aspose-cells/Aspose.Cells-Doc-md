---
title: Eje de fecha
description: Aprenda a administrar el eje de fechas en Aspose.Cells for .NET. Nuestra guía lo ayudará a comprender cómo trabajar con varios formatos de fecha, escalas de tiempo y frecuencias de etiquetas de marca.
keywords: Aspose.Cells for .NET, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /es/net/date-axis/
---
##  **Posibles escenarios de uso**
Cuando crea un gráfico a partir de datos de una hoja de cálculo que utiliza fechas y las fechas se trazan a lo largo del eje horizontal (categoría) del gráfico, Aspose.cells cambia automáticamente el eje de categoría a un eje de fecha (escala de tiempo).
Un eje de fechas muestra fechas en orden cronológico en intervalos específicos o unidades base, como el número de días, meses o años, incluso si las fechas de la hoja de cálculo no están en orden secuencial ni en las mismas unidades base.
De forma predeterminada, Aspose.cells determina las unidades base para el eje de fechas en función de la diferencia más pequeña entre dos fechas cualesquiera en los datos de la hoja de cálculo. Por ejemplo, si tiene datos sobre los precios de las acciones donde la diferencia más pequeña entre fechas es siete días, Excel establece la unidad base en días, pero puede cambiar la unidad base a meses o años si desea ver el rendimiento de las acciones a lo largo del tiempo. un período de tiempo más largo.
##  **Manejar el eje de fecha como Microsoft Excel**
 Consulte el siguiente código de muestra que crea un nuevo archivo de Excel y coloca los valores del gráfico en la primera hoja de trabajo.
 Luego agregamos un gráfico y configuramos el tipo de[**Eje**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 a[**Escala de tiempo**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) y luego configure las unidades base en Días.

![todo:image_alt_text](excel.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
