---
title: Trabajar con formatos de visualización de datos de DataField en tabla dinámica
type: docs
weight: 150
url: /es/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells admite todos los formatos de visualización de datos de DataField.

{{% /alert %}}

## **La opción de formato de visualización "Rango de menor a mayor" y "Rango de mayor a menor"**

Aspose.Cells proporciona la capacidad de establecer la opción de formato de visualización para los campos de tabla dinámica. Para esto, la API proporciona la propiedad [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat). Para clasificar de mayor a menor, puede establecer la propiedad [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) a [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK-LARGEST-TO-SMALLEST). El siguiente fragmento de código demuestra cómo establecer las opciones de formato de visualización.

Los archivos de origen y salida de muestra se pueden descargar desde aquí para probar el código de muestra:

[Archivo Excel de origen](PivotTableSample.xlsx)

[Archivo Excel de salida](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
{{< app/cells/assistant language="java" >}}
