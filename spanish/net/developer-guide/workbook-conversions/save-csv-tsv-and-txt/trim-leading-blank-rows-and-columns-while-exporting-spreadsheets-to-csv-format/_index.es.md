---
title: Recortar Filas y Columnas en Blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 100
url: /es/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Escenarios de uso posibles**

A veces, tu archivo de Excel o CSV tiene columnas o filas en blanco al principio. Por ejemplo, considera esta línea

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Aquí las tres primeras celdas o columnas están en blanco. Cuando abres un archivo CSV en Microsoft Excel, Microsoft Excel descarta estas filas y columnas en blanco.

De manera predeterminada, Aspose.Cells no descarta las columnas y filas en blanco al guardar, pero si quieres eliminarlas de la misma manera que lo hace Microsoft Excel, Aspose.Cells proporciona la propiedad [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn). Por favor, configúrala como **true** y entonces todas las filas y columnas en blanco serán descartadas al guardar.

{{% alert color="primary" %}}

Antes del lanzamiento de Aspose.Cells for .NET 20.4, el valor predeterminado de [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) era **falso**. Desde el lanzamiento 20.4, el valor predeterminado de [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) es **verdadero.**

{{% /alert %}}

## **Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV**

El siguiente código de muestra carga el [archivo de Excel de origen](sampleTrimBlankColumns.xlsx) que tiene dos columnas en blanco. Primero guarda el archivo de Excel en formato CSV sin cambios y luego configura la propiedad [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) como **true** y lo guarda de nuevo. La captura de pantalla muestra el [archivo de Excel de origen](sampleTrimBlankColumns.xlsx),  el [archivo CSV de salida sin recortar](outputWithoutTrimBlankColumns.csv), y el [archivo CSV de salida con recorte](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
