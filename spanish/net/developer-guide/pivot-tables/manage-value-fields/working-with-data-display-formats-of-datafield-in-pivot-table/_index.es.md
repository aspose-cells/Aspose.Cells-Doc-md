---
title: Trabajar con formatos de visualización de datos de DataField en tabla dinámica
type: docs
weight: 140
url: /es/net/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells admite todos los formatos de visualización de datos de DataField.

{{% /alert %}}

## **La opción de formato de visualización "Rango de menor a mayor" y "Rango de mayor a menor"**

Aspose.Cells proporciona la capacidad de establecer la opción de formato de visualización para los campos de tabla dinámica. Para esto, la API proporciona la propiedad [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/). Para ordenar de mayor a menor, puede establecer la propiedad [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/) en [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfielddatadisplayformat). El siguiente fragmento de código demuestra cómo establecer las opciones de formato de visualización.

Los archivos de origen y salida de muestra se pueden descargar desde aquí para probar el código de muestra:

[Archivo Excel de origen](101089332.xlsx)

[Archivo Excel de salida](101089333.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTables-PivotTableDataDisplayFormatRanking-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
