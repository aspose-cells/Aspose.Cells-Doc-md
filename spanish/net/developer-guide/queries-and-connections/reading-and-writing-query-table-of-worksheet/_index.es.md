---
title: Leer y Escribir Tabla de Consulta de Hoja de Cálculo
type: docs
weight: 40
url: /es/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la colección Worksheet.QueryTables que devuelve el objeto de tipo QueryTable por índice. Tiene las siguientes dos propiedades

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Ambos son valores booleanos. Puedes verlos en Microsoft Excel a través de Datos > Conexiones > Propiedades.

{{% /alert %}}

## Lectura y Escritura de Tabla de Consulta de Hoja de Cálculo

El siguiente código de ejemplo lee la primera QueryTable de la primera hoja de cálculo y luego imprime ambas propiedades de QueryTable. Luego establece QueryTable.PreserveFormatting en verdadero.

Puedes descargar el archivo de Excel fuente utilizado en este código y el archivo de Excel de salida generado por el código desde los siguientes enlaces.

- [Archivo de Excel Fuente](5115533.xlsx)
- [Archivo de Excel de Salida](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Salida en Consola

Aquí está la salida de la consola del código de ejemplo anterior

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recuperar rango de resultados de tabla de consulta

Aspose.Cells proporciona la opción de leer la dirección, es decir, el rango de resultados de celdas para una tabla de consulta. El siguiente código demuestra esta función leyendo la dirección del rango de resultados para una tabla de consulta. El archivo de ejemplo se puede descargar [aquí](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
