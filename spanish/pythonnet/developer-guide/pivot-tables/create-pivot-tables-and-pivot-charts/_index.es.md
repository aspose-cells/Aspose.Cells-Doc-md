---
title: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 20
url: /es/python-net/create-pivot-tables-and-pivot-charts/
description: Cómo añadir tablas dinámicas y gráficos dinámicos con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca Python de Excel, Agregar Tablas Dinámicas y Gráficos Dinámicos Usando la Biblioteca de Aspose.Cells para Python Excel.
---

{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puede tener cientos de entradas de factura en una lista en una hoja de cálculo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

Aspose.Cells para Python via .NET soporta [tablas dinámicas](/cells/es/python-net/create-pivot-tables-and-pivot-charts/) y [gráficos dinámicos](/cells/es/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Agregar Tablas Dinámicas y Gráficos utilizando la Biblioteca de Aspose.Cells para Python Excel**

Aspose.Cells para Python via .NET provee un conjunto especial de clases utilizadas para crear tablas dinámicas. Estas clases se utilizan para crear y establecer objetos PivotTable, que actúan como los elementos básicos de construcción de un objeto de tabla dinámica:

- PivotField, un campo en un informe de tabla dinámica.
- PivotFields, una colección de todos los objetos PivotField en una tabla dinámica.
- PivotTable, un informe de tabla dinámica en una hoja de cálculo.
- PivotTables, una colección de todos los objetos PivotTable en la hoja de cálculo.

### **Prepararse para utilizar Aspose.Cells para Python via .NET**
1. Instalar Aspose.Cells para Python via .NET desde [pypi](https://pypi.org/project/aspose-cells-python/), utilizando el comando: $ pip install aspose-cells-python.
1. También puedes seguir las instrucciones paso a paso sobre cómo instalar “Aspose.Cells para Python via .NET” en tu entorno de desarrollo.


### **Cómo Añadir una Tabla Dinámica Utilizando la Biblioteca de Aspose.Cells para Python Excel**

Para crear una tabla dinámica utilizando Aspose.Cells para Python via .NET:

1. Añadir algunos datos a las celdas de una hoja de cálculo utilizando el método put_value de un objeto Celda. También puedes utilizar un archivo de plantilla ya lleno de datos. Los datos se utilizarán como fuente de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método add de la colección PivotTables (encapsulada en el objeto Worksheet).
1. Accede al nuevo objeto PivotTable desde la colección PivotTables pasando su índice. # Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para gestionar la tabla.

A continuación se muestran ejemplos de código.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Cómo agregar un gráfico dinámico usando Aspsoe.Cells para la biblioteca de Excel de Python**

Para crear un PivotChart utilizando Aspose.Cells para Python via .NET:

1. Agregue un gráfico.
1. Establezca el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
