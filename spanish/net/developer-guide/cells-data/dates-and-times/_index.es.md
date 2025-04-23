---
title: Cómo Gestionar Fechas y Horas
type: docs
weight: 600
url: /es/net/how-to-manage-dates-and-times/
description: Aprende cómo gestionar fechas y horas a través de la API Aspose.Cells for .NET.
keywords: Cómo gestionar fechas y horas, sistema de fecha 1900, sistema de fecha 1904, establecer fechas y horas, obtener fechas y horas, gestionar fechas y horas, almacenar fechas y horas en Excel, mostrar fechas y horas en celdas.
---

## **Cómo almacenar fechas y horas en Excel**
Las fechas y horas se almacenan en las celdas como números. Por lo tanto, los valores de las celdas que contienen fechas y horas son de tipo numérico. Un número que especifica una fecha y hora consta de los componentes de la fecha (parte entera) y la hora (parte fraccionaria). La propiedad Cell.DoubleValue devuelve este número.

## **Cómo mostrar fechas y horas en Aspose.Cells**
Para mostrar un número como una fecha y hora, aplica el formato de fecha y hora requerido a una celda a través de la propiedad [Style.Number](https://reference.aspose.com/cells/net/aspose.cells/style/number/) o [Style.Custom](). La propiedad CellValue.DateTimeValue devuelve el objeto DateTime, que especifica la fecha y hora representadas por el número contenido en una celda.
<br>
<image src="1.png" width="70%" />

## **Cómo cambiar dos sistemas de fecha en Aspose.Cells**
MS-Excel almacena fechas como números que se llaman valores seriales. Un valor serial es un entero que representa el número de días transcurridos desde el primer día en el sistema de fecha. Excel admite los siguientes sistemas de fecha para los valores seriales:

1. El sistema de fecha 1900. La primera fecha es el 1 de enero de 1900 y su valor serial es 1. La última fecha es el 31 de diciembre de 9999 y su valor serial es 2,958,465. Este sistema de fecha se utiliza en el libro de trabajo de forma predeterminada.
1. El sistema de fecha 1904. La primera fecha es el 1 de enero de 1904 y su valor serial es 0. La última fecha es el 31 de diciembre de 9999 y su valor serial es 2,957,003. Para utilizar este sistema de fecha en el libro de trabajo, establece la propiedad [Workbook.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) en true.


Este ejemplo muestra que los valores seriales almacenados en la misma fecha en diferentes sistemas de fecha son diferentes.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Resultado de la salida:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Cómo establecer el valor de fecha y hora en Aspose.Cells**
Este ejemplo establece un valor de fecha y hora en la celda A1 y A2, establece el formato personalizado de A1 y el formato numérico de A2, y luego muestra los tipos de valor.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Resultado de la salida:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Cómo obtener el valor de fecha y hora en Aspose.Cells**
Este ejemplo establece un valor de fecha y hora en la celda A1 y A2, establece el formato personalizado de A1 y el formato numérico de A2, comprueba los tipos de valor de las dos celdas, y luego muestra el valor de fecha y hora y la cadena formateada.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Resultado de la salida:
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
{{< app/cells/assistant language="csharp" >}}
