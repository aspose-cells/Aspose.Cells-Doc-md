---
title: Obtener Dirección, Cuenta de Celdas, Desplazamiento, Columna Entera y fila Entera del Rango con Golang vía C++
linktitle: Obtener dirección, conteo de celdas, desplazamiento, columna completa y fila completa del rango
type: docs
weight: 330
url: /es/go-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Aprende cómo obtener dirección, conteo de celdas, desplazamiento, columna completa y fila completa de un rango usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona el objeto `Range`, que tiene varios métodos útiles que facilitan trabajar con rangos de Excel. Este artículo ilustra el uso de los siguientes métodos o propiedades del objeto `Range`:

- **Dirección**

  Obtiene la dirección del rango.

- **Recuento de celdas**

  Obtiene el conteo total de celdas en el rango.

- **Desplazamiento**

  Obtiene un rango por desplazamiento.

- **Columna completa**

  Obtiene un objeto `Range` que representa toda la columna (o columnas) que contiene el rango especificado.

- **Fila completa**

  Obtiene un objeto `Range` que representa toda la fila (o filas) que contiene el rango especificado.

## **Obtener dirección, conteo de celdas, desplazamiento, columna completa y fila completa del rango**
El siguiente código de ejemplo explica el uso de los métodos y propiedades discutidos anteriormente. Por favor, vea la salida de consola del código a continuación como referencia.

## **Código de muestra**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.go" >}}
## **Salida de la consola**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
