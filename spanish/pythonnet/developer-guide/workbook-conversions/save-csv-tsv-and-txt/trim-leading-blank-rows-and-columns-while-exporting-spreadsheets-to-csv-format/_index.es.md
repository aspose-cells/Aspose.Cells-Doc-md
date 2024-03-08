---
title: Recorte las filas y columnas en blanco iniciales al exportar hojas de cálculo al formato CSV
type: docs
weight: 100
url: /es/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Recorte las filas y columnas en blanco iniciales mientras exporta hojas de cálculo al formato CSV utilizando Aspose.Cells for Python via .NET API.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **Posibles escenarios de uso**

A veces, su archivo Excel o CSV tiene columnas o filas en blanco al principio. Por ejemplo, considere esta línea

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Aquí las primeras tres celdas o columnas están en blanco. Cuando abre un archivo CSV de este tipo en Microsoft Excel, Microsoft Excel descarta estas filas y columnas en blanco iniciales.

 De forma predeterminada, Aspose.Cells for Python via .NET no descarta las columnas y filas en blanco iniciales al guardar, pero si desea eliminarlas tal como lo hace Microsoft Excel, entonces Aspose.Cells for Python via .NET proporciona**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** propiedad. Por favor configúrelo en**verdadero**y luego todas las primeras filas y columnas en blanco se descartarán al guardar.

{{% alert color="primary" %}}

 Antes del lanzamiento de Aspose.Cells for Python via .NET 20.4, el valor predeterminado de**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**era**FALSO**. Desde la versión 20.4, el valor predeterminado de **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** es**verdadero.**

{{% /alert %}}

##  **Recorte las filas y columnas en blanco iniciales al exportar hojas de cálculo al formato CSV**

 El siguiente código de muestra carga el[archivo excel fuente](sampleTrimBlankColumns.xlsx) que tiene dos columnas en blanco al principio. Primero guarda el archivo Excel en formato CSV sin ningún cambio y luego configura**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** propiedad a**verdadero** y lo guarda de nuevo. La captura de pantalla muestra el[archivo excel fuente](sampleTrimBlankColumns.xlsx), [salida del archivo CSV sin recortar](outputWithoutTrimBlankColumns.csv), y el[salida CSV archivo con recorte](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
