---
title: Recorte las filas y columnas en blanco iniciales al exportar hojas de cálculo al formato CSV
type: docs
weight: 100
url: /es/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **Posibles escenarios de uso**

A veces, su archivo de Excel o CSV tiene columnas o filas en blanco al principio. Por ejemplo, considere esta línea

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Aquí las primeras tres celdas o columnas están en blanco. Cuando abre un archivo CSV de este tipo en Microsoft Excel, entonces Microsoft Excel descarta estas filas y columnas en blanco iniciales.

 De forma predeterminada, Aspose.Cells no descarta las columnas y filas en blanco iniciales al guardar, pero si desea eliminarlas como lo hace Microsoft Excel, entonces Aspose.Cells proporciona**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** propiedad. Por favor, configúralo en**verdadero**luego todas las filas y columnas en blanco principales se descartarán al guardar.

{{% alert color="primary" %}}

 Antes del lanzamiento de Aspose.Cells for .NET 20.4, el valor predeterminado de**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** fue**falso** . Desde la versión 20.4, el valor predeterminado de**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** es**verdadero.**

{{% /alert %}}

## **Recorte las filas y columnas en blanco iniciales al exportar hojas de cálculo al formato CSV**

 El siguiente código de ejemplo carga el[archivo fuente excel](sampleTrimBlankColumns.xlsx) que tiene dos columnas principales en blanco. Primero guarda el archivo de Excel en formato CSV sin ningún cambio y luego establece**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)** propiedad a**verdadero** y lo guarda de nuevo. La captura de pantalla muestra la[archivo fuente excel](sampleTrimBlankColumns.xlsx), [archivo de salida CSV sin recortar](outputWithoutTrimBlankColumns.csv), y el[archivo de salida CSV con recorte](outputTrimBlankColumns.csv).

![todo:imagen_alternativa_texto](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
