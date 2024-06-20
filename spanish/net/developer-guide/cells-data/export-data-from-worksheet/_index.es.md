---
title: Exportar datos desde la hoja de cálculo en .NET
linktitle: Exportar datos desde la hoja de cálculo
type: docs
weight: 180
url: /es/net/export-data-from-worksheet/
description: Este artículo explica cómo exportar o importar datos desde una hoja de cálculo a una tabla utilizando C#.
keywords: Exportar datos desde la hoja de cálculo en C#, Exportar datos a DataTable en C#, Columnas que contienen datos fuertemente tipados, Columnas que contienen datos no fuertemente tipados, C# Exportar rango con indicador para omitir el nombre de la columna, C# Cómo exportar rango con encabezado.
---

## Resumen

Este artículo explica cómo exportar los datos de su hoja de cálculo a DataTable utilizando C#. Cubre los siguientes temas

_Formato_: **Excel**
- [C# Excel a DataTable](#csharp-excel-to-datatable)
- [C# Convertir Excel a DataTable](#csharp-convert-excel-to-datatable)
- [C# Importar Excel a DataTable](#csharp-import-excel-to-datatable)
- [C# Exportar a DataTable desde Excel](#csharp-export-to-datatable-from-excel)

_Formato_: **XLS**
- [C# XLS a DataTable](#csharp-xls-to-datatable)
- [C# Convertir XLS a DataTable](#csharp-convert-xls-to-datatable)
- [C# Importar XLS a DataTable](#csharp-import-xls-to-datatable)
- [C# Exportar a DataTable desde XLS](#csharp-export-to-datatable-from-xls)

_Formato_: **XLSX**
- [C# XLSX a DataTable](#csharp-xlsx-to-datatable)
- [C# Convertir XLSX a DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importar XLSX a DataTable](#csharp-import-xlsx-to-datatable)
- [C# Exportar a DataTable desde XLSX](#csharp-export-to-datatable-from-xlsx)

_Formato_: **ODS**
- [C# ODS a DataTable](#csharp-ods-to-datatable)
- [C# Convertir ODS a DataTable](#csharp-convert-ods-to-datatable)
- [C# Importar ODS a DataTable](#csharp-import-ods-to-datatable)
- [C# Exportar a DataTable desde ODS](#csharp-export-to-datatable-from-ods)

## **Cómo exportar datos de Excel usando C#**

{{% alert color="primary" %}}

Este artículo discute algunas técnicas de exportación de datos a las que los desarrolladores tienen acceso a través de Aspose.Cells.

{{% /alert %}}

## **Cómo exportar datos desde una hoja de cálculo**

Aspose.Cells no solo facilita a sus usuarios importar datos a hojas de cálculo desde fuentes de datos externas, sino que también les permite exportar sus datos de hoja de cálculo a un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). Como sabemos que [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) es parte de ADO.NET y se usa para almacenar datos. Una vez que los datos se almacenan en un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), se pueden utilizar de cualquier manera según los requisitos de los usuarios. Los desarrolladores también pueden almacenar estos datos (almacenados en [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) directamente en una base de datos si lo desean. Por lo tanto, podemos ver que se vuelve más fácil para los desarrolladores manipular los datos de la hoja de cálculo si se exportan a un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Cómo exportar datos a DataTable usando Aspose.Cells**

Los desarrolladores pueden exportar fácilmente sus datos de hoja de cálculo a un objeto [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) llamando ya sea al método [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) o [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Ambos métodos se utilizan en diferentes escenarios, que se discuten a continuación con más detalle.

## **Columnas que contienen datos fuertemente tipados**

Sabemos que una hoja de cálculo almacena datos como una secuencia de filas y columnas. Si todos los valores en las columnas de una hoja de cálculo tienen un tipo de datos fuertemente tipado (lo que significa que todos los valores en una columna deben tener el mismo tipo de datos) entonces podemos exportar el contenido de la hoja de cálculo llamando al método [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). El método [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) toma los siguientes parámetros para exportar los datos de la hoja de cálculo como un objeto [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8):

- **Número de fila**, el número de la primera celda de datos que se exportará.
- **Número de columna**, el número de columna de la primera celda de datos que se exportará.
- **Número de filas**, el número de filas a exportar.
- **Número de columnas**, el número de columnas a exportar.
- **Exportar nombres de columna**, una propiedad booleana que indica si los datos en la primera fila de la hoja de cálculo deben exportarse como nombres de columnas del [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) o no.

Pasos: Exportar datos a un DataTable

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Pasos:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Pasos:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Pasos:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Pasos:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Pasos:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Pasos:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Pasos:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Pasos:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Pasos:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Pasos:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Pasos:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Pasos:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Pasos:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Pasos:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Pasos:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Pasos:</em> Export to DataTable from ODS in C#</strong></a>

_Pasos de código:_

1. Cargue su archivo de Excel en el objeto [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/).
   - El objeto [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) puede cargar formatos de archivo de Excel como XLS, XLSX, XLSM, ODS, etc.
3. Acceda a la primera [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) en el archivo de Excel.
4. Elija su área de exportación, por ejemplo, 7 filas y 2 columnas a partir de la celda 1 de **DataTable**.
5. Utilice el método [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) para exportar los datos a DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Columnas que contienen datos no fuertemente tipados**

Si todos los valores en las columnas de una hoja de cálculo no son fuertemente tipados (eso significa que los valores en una columna pueden tener diferentes tipos de datos), entonces podemos exportar el contenido de la hoja de cálculo llamando al método [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). El método [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) toma el mismo conjunto de parámetros que el método [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) para exportar datos de la hoja de cálculo como un objeto [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Cómo Exportar un Rango con Encabezado**

Se pueden exportar datos de un rango a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) donde hay una bandera disponible para saltar la fila del encabezado en los datos exportados. El siguiente código exporta un rango de datos a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) con un argumento [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) que contiene [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) bandera. Se establece en **true** si hay información de encabezado, por lo tanto, no se incluirá en los datos y se establece en **false** si no hay encabezado y todas las filas se consideran como datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Temas avanzados**
- [Exportar datos de Excel a DataTable sin ningún formato](/cells/es/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exportar cadena HTML del valor de las celdas al DataTable](/cells/es/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exportar datos de filas visibles desde la hoja de cálculo](/cells/es/net/export-visible-rows-data-from-worksheet/)
- [Ignorar columnas ocultas al exportar datos de la hoja de cálculo al DataTable](/cells/es/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Renombrar columnas duplicadas automáticamente al exportar datos de la hoja de cálculo](/cells/es/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
