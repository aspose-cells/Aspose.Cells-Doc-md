---
title: Exportar datos de Excel a DataTable y comprobar el tipo de datos mixto
type: docs
weight: 280
url: /es/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Aprende cómo exportar datos de Excel a DataTable y verificar el tipo de datos mixto a través de la API Aspose.Cells for .NET.
keywords: Exportar datos de Excel a DataTable y verificar el tipo de datos mixto, Exportar datos del libro de Excel a DataTable y verificar el tipo de datos mixto, Exportar datos a DataTable y verificar el tipo de datos mixto, Exportar datos de hoja de cálculo a DataTable y verificar el tipo de datos mixto.
---

## **Escenarios de uso posibles**
Si una columna contiene datos de varios tipos, el programa lanzará una excepción de tipo al exportar datos a un DataTable. Para la exportación de la tabla de datos, de forma predeterminada, Aspose.Cells evalúa el tipo de datos para los valores basándose en el primer valor (celda) en la columna. Entonces, si el valor es numérico, significa que el tipo de datos de la columna sería numérico, lo cual es razonable. Si el primer valor es numérico pero hay datos alfanuméricos o valores en la columna, se debe asignar un tipo de datos de cadena. Para hacer frente a esto, por favor use [ExportDataTable overload](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) que implica [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) e intente establecer el atributo Boolean [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) en "Verdadero" si una columna tiene valores numéricos y de cadena para escapar del error.

## **Exportar datos de Excel a DataTable y comprobar el tipo de datos mixtos**

El siguiente ejemplo explica el uso de la propiedad [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) para exportar datos de Excel a una tabla de datos. Consulte el [archivo de Excel de ejemplo](sample.xlsx), su captura de pantalla y la salida de la consola para obtener una referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **Captura de pantalla**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Salida de la consola**

A continuación se muestra la salida de depuración de la consola del código de ejemplo anterior

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
