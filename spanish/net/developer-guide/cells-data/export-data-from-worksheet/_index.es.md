---
title: Exportar datos de la hoja de trabajo en .NET
linktitle: Exportar datos desde la hoja de trabajo
type: docs
weight: 180
url: /es/net/export-data-from-worksheet/
description: Este artículo explica cómo exportar o importar datos de una hoja de trabajo a una tabla de datos usando C#.
---
## Descripción general

Este artículo explica cómo exportar los datos de su hoja de trabajo a DataTable usando C#. Cubre los siguientes temas

_Formato_: **Sobresalir**
- [C# Excel a tabla de datos](#csharp-excel-to-datatable)
- [C# Convertir Excel a DataTable](#csharp-convert-excel-to-datatable)
- [C# Importar Excel a DataTable](#csharp-import-excel-to-datatable)
- [C# Exportar a DataTable desde Excel](#csharp-export-to-datatable-from-excel)

_Formato_: **XLS**
- [C# XLS a tabla de datos](#csharp-xls-to-datatable)
- [C# Convertir XLS a DataTable](#csharp-convert-xls-to-datatable)
- [C# Importar XLS a DataTable](#csharp-import-xls-to-datatable)
- [C# Exportar a DataTable desde XLS](#csharp-export-to-datatable-from-xls)

_Formato_: **XLSX**
- [C# XLSX a tabla de datos](#csharp-xlsx-to-datatable)
- [C# Convertir XLSX a DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importar XLSX a DataTable](#csharp-import-xlsx-to-datatable)
- [C# Exportar a DataTable desde XLSX](#csharp-export-to-datatable-from-xlsx)

_Formato_: **ODS**
- [C# ODS a tabla de datos](#csharp-ods-to-datatable)
- [C# Convertir ODS a DataTable](#csharp-convert-ods-to-datatable)
- [C# Importar ODS a DataTable](#csharp-import-ods-to-datatable)
- [C# Exportar a DataTable desde ODS](#csharp-export-to-datatable-from-ods)

## **C# Exportar datos de Excel**

{{% alert color="primary" %}}

Este artículo analiza algunas técnicas de exportación de datos a las que los desarrolladores tienen acceso a través del Aspose.Cells.

{{% /alert %}}

## **Exportar datos desde la hoja de trabajo**

 Aspose.Cells no solo facilita a sus usuarios importar datos a hojas de trabajo desde fuentes de datos externas, sino que también les permite exportar sus datos de hojas de trabajo a un[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Como sabemos que[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) es la parte de ADO.NET y se utiliza para almacenar datos. Una vez que los datos se almacenan en un[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , se puede utilizar de cualquier manera según los requisitos de los usuarios. Los desarrolladores también pueden almacenar estos datos (almacenados en[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) directamente a una base de datos si así lo desean. Entonces, podemos ver que se vuelve más fácil para los desarrolladores manipular los datos de la hoja de trabajo si se exportan a un[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Exportación de datos a DataTable usando Aspose.Cells**

 Los desarrolladores pueden exportar fácilmente los datos de su hoja de trabajo a un[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) objeto llamando a cualquiera[**ExportDataTableExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) o[**ExportDataTableAsStringExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)clase. Ambos métodos se utilizan en diferentes escenarios, que se analizan a continuación con más detalle.

## **Columnas que contienen datos fuertemente tipados**

Sabemos que una hoja de cálculo almacena datos como una secuencia de filas y columnas. Si todos los valores en las columnas de una hoja de trabajo están fuertemente tipados (eso significa que todos los valores en una columna deben tener el mismo tipo de datos), entonces podemos exportar el contenido de la hoja de trabajo llamando a la[**ExportDataTableExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) clase.[**ExportDataTableExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) El método toma los siguientes parámetros para exportar datos de la hoja de trabajo como[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)objeto:

- **Numero de fila**, se exportará el número de fila de los datos de la primera celda.
- **número de columna**, el número de columna de la primera celda desde la que se exportarán los datos.
- **Número de filas**, el número de filas para exportar.
- **Número de columnas**, el número de columnas a exportar.
- **Exportar nombres de columnas** , una propiedad booleana que indica si los datos de la primera fila de la hoja de cálculo deben exportarse como nombres de columna de la[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)O no.

_Pasos: exportar datos a DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Pasos:</em> Excel a DataTable en C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Pasos:</em> XLS a DataTable en C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Pasos:</em> XLSX a DataTable en C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Pasos:</em> ODS a DataTable en C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Pasos:</em> Convertir Excel a DataTable en C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Pasos:</em>Convertir XLS a DataTable en C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Pasos:</em>Convertir XLSX a DataTable en C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Pasos:</em>Convertir ODS a DataTable en C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Pasos:</em> Importar Excel a DataTable en C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Pasos:</em> Importar XLS a DataTable en C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Pasos:</em> Importar XLSX a DataTable en C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Pasos:</em> Importar ODS a DataTable en C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Pasos:</em> Exportar a DataTable desde Excel en C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Pasos:</em> Exportar a DataTable desde XLS en C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Pasos:</em> Exportar a DataTable desde XLSX en C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Pasos:</em> Exportar a DataTable desde ODS en C#</strong></a>

_Pasos del código:_

1.  Cargue su archivo de Excel en[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook/) objeto.
   - [Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook/) El objeto puede cargar formatos de archivo de Excel, por ejemplo, XLS, XLSX, XLSM, ODS, etc.
 3. Accede a la primera[Hoja de cálculo](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) en el archivo de Excel.
 4. Elija su área de exportación, por ejemplo, 7 filas y 2 columnas a partir de la primera celda de**Tabla de datos**.
 5. Uso[ExportDataTableExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) método para exportar los datos a DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Columnas que contienen datos no fuertemente tipados**

 Si todos los valores en las columnas de una hoja de trabajo no están fuertemente tipados (eso significa que los valores en una columna pueden tener diferentes tipos de datos), entonces podemos exportar el contenido de la hoja de trabajo llamando a la[**ExportDataTableAsStringExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) clase.[**ExportDataTableAsStringExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)El método toma el mismo conjunto de parámetros que el del[**ExportDataTableExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)método para exportar datos de la hoja de trabajo como un[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)objeto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Exportar rango con bandera para omitir el nombre de la columna**

Los datos de un rango se pueden exportar a[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) donde hay un indicador disponible para omitir la fila del encabezado en los datos exportados. El siguiente código exporta un rango de datos a[**Tabla de datos**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) con un argumento[**ExportTableOptionsExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) que contiene[**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) bandera. está configurado para**verdadero** si la información del encabezado está allí, por lo tanto, no se incluirá en los datos y se establecerá en**falso** si no hay encabezado y todas las filas se deben considerar como datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Temas avanzados**
- [Exportar datos de Excel a DataTable sin ningún formato](/cells/es/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exportar HTML Valor de cadena de Cells a DataTable](/cells/es/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exportar datos de filas visibles desde la hoja de trabajo](/cells/es/net/export-visible-rows-data-from-worksheet/)
- [Ignorar columnas ocultas al exportar datos de la hoja de trabajo a la tabla de datos](/cells/es/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Cambie el nombre de las columnas duplicadas automáticamente al exportar datos de la hoja de trabajo](/cells/es/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
