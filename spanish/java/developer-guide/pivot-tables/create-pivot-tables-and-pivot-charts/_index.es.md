---
title: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 10
url: /es/java/create-pivot-tables-and-pivot-charts/
description: Crear tablas dinámicas y gráficos dinámicos con la API Aspose.Cells for Java.
keywords: excel crear tabla dinámica java, excel crear gráfico dinámico java, excel crear tabla dinámica y gráfico dinámico java, crear tabla dinámica excel java, crear gráfico dinámico excel java, crear tabla dinámica y gráfico dinámico excel java, java crear tabla dinámica y gráfico dinámico excel, cómo crear tabla dinámica y gráfico dinámico excel java
---

{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puede tener cientos de entradas de factura en una lista en una hoja de cálculo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

Aspose.Cells soporta [tablas dinámicas](/cells/es/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) y [gráficos dinámicos](/cells/es/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Añadiendo tablas dinámicas y gráficos**

Aspose.Cells proporciona un conjunto especial de clases utilizadas para crear tablas dinámicas. Estas clases se utilizan para crear y configurar objetos PivotTable, que actúan como bloques de construcción básicos de un objeto PivotTable:

- PivotField, un campo en un informe de tabla dinámica.
- PivotFields, una colección de todos los objetos PivotField en una tabla dinámica.
- PivotTable, un informe de tabla dinámica en una hoja de cálculo.
- PivotTables, una colección de todos los objetos PivotTable en la hoja de cálculo.

### **Preparación para usar Aspose.Cells**

1. Descargar e instalar Aspose.Cells.Zip:
   1. [Descargar Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Descomprímelo en tu computadora de desarrollo.
      Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. Crear un proyecto
   1. Puede crear un proyecto utilizando algún editor de Java, por ejemplo, Eclipse, o crear un programa simple usando el Bloc de notas.
1. Agregar ruta de clase:
   Para establecer una ruta de clase utilizando Eclipse:
   1. Extrae Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
   1. Configura la ruta de clase del proyecto en Eclipse:
   1. Seleccione su proyecto en Eclipse y luego haga clic en el menú Proyecto-Propiedades.
   1. Selecciona "Ruta de compilación de Java" en el lado izquierdo de la ventana emergente, luego selecciona la pestaña "Bibliotecas", haz clic en "Agregar archivos JAR" o "Agregar archivos JAR externos" para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a las rutas de compilación.
   1. Escribe una aplicación para invocar las API de los componentes de Aspose.
      O también puede configurarlo en tiempo de ejecución en el símbolo del sistema en Windows.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Crear una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de cálculo utilizando el método PutValue/setValue de un objeto Cell. También puede utilizar un archivo de plantilla ya lleno con datos. Los datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método add de la colección PivotTables (encapsulada en el objeto Worksheet).
1. Acceda al nuevo objeto PivotTable de la colección PivotTables pasando su índice.
1. Utilice cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para administrar la tabla.

A continuación se muestra un ejemplo de código. La ejecución del código genera un nuevo archivo: pivotTable_test.xls.

**Datos de entrada** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**La tabla dinámica de salida**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Crear un gráfico dinámico basado en la tabla dinámica**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregue un gráfico.
1. Establezca el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

A continuación se muestra el código utilizado por el componente para realizar la tarea. Al ejecutar el código se genera un nuevo archivo: pivotChart_test.xls.

**La hoja del gráfico dinámico**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Este artículo muestra cómo crear tablas dinámicas y gráficos dinámicos utilizando Aspose.Cells. Con suerte, le ayudará a usar estas características en sus propios escenarios.

Aspose.Cells se ha beneficiado de años de investigación, diseño y ajustes cuidadosos.

Agradecemos sus consultas, comentarios y sugerencias en el [Foro de Aspose.Cells](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}

## Artículos relacionados

- [Orden personalizado en la tabla dinámica](/cells/es/java/custom-sorting-in-pivot-table/)
- [Dar formato a la tabla dinámica](/cells/es/java/formatting-pivot-table/)
- [Actualizar y Calcular Tabla Dinámica con Elementos Calculados](/cells/es/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Deshabilitar las cintas de la tabla dinámica](/cells/es/java/disable-pivot-table-ribbons/)

{{< app/cells/assistant language="java" >}}
