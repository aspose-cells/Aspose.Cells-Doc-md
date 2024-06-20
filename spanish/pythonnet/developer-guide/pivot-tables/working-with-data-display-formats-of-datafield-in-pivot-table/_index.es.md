---
title: Trabajar con formatos de visualización de datos de DataField en tabla dinámica
type: docs
weight: 140
url: /es/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Cómo trabajar con formatos de visualización de datos de DataField en una tabla dinámica con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca Python de Excel, Trabajar con formatos de visualización de datos de DataField en tabla dinámica.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET admite todos los formatos de visualización de datos de DataField.

{{% /alert %}}

## **Cómo configurar la opción de formato de visualización "Clasificar de menor a mayor" y "Clasificar de mayor a menor"**

Aspose.Cells para Python via .NET proporciona la capacidad de establecer la opción de formato de visualización para los campos de tabla dinámica. Para esto, la API proporciona la propiedad [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/). Para clasificar de mayor a menor, puede establecer la propiedad [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) en [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/). El siguiente fragmento de código demuestra cómo establecer las opciones de formato de visualización.

Los archivos de origen y salida de muestra se pueden descargar desde aquí para probar el código de muestra:

[Archivo Excel de origen](101089332.xlsx)

[Archivo Excel de salida](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
