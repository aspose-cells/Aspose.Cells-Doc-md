---
title: Crear tabla dinámica
type: docs
weight: 10
url: /es/java/create-pivot-table/
---
## **Crear tabla dinámica**

### **Crear tabla dinámica usando Aspose.Cells**

{{% alert color="primary" %}}

 Con Aspose.Cells, es posible agregar tablas dinámicas a las hojas de cálculo. Aspose.Cells tiene varias clases especiales que se usan específicamente para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y establecer las propiedades de un[**Tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)objeto, utilizado como los bloques de construcción de la tabla dinámica.

Los objetos de la tabla dinámica son:

- [**campo pivote**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): representa un campo en una tabla dinámica.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) : representa una colección de todos los[**campo pivote**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)objetos en la tabla dinámica.
- [**Tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): representa una tabla dinámica.
- [**Colección de tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): representa la colección de todos los objetos de la tabla dinámica en la hoja de trabajo.

{{% /alert %}}

### **Crear una tabla dinámica simple**

Para crear una tabla dinámica usando Aspose.Cells, siga los pasos a continuación:

1.  Agregue algunos datos a las celdas de la hoja de trabajo usando el[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) objetos[**valor ajustado**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)método. Estos datos se utilizarán como fuente de datos para la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de trabajo llamando al[**agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) método de la[**Colección de tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) clase, encapsulada en el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)objeto.
1.  Acceder al[**Tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) objeto de la[**Colección de tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) al pasar el[**Tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)índice.
1.  Utilice cualquiera de los objetos de la tabla dinámica (explicados anteriormente) encapsulados en el[**Tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)objeto para gestionar la tabla dinámica.

{{% alert color="primary" %}}

Al asignar un rango de celdas como fuente de datos, el rango debe configurarse desde la parte superior izquierda hasta la parte inferior derecha. Por ejemplo, "A1:C3" es válido; "C3:A1" no es válido.

{{% /alert %}}

El siguiente ejemplo de código muestra cómo crear una tabla dinámica simple siguiendo los pasos básicos enumerados anteriormente. Al ejecutar el código, se agrega una tabla dinámica a la hoja de trabajo:

**Crear una tabla dinámica basada en un campo correspondiente**

![todo:imagen_alternativa_texto](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
