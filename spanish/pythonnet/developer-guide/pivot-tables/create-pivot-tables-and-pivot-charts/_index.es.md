---
title: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 20
url: /es/python-net/create-pivot-tables-and-pivot-charts/
description: Cómo agregar tablas dinámicas y gráficos dinámicos con Aspose.Cells for Python via .NET.
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, es posible que tenga cientos de entradas de facturas en una lista de una hoja de trabajo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando los botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico hace que sea aún más fácil comprender los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

 Aspose.Cells for Python via .NET soportes[tablas dinamicas](/cells/es/python-net/create-pivot-tables-and-pivot-charts/) y[gráficos dinámicos](/cells/es/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **Agregar tablas dinámicas y gráficos**

Aspose.Cells for Python via .NET proporciona un conjunto especial de clases que se utilizan para crear tablas dinámicas. Estas clases se utilizan para crear y configurar objetos de tabla dinámica, que actúan como los componentes básicos de un objeto de tabla dinámica:

- PivotField, un campo en un informe de tabla dinámica.
- PivotFields, una colección de todos los objetos PivotField en una tabla dinámica.
- Tabla dinámica, un informe de tabla dinámica en una hoja de trabajo.
- Tablas dinámicas, una colección de todos los objetos de la tabla dinámica en la hoja de trabajo.

###  **Preparándose para usar Aspose.Cells for Python via .NET**
1.  Instalar Aspose.Cells for Python via .NET desde[pipi](https://pypi.org/project/aspose-cells-python/)use el comando como: $ pip install aspose-cells-python.
1. También puede seguir las instrucciones paso a paso sobre cómo instalar “Aspose.Cells for Python via .NET” en su entorno de desarrollador.


###  **Agregar una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells for Python via .NET:

1. Agregue algunos datos a las celdas de una hoja de cálculo utilizando el método put_value de un objeto Cell. También utiliza un archivo de plantilla ya lleno de datos. Los datos se utilizarán como fuente de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de trabajo llamando al método add de la colección PivotTables (encapsulado en el objeto Hoja de trabajo).
1. Acceda al nuevo objeto de tabla dinámica de la colección de tablas dinámicas pasando su índice. # Utilice cualquiera de los objetos de la tabla dinámica encapsulados en el objeto PivotTable para administrar la tabla.

A continuación se proporcionan ejemplos de código.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **Agregar un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells for Python via .NET:

1. Añade un gráfico.
1. Establezca el PivotSource del gráfico para que haga referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establece otros atributos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

