---
title: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 20
url: /es/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Cómo agregar tablas dinámicas y gráficos dinámicos con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, biblioteca de Node.js para Excel, agregar tablas dinámicas y gráficos dinámicos usando la biblioteca Excel Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puede tener cientos de entradas de factura en una lista en una hoja de cálculo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

Aspose.Cells for Node.js via C++ soporta [tablas dinámicas](/cells/es/nodejs-cpp/create-pivot-tables-and-pivot-charts/) y [gráficos dinámicos](/cells/es/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Agregar tablas dinámicas y gráficos usando Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ proporciona un conjunto especial de clases utilizadas para crear tablas dinámicas. Estas clases sirven para crear y configurar objetos PivotTable, que actúan como los bloques básicos de un objeto PivotTable:

- PivotField, un campo en un informe de tabla dinámica.
- PivotFields, una colección de todos los objetos PivotField en una tabla dinámica.
- PivotTable, un informe de tabla dinámica en una hoja de cálculo.
- PivotTables, una colección de todos los objetos PivotTable en la hoja de cálculo.

### **Prepararse para usar Aspose.Cells for Node.js via C++**
1. Instala Aspose.Cells for Node.js via C++ desde NPM, usando el comando: $ npm install aspose.cells.node.
1. También puedes seguir las instrucciones paso a paso sobre cómo instalar “Aspose.Cells for Node.js via C++” en tu entorno de desarrollo.


### **Cómo agregar una tabla dinámica usando Aspose.Cells for Node.js via C++**

Para crear una tabla dinámica usando Aspose.Cells for Node.js via C++:

1. Añadir algunos datos a las celdas de una hoja de cálculo utilizando el método put_value de un objeto Celda. También puedes utilizar un archivo de plantilla ya lleno de datos. Los datos se utilizarán como fuente de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método add de la colección PivotTables (encapsulada en el objeto Worksheet).
1. Accede al nuevo objeto PivotTable desde la colección PivotTables pasando su índice. # Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para gestionar la tabla.

A continuación se muestran ejemplos de código.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Cómo agregar un gráfico dinámico usando la biblioteca Aspose.Cells for Node.js via C++**

Para crear un gráfico dinámico usando Aspose.Cells for Node.js via C++:

1. Agregue un gráfico.
1. Establezca el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
