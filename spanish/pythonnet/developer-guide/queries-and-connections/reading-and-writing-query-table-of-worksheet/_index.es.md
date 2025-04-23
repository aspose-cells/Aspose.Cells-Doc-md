---
title: Leer y Escribir Tabla de Consulta de Hoja de Cálculo
type: docs
weight: 40
url: /es/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET proporciona la colección Worksheet.QueryTables que devuelve el objeto QueryTable por índice. Tiene las siguientes dos propiedades.

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Ambos son valores booleanos. Puedes verlos en Microsoft Excel a través de Datos > Conexiones > Propiedades.

{{% /alert %}}

## Lectura y Escritura de Tabla de Consulta de Hoja de Cálculo

El siguiente código de ejemplo lee la primera QueryTable de la primera hoja de cálculo y luego imprime ambas propiedades de QueryTable. Luego establece QueryTable.PreserveFormatting en verdadero.

Puedes descargar el archivo de Excel fuente utilizado en este código y el archivo de Excel de salida generado por el código desde los siguientes enlaces.

- [Archivo de Excel Fuente](5115533.xlsx)
- [Archivo de Excel de Salida](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### Salida en Consola

Aquí está la salida de la consola del código de ejemplo anterior

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recuperar rango de resultados de tabla de consulta

Aspose.Cells para Python via .NET ofrece la opción de leer la dirección, es decir, el rango de resultados de las celdas para una tabla de consulta. El siguiente código demuestra esta función leyendo la dirección del rango de resultados para una tabla de consulta. El archivo de ejemplo se puede descargar [aquí](72417290.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

