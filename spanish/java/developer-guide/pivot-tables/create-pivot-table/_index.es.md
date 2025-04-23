---
title: Crear tabla dinámica
type: docs
weight: 10
url: /es/java/create-pivot-table/
---

## **Crear tabla dinámica**

### **Crear tabla dinámica utilizando Aspose.Cells**

{{% alert color="primary" %}}

Con Aspose.Cells, es posible agregar tablas dinámicas a las hojas de cálculo. Aspose.Cells cuenta con varias clases especiales utilizadas específicamente para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y establecer las propiedades de un objeto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), utilizado como los bloques de construcción de la tabla dinámica.

Los objetos de tabla dinámica son:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): representa un campo en una tabla dinámica.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) en la tabla dinámica.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): representa una tabla dinámica.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): representa la colección de todos los objetos de tabla dinámica en la hoja de cálculo.

{{% /alert %}}

### **Crear una tabla dinámica simple**

Para crear una tabla dinámica utilizando Aspose.Cells, siga los pasos a continuación:

1. Agregue algunos datos a las celdas de la hoja de cálculo utilizando el método [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) del objeto [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Estos datos se utilizarán como origen de datos para la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) de la clase [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection), encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. Acceda al objeto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) desde el [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) pasando el índice [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
1. Utilice cualquiera de los objetos de tabla dinámica (explicados anteriormente) encapsulados en el objeto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) para gestionar la tabla dinámica.

{{% alert color="primary" %}}

Al asignar un rango de celdas como origen de datos, el rango debe establecerse desde la esquina superior izquierda hasta la esquina inferior derecha. Por ejemplo, "A1:C3" es válido; "C3:A1" no es válido.

{{% /alert %}}

El ejemplo de código a continuación muestra cómo crear una tabla dinámica simple siguiendo los pasos básicos enumerados anteriormente. Al ejecutar el código, se agrega una tabla dinámica a la hoja de cálculo:

**Creando una tabla dinámica basada en un campo correspondiente**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
