---
title: Exporte datos de Excel a DataTable y verifique el tipo de datos mixtos
type: docs
weight: 280
url: /es/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Aprenda a exportar datos de Excel a DataTable y verificar tipos de datos mixtos a través de Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **Posibles escenarios de uso**
Si una columna contiene datos de varios tipos, el programa generará una excepción de tipo al exportar datos a un DataTable. Para exportar una tabla de datos, de forma predeterminada, Aspose.Cells evalúa el tipo de datos para los valores en función del primer valor (celda) de la columna. Entonces, si el valor es un número, significa que el tipo de datos de la columna sería numérico, lo cual es razonable. Si el primer valor es un número pero hay datos o valores alfanuméricos en la columna, se debe asignar un tipo de datos de cadena. Para afrontarlo, utilice[Sobrecarga de ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) El cual involucra[Exportar opciones de tabla de datos](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) y trata de configurar[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Atributo booleano a "verdadero" si una columna tiene valores numéricos y de cadena para escapar del error.

##  **Exporte datos de Excel a DataTable y verifique el tipo de datos mixtos**

 El siguiente ejemplo explica el uso de[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Propiedad para exportar datos de Excel a la tabla de datos. Por favor vea el[archivo de Excel de muestra](sample.xlsx), su captura de pantalla y la salida de la consola como referencia.

###  **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **Captura de pantalla**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **Salida de consola**

A continuación se muestra el resultado de depuración de la consola del código de muestra anterior.

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
