---
title: Crear Gráficos Dinámicos
description: Aprende cómo crear gráficos dinámicos en Aspose.Cells for .NET. Nuestra guía te mostrará cómo actualizar dinámicamente los datos del gráfico, series y formato en función de tus requisitos, lo que te permitirá presentar visualmente datos cambiantes en tus hojas de cálculo.
keywords: Aspose.Cells for .NET, graficación, gráficos dinámicos, datos, series, formato, hojas de cálculo, actualización.
type: docs
weight: 240
url: /es/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Los gráficos dinámicos (o interactivos) tienen la capacidad de cambiar cuando cambias el alcance de los datos. En otras palabras, los gráficos dinámicos pueden reflejar automáticamente los cambios cuando se cambia la fuente de datos. Para desencadenar el cambio en la fuente de datos, se puede usar la opción de filtrado de las Tablas de Excel o usar un control como ComboBox o lista desplegable.

Este artículo demuestra el uso de las API Aspose.Cells for .NET para crear gráficos dinámicos utilizando ambos enfoques mencionados anteriormente.

{{% /alert %}}

## **Uso de Tablas de Excel**

{{% alert color="primary" %}}

Las tablas de Excel se denominan ListObjects en la perspectiva de Aspose.Cells, por lo tanto, utilizaremos el término "ListObject" en lugar de "Tabla" para mayor claridad. Por favor, lee en detalle cómo [crear ListObjects](/cells/es/net/crear-y-formatear-tabla/) con la API Aspose.Cells for .NET.

{{% /alert %}}

ListObjects proporciona la funcionalidad integrada para ordenar y filtrar los datos mediante la interacción del usuario. Ambas opciones de ordenación y filtrado se proporcionan a través de las listas desplegables que se añaden automáticamente en la fila del encabezado de la [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject). Debido a estas funciones (ordenación y filtrado), la [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) parece ser la candidata perfecta para servir como fuente de datos de un gráfico dinámico, porque cuando se cambia la ordenación o el filtrado, la representación de los datos en el gráfico se variará para reflejar el estado actual de la [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

Para mantener la demostración simple de entender, crearemos la [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) desde cero y avanzaremos paso a paso como se describe a continuación.

1. Crear un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) vacío.
1. Acceder al [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primer [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en el [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Insertar algunos datos en las celdas.
1. Crear [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) basado en los datos insertados.
1. Crear [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basado en el rango de datos de [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Uso de Fórmulas Dinámicas**

En caso de que no desees utilizar la [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) como fuente de datos para el gráfico dinámico, la otra opción es utilizar las funciones de Excel (o fórmulas) para crear un rango dinámico de datos, y un control (como ComboBox) para desencadenar el cambio en los datos. En este escenario, usaremos la función VLOOKUP para obtener los valores apropiados en función de la selección de ComboBox. Cuando se cambia la selección, la función VLOOKUP actualizará el valor de la celda. Si un rango de celdas está utilizando la función VLOOKUP, todo el rango puede ser actualizado mediante la interacción del usuario, por lo tanto, puede utilizarse como fuente para el gráfico dinámico.

Para mantener la demostración simple de entender, crearemos el libro de trabajo desde cero y avanzaremos paso a paso según se describe a continuación.

1. Crear un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) vacío.
1. Acceder al [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primer [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en el [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserte algunos datos en las celdas creando un Rango Nombrado. Estos datos servirán como una serie para el gráfico dinámico.
1. Cree [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) basado en el Rango Nombrado creado en el paso anterior.
1. Inserte más datos en las celdas que servirán como origen para la función VLOOKUP.
1. Inserte la función VLOOKUP (con los parámetros apropiados) en un rango de celdas. Este rango servirá como origen para el gráfico dinámico.
1. Cree [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basado en el rango creado en el paso anterior.
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
