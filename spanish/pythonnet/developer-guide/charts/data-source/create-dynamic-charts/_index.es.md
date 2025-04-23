---
title: Crear Gráficos Dinámicos
description: Aprende cómo crear gráficos dinámicos en Aspose.Cells para Python via .NET. Nuestra guía te mostrará cómo actualizar de forma dinámica los datos del gráfico, series y formato según tus requisitos, permitiéndote presentar datos cambiantes visualmente en tus hojas de cálculo.
keywords: Aspose.Cells para Python via .NET, gráficos, gráficos dinámicos, datos, series, formato, hojas de cálculo, actualización.
type: docs
weight: 240
url: /es/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Los gráficos dinámicos (o interactivos) tienen la capacidad de cambiar cuando cambias el alcance de los datos. En otras palabras, los gráficos dinámicos pueden reflejar automáticamente los cambios cuando se cambia la fuente de datos. Para desencadenar el cambio en la fuente de datos, se puede usar la opción de filtrado de las Tablas de Excel o usar un control como ComboBox o lista desplegable.

Este artículo demuestra el uso de las APIs de Aspose.Cells para Python via .NET para crear gráficos dinámicos usando ambos enfoques mencionados anteriormente.

{{% /alert %}}

## **Uso de Tablas de Excel**

{{% alert color="primary" %}}

Las tablas de Excel se denominan ListObjects en la perspectiva de Aspose.Cells, por lo tanto, usaremos el término "ListObject" en lugar de "Tabla" para mayor claridad. Lea en detalle sobre cómo [crear ListObjects](/cells/es/python-net/create-and-format-table/) con la API Aspose.Cells para Python via .NET.

{{% /alert %}}

ListObjects proporciona la funcionalidad integrada para ordenar y filtrar los datos mediante la interacción del usuario. Ambas opciones de ordenamiento y filtrado se ofrecen a través de las listas desplegables que se agregan automáticamente a la fila de encabezado del. Debido a estas características (ordenamiento y filtrado), el [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) parece ser el candidato perfecto para servir como fuente de datos para un gráfico dinámico porque cuando se cambia el ordenamiento o filtrado, la representación de los datos en el gráfico cambiará para reflejar el estado actual del.

Para mantener la demostración simple de entender, crearemos la [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) desde cero y avanzaremos paso a paso como se describe a continuación.

1. Crear un [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) vacío.
1. Acceder al [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) del primer [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) en el [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Insertar algunos datos en las celdas.
1. Crear [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) basado en los datos insertados.
1. Crear [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basado en el rango de datos de [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject).
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **Uso de Fórmulas Dinámicas**

En caso de que no desees utilizar la [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) como fuente de datos para el gráfico dinámico, la otra opción es utilizar las funciones de Excel (o fórmulas) para crear un rango dinámico de datos, y un control (como ComboBox) para desencadenar el cambio en los datos. En este escenario, usaremos la función VLOOKUP para obtener los valores apropiados en función de la selección de ComboBox. Cuando se cambia la selección, la función VLOOKUP actualizará el valor de la celda. Si un rango de celdas está utilizando la función VLOOKUP, todo el rango puede ser actualizado mediante la interacción del usuario, por lo tanto, puede utilizarse como fuente para el gráfico dinámico.

Para mantener la demostración simple de entender, crearemos el libro de trabajo desde cero y avanzaremos paso a paso según se describe a continuación.

1. Crear un [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) vacío.
1. Acceder al [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) del primer [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) en el [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Inserte algunos datos en las celdas creando un Rango Nombrado. Estos datos servirán como una serie para el gráfico dinámico.
1. Cree [**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) basado en el Rango Nombrado creado en el paso anterior.
1. Inserte más datos en las celdas que servirán como origen para la función VLOOKUP.
1. Inserte la función VLOOKUP (con los parámetros apropiados) en un rango de celdas. Este rango servirá como origen para el gráfico dinámico.
1. Cree [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basado en el rango creado en el paso anterior.
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
