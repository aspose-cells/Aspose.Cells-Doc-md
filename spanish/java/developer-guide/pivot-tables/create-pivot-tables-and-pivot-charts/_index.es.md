---
title: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 10
url: /es/java/create-pivot-tables-and-pivot-charts/
description: Cree tablas dinámicas y gráficos dinámicos con Aspose.Cells for Java API.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puede tener cientos de entradas de facturas en una lista en una hoja de trabajo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando los botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

 Aspose.Cells apoya[tablas dinamicas](/cells/es/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) y[gráficos dinámicos](/cells/es/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Adición de tablas y gráficos dinámicos**

Aspose.Cells proporciona un conjunto especial de clases que se utilizan para crear tablas dinámicas. Estas clases se utilizan para crear y establecer objetos de tabla dinámica, que actúan como bloques de construcción básicos de un objeto de tabla dinámica:

- PivotField, un campo en un informe de tabla dinámica.
- PivotFields, una colección de todos los objetos PivotField en una tabla dinámica.
- Tabla dinámica, un informe de tabla dinámica en una hoja de cálculo.
- Tablas dinámicas, una colección de todos los objetos de tabla dinámica en la hoja de cálculo.

### **Preparándose para usar Aspose.Cells**

1. Descargue e instale Aspose.Cells.Zip:
   1. [Descargar Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Descomprímalo en su computadora de desarrollo.
 Todos[Aspose](http://www.aspose.com/) Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. crear un proyecto
 1. Puede crear un proyecto usando algún editor Java, por ejemplo, Eclipse, o crear un programa simple usando un Bloc de notas.
1. Agregar ruta de clase:
 Para establecer una ruta de clase usando Eclipse:
1. Extraiga Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Establezca el classpath del proyecto en Eclipse:
1. Seleccione su proyecto en Eclipse y luego haga clic en los menús Proyecto-Propiedades.
 1. Seleccione "Java Build Path" en el lado izquierdo de la ventana emergente, luego seleccione la pestaña "Bibliotecas", haga clic en "Agregar JAR" o "Agregar JAR externos" para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos en caminos de construcción.
 1. Escriba una aplicación para invocar las API de los componentes de Aspose.
 O puede configurarlo en tiempo de ejecución en el indicador de dos en Windows.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Creación de una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de cálculo mediante el método PutValue/setValue de un objeto Cell. También utiliza un archivo de plantilla ya lleno de datos. Los datos se utilizarán como fuente de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de trabajo llamando al método add de la colección PivotTables (encapsulado en el objeto Worksheet).
1. Acceda al nuevo objeto PivotTable de la colección PivotTables pasando su índice.
1. Utilice cualquiera de los objetos de la tabla dinámica encapsulados en el objeto PivotTable para administrar la tabla.

A continuación se proporciona un ejemplo de código. La ejecución del código genera un nuevo archivo: pivotTable_test.xls.

**Datos de entrada** 

![todo:imagen_alternativa_texto](create-pivot-tables-and-pivot-charts_1.png)

**La tabla dinámica de salida**

![todo:imagen_alternativa_texto](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Creación de un gráfico dinámico basado en la tabla dinámica**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregar un gráfico.
1. Configure el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establecer otros atributos.

A continuación se muestra el código utilizado por el componente para realizar la tarea. La ejecución del código genera un nuevo archivo: pivotChart_test.xls.

**La hoja del gráfico pivote**

![todo:imagen_alternativa_texto](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Este artículo muestra cómo crear tablas dinámicas y gráficos dinámicos usando Aspose.Cells. Con suerte, lo ayudará a usar estas funciones en sus propios escenarios.

Aspose.Cells se ha beneficiado de años de investigación, diseño y ajuste cuidadoso.

 Agradecemos sus consultas, comentarios y sugerencias en[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}

## Artículos relacionados

- [Clasificación personalizada en la tabla dinámica](/cells/es/java/custom-sorting-in-pivot-table/)
- [Formato de tabla dinámica](/cells/es/java/formatting-pivot-table/)
- [Actualizar y calcular tabla dinámica con elementos calculados](/cells/es/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Deshabilitar cintas de tabla dinámica](/cells/es/java/disable-pivot-table-ribbons/)

