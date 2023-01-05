---
title: Eje de fecha
type: docs
weight: 200
url: /es/net/date-axis/
---
## **Posibles escenarios de uso**
Cuando crea un gráfico a partir de datos de la hoja de trabajo que usa fechas, y las fechas se trazan a lo largo del eje horizontal (categoría) en el gráfico, Aspose.cells cambia automáticamente el eje de categoría a un eje de fecha (escala de tiempo).
Un eje de fechas muestra fechas en orden cronológico en intervalos específicos o unidades base, como el número de días, meses o años, incluso si las fechas en la hoja de trabajo no están en orden secuencial o en las mismas unidades base.
De forma predeterminada, Aspose.cells determina las unidades base para el eje de fechas en función de la diferencia más pequeña entre dos fechas en los datos de la hoja de trabajo. Por ejemplo, si tiene datos de precios de acciones donde la diferencia más pequeña entre fechas es de siete días, Excel establece la unidad base en días, pero puede cambiar la unidad base a meses o años si desea ver el rendimiento de las acciones a lo largo del tiempo. un período de tiempo más largo.
## **Manejar eje de fecha como Microsoft Excel**
 Consulte el siguiente código de muestra que crea un nuevo archivo de Excel y coloca los valores del gráfico en la primera hoja de cálculo.
 Luego agregamos un gráfico y establecemos el tipo de[**Eje**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 a[**Escala de tiempo**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) y luego establezca las unidades base en Días.

![todo:imagen_alternativa_texto](excel.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
