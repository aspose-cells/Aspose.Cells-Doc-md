---
title: Cómo gestionar fechas y horas
type: docs
weight: 600
url: /es/net/how-to-manage-dates-and-times/
description: Aprenda a Cómo Administrar Fechas y Horarios a través del Aspose.Cells for .NET API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **Cómo almacenar fechas y horas en Excel**
Las fechas y horas se almacenan en celdas como números. Así, los valores de las celdas que contienen fechas y horas son de tipo numérico. Un número que especifica una fecha y hora consta de los componentes de fecha (parte entera) y hora (parte fraccionaria). La propiedad Cell.DoubleValue devuelve este número.

##  **Cómo mostrar fechas y horas en Aspose.Cells**
Para mostrar un número como fecha y hora, aplique el formato de fecha y hora requerido a una celda a través del[Número de estilo](https://reference.aspose.com/cells/net/aspose.cells/style/number/) o[Estilo.Personalizado]() propiedad. La propiedad CellValue.DateTimeValue devuelve el objeto DateTime, que especifica la fecha y hora representadas por el número contenido en una celda.
<br>
<image src="1.png" width="70%" />

##  **Cómo cambiar dos sistemas de fechas en Aspose.Cells**
MS-Excel almacena las fechas como números que se denominan valores de serie. Un valor de serie es un número entero que es el número de días transcurridos desde el primer día en el sistema de fechas. Excel admite los siguientes sistemas de fechas para valores seriales:

1. El sistema de fechas de 1900. La primera fecha es el 1 de enero de 1900 y su valor de serie es 1. La última fecha es el 31 de diciembre de 9999 y su valor de serie es 2.958.465. Este sistema de fechas se utiliza en el libro de trabajo de forma predeterminada.
1.  El sistema de fechas de 1904. La primera fecha es el 1 de enero de 1904 y su valor de serie es 0. La última fecha es el 31 de diciembre de 9999 y su valor de serie es 2.957.003. Para utilizar este sistema de fechas en el libro de trabajo, configure el[Libro de trabajo.Configuración.Fecha1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) propiedad a verdadera.


Este ejemplo muestra que los valores seriales almacenados en la misma fecha en diferentes sistemas de fechas son diferentes.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Resultado de salida:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **Cómo establecer el valor de fecha y hora en Aspose.Cells**
Este ejemplo establece un valor de Fecha y hora en las celdas A1 y A2, establece el formato personalizado de A1 y el formato numérico de A2 y luego genera los tipos de valor.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Resultado de salida:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **Cómo obtener el valor de fecha y hora en Aspose.Cells**
Este ejemplo establece un valor de Fecha y hora en las celdas A1 y A2, establece el formato personalizado de A1 y el formato numérico de A2, verifica los tipos de valores de dos celdas y luego genera el valor de Fecha y hora y la cadena formateada.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Resultado de salida:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
