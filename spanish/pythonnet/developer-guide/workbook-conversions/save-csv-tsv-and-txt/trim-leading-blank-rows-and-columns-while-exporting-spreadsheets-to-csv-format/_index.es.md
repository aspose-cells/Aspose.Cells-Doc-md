---
title: Recortar Filas y Columnas en Blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 100
url: /es/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Recortar Filas y Columnas en Blanco al exportar hojas de cálculo al formato CSV utilizando Aspose.Cells para Python via .NET API.
keywords: Python Recortar Filas y Columnas en Blanco al exportar hojas de cálculo al formato CSV, Recortar Filas y Columnas en Blanco al guardar excel al formato CSV en Python via NET, Python Recortar Filas y Columnas en Blanco al exportar excel al formato CSV.
---

## **Escenarios de uso posibles**

A veces, tu archivo de Excel o CSV tiene columnas o filas en blanco al principio. Por ejemplo, considera esta línea

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Aquí las tres primeras celdas o columnas están en blanco. Cuando abres un archivo CSV en Microsoft Excel, Microsoft Excel descarta estas filas y columnas en blanco.

Por defecto, Aspose.Cells para Python via .NET no descarta las columnas y filas en blanco al inicio al guardar, pero si desea eliminarlas como lo hace Microsoft Excel, entonces Aspose.Cells para Python via .NET proporciona la propiedad [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/). Por favor ajústelo a **true** y luego todas las filas y columnas en blanco al inicio se descartarán al guardar.

{{% alert color="primary" %}}

Antes del lanzamiento de Aspose.Cells for Python via .NET 20.4, el valor predeterminado de [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) era **falso**. Desde el lanzamiento 20.4, el valor predeterminado de [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) es **verdadero.**

{{% /alert %}}

## **Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV**

El siguiente código de muestra carga el [archivo de Excel de origen](sampleTrimBlankColumns.xlsx) que tiene dos columnas en blanco. Primero guarda el archivo de Excel en formato CSV sin cambios y luego configura la propiedad [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) como **true** y lo guarda de nuevo. La captura de pantalla muestra el [archivo de Excel de origen](sampleTrimBlankColumns.xlsx),  el [archivo CSV de salida sin recortar](outputWithoutTrimBlankColumns.csv), y el [archivo CSV de salida con recorte](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
