---
title: Trabajar con formatos de visualización de datos de DataField en Pivot Table
type: docs
weight: 150
url: /es/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---
{{% alert color="primary" %}}

Aspose.Cells admite todos los formatos de visualización de datos de DataField.

{{% /alert %}}

## **Opción de formato de visualización "Clasificar de menor a mayor" y "Clasificar de mayor a menor"**

Aspose.Cells ofrece la posibilidad de configurar la opción de formato de visualización para los campos dinámicos. Para esto, el API proporciona el[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) propiedad. Para clasificar de mayor a menor, puede configurar el[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat)propiedad a[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST). El siguiente fragmento de código muestra la configuración de las opciones de formato de visualización.

Los archivos fuente y de salida de muestra se pueden descargar desde aquí para probar el código de muestra:

[Archivo Excel de origen](PivotTableSample.xlsx)

[Archivo de Excel de salida](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
