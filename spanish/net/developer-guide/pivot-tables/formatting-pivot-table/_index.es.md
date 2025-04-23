---
title: Dar formato a la tabla dinámica
type: docs
weight: 10
url: /es/net/formatting-pivot-table/
---

## **Apariencia de la tabla dinámica**

Cómo crear una tabla dinámica explica cómo crear una tabla dinámica simple. Este artículo describe cómo personalizar la apariencia de una tabla dinámica estableciendo diversas propiedades:

- Opciones de formato de tabla dinámica
- Opciones de formato de campos de tabla dinámica
- Opciones de formato de campos de datos

### **Configuración de opciones de formato de tabla dinámica**

La clase [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) controla la tabla dinámica general y se puede formatear de varias maneras.

#### **Establecer el tipo de autoformato**

Microsoft Excel ofrece varios formatos de informe predefinidos. Aspose.Cells también admite estas opciones de formato. Para acceder a ellas:

1. Establezca [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) en **verdadero**.
1. Asignar una opción de formato de la enumeración [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Configuración de opciones de formato**

El ejemplo de código a continuación muestra cómo dar formato a la tabla dinámica para mostrar totales generales para filas y columnas, y cómo establecer el orden de los campos del informe. También muestra cómo establecer una cadena personalizada para los valores nulos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Dar formato manualmente al aspecto visual**

Para dar formato manualmente al informe de la tabla dinámica en lugar de usar formatos de informe preestablecidos, use los métodos [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) y [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall). Cree un objeto de estilo para el formato deseado, por ejemplo:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Configuración de opciones de formato de campo de tabla dinámica**

La clase [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representa un campo en una tabla dinámica y se puede formatear de varias formas. El ejemplo de código a continuación muestra cómo:

- Acceder a los campos de fila.
- Establecer subtotales.
- Establecer orden automático.
- Establecer autover.

#### **Configuración de formato de campos de fila/columna/página**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Configuración de formato de campos de datos**

El ejemplo de código a continuación muestra cómo establecer formatos de visualización y formato numérico para los campos de datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Borrado de campos de tabla dinámica**

La clase [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) tiene un método llamado [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) que te permite borrar campos de tabla dinámica. Úsalo cuando quieras borrar todos los campos de tabla dinámica en las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos de tabla dinámica en un área de datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
