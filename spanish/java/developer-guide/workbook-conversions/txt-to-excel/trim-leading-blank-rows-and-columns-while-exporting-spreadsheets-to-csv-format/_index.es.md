---
title: Recortar Filas y Columnas en Blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 50
url: /es/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Escenarios de uso posibles**

A veces, tu archivo de Excel o CSV tiene columnas o filas en blanco al principio. Por ejemplo, considera esta línea

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Aquí las tres primeras celdas o columnas están en blanco. Cuando abres un archivo CSV en Microsoft Excel, Microsoft Excel descarta estas filas y columnas en blanco.

De manera predeterminada, Aspose.Cells no descarta las columnas y filas en blanco al guardar, pero si quieres eliminarlas de la misma manera que lo hace Microsoft Excel, Aspose.Cells proporciona la propiedad [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn). Por favor, configúrala como **true** y entonces todas las filas y columnas en blanco serán descartadas al guardar.

{{% alert color="primary" %}}

Antes del lanzamiento de Aspose.Cells for .NET 20.4, el valor predeterminado de [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) era **falso**. Desde el lanzamiento 20.4, el valor predeterminado de [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) es **verdadero.**

{{% /alert %}}

## **Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV**

El siguiente código de muestra carga el archivo de Excel fuente que tiene dos columnas en blanco al principio. Primero guarda el archivo de Excel en formato CSV sin cambios y luego establece la propiedad [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) a **true** y lo guarda nuevamente. La captura de pantalla muestra el [archivo de Excel fuente](sampleTrimBlankColumns.xlsx), el [archivo CSV de salida sin recortar](outputWithoutTrimBlankColumns.csv) y el [archivo CSV de salida con recorte](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}
