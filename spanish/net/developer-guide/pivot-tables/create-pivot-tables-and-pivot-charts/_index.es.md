---
title: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 20
url: /es/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puede tener cientos de entradas de facturas en una lista en una hoja de trabajo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando los botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

 Aspose.Cells apoya[tablas dinamicas](/cells/es/net/create-pivot-tables-and-pivot-charts/) y[gráficos dinámicos](/cells/es/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Adición de tablas y gráficos dinámicos**

Aspose.Cells proporciona un conjunto especial de clases que se utilizan para crear tablas dinámicas. Estas clases se utilizan para crear y establecer objetos de tabla dinámica, que actúan como bloques de construcción básicos de un objeto de tabla dinámica:

- PivotField, un campo en un informe de tabla dinámica.
- PivotFields, una colección de todos los objetos PivotField en una tabla dinámica.
- Tabla dinámica, un informe de tabla dinámica en una hoja de cálculo.
- Tablas dinámicas, una colección de todos los objetos de tabla dinámica en la hoja de cálculo.

### **Preparándose para usar Aspose.Cells**

1. Descargar e instalar Aspose.Cells:
   1. [Descargar Aspose.Cells](https://downloads.aspose.com/cells/net).
 1. Instálelo en su computadora de desarrollo.
 Todos[Aspose](http://www.aspose.com/) Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos. Para trabajar con el componente en toda su capacidad, necesita tener una licencia válida.
1. Crear un proyecto:
 1. Inicie Visual Studio.Net.
 1. Cree una nueva aplicación de consola.
1. Añadir referencias:
 Agregue una referencia al componente Aspose.Cells en su proyecto, por ejemplo ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Agregar una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de cálculo mediante el método PutValue/setValue de un objeto Cell. También utiliza un archivo de plantilla ya lleno de datos. Los datos se utilizarán como fuente de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de trabajo llamando al método add de la colección PivotTables (encapsulado en el objeto Worksheet).
1. Acceda al nuevo objeto PivotTable de la colección PivotTables pasando su índice. # Use cualquiera de los objetos de la tabla dinámica encapsulados en el objeto PivotTable para administrar la tabla.

Los ejemplos de código se dan a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Agregar un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregar un gráfico.
1. Configure el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establecer otros atributos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

