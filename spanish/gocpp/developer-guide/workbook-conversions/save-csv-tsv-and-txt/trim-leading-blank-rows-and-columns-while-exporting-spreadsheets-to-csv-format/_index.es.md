---
title: Recortar filas y columnas en blanco al exportar hojas de cálculo a formato CSV con Golang mediante C++
linktitle: Recortar filas y columnas vacías iniciales
type: docs
weight: 100
url: /es/go-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aprenda cómo recortar filas y columnas vacías iniciales al exportar hojas de cálculo a formato CSV usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces, su archivo Excel o CSV tiene columnas o filas vacías iniciales. Por ejemplo, considera esta línea:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Aquí las tres primeras celdas o columnas están en blanco. Cuando abres un archivo CSV en Microsoft Excel, Microsoft Excel descarta estas filas y columnas en blanco.

De manera predeterminada, Aspose.Cells no descarta las columnas y filas en blanco al guardar, pero si quieres eliminarlas de la misma manera que lo hace Microsoft Excel, Aspose.Cells proporciona la propiedad [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/). Por favor, configúrala como **true** y entonces todas las filas y columnas en blanco serán descartadas al guardar.

{{% alert color="primary" %}}

Antes del lanzamiento de Aspose.Cells for C++ 20.4, el valor predeterminado de [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) era **false**. Desde el lanzamiento 20.4, el valor predeterminado de [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) es **true.**

{{% /alert %}}

## **Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV**

El siguiente código de muestra carga el [archivo de Excel de origen](sampleTrimBlankColumns.xlsx) que tiene dos columnas en blanco. Primero guarda el archivo de Excel en formato CSV sin cambios y luego configura la propiedad [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) como **true** y lo guarda de nuevo. La captura de pantalla muestra el [archivo de Excel de origen](sampleTrimBlankColumns.xlsx),  el [archivo CSV de salida sin recortar](outputWithoutTrimBlankColumns.csv), y el [archivo CSV de salida con recorte](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCsvFormat.go" >}}
