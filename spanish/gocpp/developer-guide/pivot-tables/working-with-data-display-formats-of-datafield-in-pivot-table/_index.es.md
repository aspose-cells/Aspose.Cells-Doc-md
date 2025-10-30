---
title: Trabajando con formatos de visualización de datos del campo de datos en la tabla dinámica con Golang a través de C++
linktitle: Trabajando con formatos de visualización de datos en DataField en tablas dinámicas
type: docs
weight: 140
url: /es/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Aprende cómo trabajar con los formatos de visualización de datos en DataField en tablas dinámicas usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells admite todos los formatos de visualización de datos de DataField.

{{% /alert %}}

## **Opción de formato de visualización "Clasificación de menor a mayor" y "Clasificación de mayor a menor"**

Aspose.Cells proporciona la capacidad de configurar la opción de formato de visualización para campos pivote. Para esto, la API ofrece la propiedad [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/). Para clasificar de mayor a menor, puedes establecer la propiedad [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) a [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). El siguiente fragmento de código muestra cómo establecer las opciones de formato de visualización.

Los archivos de origen y salida de muestra se pueden descargar desde aquí para probar el código de muestra:

[Archivo Excel de origen](101089332.xlsx)

[Archivo Excel de salida](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
