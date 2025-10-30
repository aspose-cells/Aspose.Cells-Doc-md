---
title: Crear tablas dinámicas y gráficos dinámicos con Golang vía C++
linktitle: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 20
url: /es/go-cpp/create-pivot-tables-and-pivot-charts/
description: Aprende cómo crear tablas dinámicas y gráficos dinámicos en archivos Excel usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puedes tener cientos de entradas de facturas en una lista en una hoja de cálculo. Una tabla dinámica puede sumar las facturas por cliente, producto o fecha. Con Microsoft Excel, es posible reorganizar rápidamente la información en la tabla dinámica arrastrando botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

Aspose.Cells admite [tablas dinámicas](/cells/es/cpp/create-pivot-tables-and-pivot-charts/) y [gráficos dinámicos](/cells/es/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Añadiendo tablas dinámicas y gráficos**

Aspose.Cells proporciona un conjunto especial de clases utilizadas para crear tablas dinámicas. Estas clases se utilizan para crear y configurar objetos PivotTable, que actúan como bloques de construcción básicos de un objeto PivotTable:

- **CampoDinámico**, un campo en un informe de tabla dinámica.
- **CamposDinámicos**, una colección de todos los objetos CampoDinámico en una tabla dinámica.
- **TablaDinámica**, un informe de TablaDinámica en una hoja de cálculo.
- **TablasDinámicas**, una colección de todos los objetos TablaDinámica en la hoja de cálculo.

### **Preparación para usar Aspose.Cells**

1. Descargue e instale Aspose.Cells:
   1. [Descargar Aspose.Cells](https://downloads.aspose.com/cells/go-cpp/).
   1. Instálelo en su equipo de desarrollo.
      Todos los componentes de [Aspose](http://www.aspose.com/), al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos. Para trabajar con el componente en su capacidad total, necesitas tener una licencia válida.
1. Cree un proyecto:
   1. Inicia tu entorno de desarrollo C++ (por ejemplo, Visual Studio).
   1. Cree una nueva aplicación de consola.
1. Agregue referencias:
   Agrega una referencia al componente Aspose.Cells en tu proyecto, por ejemplo, `...\Archivos de programa\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Añadiendo una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agrega algunos datos a las celdas de una hoja de cálculo usando el método `PutValue` de un objeto `Cell`. También puedes usar un archivo de plantilla ya llenado con datos. Los datos se usarán como fuente de datos para la tabla dinámica.
1. Agrega una tabla dinámica a la hoja llamando al método `Add` de la colección `PivotTables` (encapsulada en el objeto `Worksheet`).
1. Accede al nuevo objeto `PivotTable` desde la colección `PivotTables` pasando su índice. Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto `PivotTable` para gestionar la tabla.

A continuación se muestran ejemplos de código.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **Añadiendo un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregue un gráfico.
1. Establece el `PivotSource` del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
