---
title: Formatear tabla dinámica con Golang vía C++
linktitle: Dar formato a la tabla dinámica
type: docs
weight: 10
url: /es/go-cpp/formatting-pivot-table/
description: Aprende cómo personalizar la apariencia de las tablas dinámicas usando Aspose.Cells for C++.
---

## **Apariencia de la tabla dinámica**

Cómo crear una tabla dinámica explica cómo crear una tabla dinámica simple. Este artículo describe cómo personalizar la apariencia de una tabla dinámica estableciendo diversas propiedades:

- Opciones de formato de tabla dinámica
- Opciones de formato de campos de tabla dinámica
- Opciones de formato de campos de datos

### **Configuración de opciones de formato de tabla dinámica**

La clase [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) controla la tabla dinámica general y se puede formatear de varias maneras.

#### **Establecer el tipo de autoformato**

Microsoft Excel ofrece varias configuraciones de formato preestablecidas para informes. Aspose.Cells también soporta estas opciones de formato. Para acceder a ellas:

1. Establezca [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) en **verdadero**.
1. Asignar una opción de formato de la enumeración [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **Configuración de opciones de formato**

El siguiente ejemplo de código muestra cómo formatear la tabla dinámica para mostrar totales generales para filas y columnas, y cómo establecer el orden de los campos del informe. También muestra cómo establecer una cadena personalizada para valores nulos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **Dar formato manualmente al aspecto visual**

Para formatear manualmente la apariencia del informe de tabla dinámica, en lugar de usar formatos predefinidos, utiliza los métodos [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) y [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). Crea un objeto de estilo para tu formato deseado, por ejemplo:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **Configuración de opciones de formato de campo de tabla dinámica**

La clase [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) representa un campo en una tabla dinámica y se puede formatear de varias formas. El ejemplo de código a continuación muestra cómo:

- Acceder a los campos de fila.
- Establecer subtotales.
- Establecer orden automático.
- Establecer autover.

#### **Configuración de formato de campos de fila/columna/página**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **Configuración de formato de campos de datos**

El ejemplo de código a continuación muestra cómo establecer formatos de visualización y formato numérico para los campos de datos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **Borrado de campos de tabla dinámica**

La clase [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) tiene un método llamado [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) que te permite borrar campos de tabla dinámica. Úsalo cuando quieras borrar todos los campos de tabla dinámica en las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos de tabla dinámica en un área de datos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
