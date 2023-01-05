---
title: Formato de tabla dinámica
type: docs
weight: 10
url: /es/net/formatting-pivot-table/
---
## **Aspecto de la tabla dinámica**

Cómo crear una tabla dinámica explica cómo crear una tabla dinámica simple. Este artículo describe cómo personalizar la apariencia de una tabla dinámica configurando varias propiedades:

- Opciones de formato de tabla dinámica
- Opciones de formato de campos dinámicos
- Opciones de formato de campo de datos

### **Configuración de opciones de formato de tabla dinámica**

 Él[**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)La clase controla la tabla dinámica general y se puede formatear de varias maneras.

#### **Configuración del tipo de formato automático**

Microsoft Excel ofrece varios formatos de informe preestablecidos diferentes. Aspose.Cells también admite estas opciones de formato. Para acceder a ellos:

1.  Colocar[**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) a**verdadero**.
1.  Asigne una opción de formato de la[**Tipo de formato automático de tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)enumeración.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Configuración de las opciones de formato**

El ejemplo de código a continuación muestra cómo formatear la tabla dinámica para mostrar los totales generales de filas y columnas, y cómo establecer el orden de los campos del informe. También muestra cómo configurar una cadena de cliente para valores nulos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Dar formato a Look and Feel manualmente**

 Para dar formato al aspecto del informe de la tabla dinámica de forma manual, en lugar de utilizar formatos de informe preestablecidos, utilice el[**Tabla dinámica.Formato()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) y[**Tabla dinámica.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)métodos. Cree un objeto de estilo para el formato deseado, por ejemplo:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Configuración de opciones de formato de campo pivote**

 Él[**campo pivote**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)class representa un campo en una tabla dinámica y se puede formatear de varias maneras. El ejemplo de código a continuación muestra cómo:

- Acceder a campos de fila.
- Configuración de subtotales.
- Configuración de ordenación automática.
- Configuración de exhibición automática.

#### **Configuración del formato de campos de fila/columna/página**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Configuración del formato de los campos de datos**

El ejemplo de código a continuación muestra cómo configurar los formatos de visualización y el formato numérico para los campos de datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Borrado de campos pivote**

 Él[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) tiene un método llamado[**Claro()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)que le permite borrar campos pivote. Úselo cuando desee borrar todos los campos dinámicos en las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos dinámicos en un área de datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
