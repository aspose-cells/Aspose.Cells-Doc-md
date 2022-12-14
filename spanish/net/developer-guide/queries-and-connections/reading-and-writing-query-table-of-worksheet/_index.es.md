---
title: Tabla de consulta de lectura y escritura de la hoja de trabajo
type: docs
weight: 40
url: /es/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells proporciona la colección Worksheet.QueryTables que devuelve el objeto de tipo QueryTable por índice. tiene las siguientes dos propiedades

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Ambos son valores booleanos. Puede verlos en Microsoft Excel a través de Datos > Conexiones > Propiedades.

{{% /alert %}}

## Tabla de consulta de lectura y escritura de la hoja de trabajo

El siguiente código de ejemplo lee la primera QueryTable de la primera hoja de cálculo y luego imprime ambas propiedades de QueryTable. Luego establece QueryTable.PreserveFormatting en verdadero.

Puede descargar el archivo de origen de Excel utilizado en este código y el archivo de salida de Excel generado por el código desde los siguientes enlaces.

- [Archivo Excel de origen](5115533.xlsx)
- [Archivo de Excel de salida](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Salida de consola

Aquí está la salida de la consola del código de muestra anterior

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recuperar el rango de resultados de la tabla de consulta

 Aspose.Cells ofrece la opción de leer la dirección, es decir, el rango de resultados de las celdas para una tabla de consulta. El siguiente código demuestra esta característica al leer la dirección del rango de resultados para una tabla de consulta. El archivo de muestra se puede descargar[aquí](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
