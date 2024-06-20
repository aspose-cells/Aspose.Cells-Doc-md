---
title: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 20
url: /es/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puede tener cientos de entradas de factura en una lista en una hoja de cálculo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

Aspose.Cells admite [tablas dinámicas](/cells/es/net/create-pivot-tables-and-pivot-charts/) y [gráficos dinámicos](/cells/es/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Añadiendo tablas dinámicas y gráficos**

Aspose.Cells proporciona un conjunto especial de clases utilizadas para crear tablas dinámicas. Estas clases se utilizan para crear y configurar objetos PivotTable, que actúan como bloques de construcción básicos de un objeto PivotTable:

- PivotField, un campo en un informe de tabla dinámica.
- PivotFields, una colección de todos los objetos PivotField en una tabla dinámica.
- PivotTable, un informe de tabla dinámica en una hoja de cálculo.
- PivotTables, una colección de todos los objetos PivotTable en la hoja de cálculo.

### **Preparación para usar Aspose.Cells**

1. Descargue e instale Aspose.Cells:
   1. [Descargar Aspose.Cells](https://downloads.aspose.com/cells/net).
   1. Instálelo en su equipo de desarrollo.
      Todos los componentes de [Aspose](http://www.aspose.com/), al ser instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos. Para trabajar con el componente en su capacidad total, necesitas tener una licencia válida.
1. Cree un proyecto:
   1. Inicia Visual Studio.Net.
   1. Cree una nueva aplicación de consola.
1. Agregue referencias:
   Agrega una referencia al componente Aspose.Cells en tu proyecto, por ejemplo ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Añadiendo una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de cálculo utilizando el método PutValue/setValue de un objeto Cell. También puede utilizar un archivo de plantilla ya lleno con datos. Los datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método add de la colección PivotTables (encapsulada en el objeto Worksheet).
1. Accede al nuevo objeto PivotTable desde la colección PivotTables pasando su índice. # Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para gestionar la tabla.

A continuación se muestran ejemplos de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Añadiendo un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregue un gráfico.
1. Establezca el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

