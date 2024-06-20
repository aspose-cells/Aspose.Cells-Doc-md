---
title: Eje de fecha
description: Aprenda a gestionar el eje de fecha en Aspose.Cells for .NET. Nuestra guía lo ayudará a comprender cómo trabajar con varios formatos de fecha, escalas de tiempo y frecuencias de etiquetas de marcas de verificación.
keywords: Aspose.Cells for .NET, eje de fecha, gestionar, formatos de fecha, escalas de tiempo, frecuencias de etiquetas de marcas de verificación.
type: docs
weight: 200
url: /es/net/date-axis/
---

## **Escenarios de uso posibles**
Cuando crea un gráfico a partir de datos de la hoja de cálculo que utilizan fechas, y las fechas se trazan a lo largo del eje horizontal (categoría) en el gráfico, Aspose.cells cambia automáticamente el eje de categoría a un eje de fecha (escala de tiempo).
Un eje de fecha muestra fechas en orden cronológico a intervalos específicos o unidades base, como el número de días, meses o años, incluso si las fechas en la hoja de cálculo no están en orden secuencial o en las mismas unidades base.
De forma predeterminada, Aspose.cells determina las unidades base para el eje de fecha en función de la diferencia más pequeña entre dos fechas en los datos de la hoja de cálculo.  Por ejemplo, si tiene datos de precios de acciones donde la diferencia más pequeña entre fechas es de siete días, Excel establece la unidad base en días, pero puede cambiar la unidad base a meses o años si desea ver el rendimiento de la acción durante un período de tiempo más largo.
## **Manejar el eje de fechas como en Microsoft Excel**
Consulte el siguiente código de ejemplo que crea un nuevo archivo de Excel y coloca los valores del gráfico en la primera hoja de cálculo. 
Luego agregamos un gráfico y establecemos el tipo de [**Axis**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
a [**TimeScale**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) y luego establecemos las unidades base en Días.

![todo:image_alt_text](excel.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
