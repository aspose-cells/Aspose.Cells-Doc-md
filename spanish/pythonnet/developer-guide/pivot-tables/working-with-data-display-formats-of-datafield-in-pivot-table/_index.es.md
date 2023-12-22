---
title: Trabajar con formatos de visualización de datos de DataField en tabla dinámica
type: docs
weight: 140
url: /es/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Cómo trabajar con formatos de visualización de datos de DataField en tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Work with data display formats of DataField in Pivot Table.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET admite todos los formatos de visualización de datos de DataField.

{{% /alert %}}

##  **Opción de formato de visualización "Clasificar de menor a mayor" y "Clasificar de mayor a menor"**

Aspose.Cells for Python via .NET proporciona la posibilidad de configurar la opción de formato de visualización para campos dinámicos. Para ello, el API proporciona la[**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) propiedad. Para clasificar de mayor a menor, puede configurar el[**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/)propiedad a[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/). El siguiente fragmento de código demuestra la configuración de las opciones de formato de visualización.

Se pueden descargar archivos fuente y de salida de muestra desde aquí para probar el código de muestra:

[Archivo Excel de origen](101089332.xlsx)

[Archivo de Excel de salida](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
