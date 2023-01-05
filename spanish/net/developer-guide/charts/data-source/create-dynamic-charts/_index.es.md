---
title: Crear gráficos dinámicos
type: docs
weight: 240
url: /es/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Los gráficos dinámicos (o interactivos) tienen la capacidad de cambiar cuando cambia el alcance de los datos. En otras palabras, los gráficos dinámicos pueden reflejar cambios automáticamente cuando se cambia la fuente de datos. Para activar el cambio en la fuente de datos, se puede usar la opción de filtrado de tablas de Excel o usar un control como ComboBox o lista desplegable.

Este artículo demuestra el uso de las API Aspose.Cells for .NET para crear gráficos dinámicos utilizando los dos enfoques mencionados anteriormente.

{{% /alert %}}

## **Uso de tablas de Excel**

{{% alert color="primary" %}}

 Las tablas de Excel se conocen como ListObjects en la perspectiva Aspose.Cells, por lo tanto, usaremos el término "ListObject" en lugar de "Table" para mayor claridad. Por favor, lea en detalle sobre cómo[crear ListObjects](/cells/es/net/create-and-format-table/) con Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects proporciona la funcionalidad integrada para ordenar y filtrar los datos sobre la interacción del usuario. Las opciones de clasificación y filtrado se proporcionan a través de las listas desplegables que se agregan automáticamente a la fila del encabezado del[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Debido a estas características (clasificación y filtrado), el[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)parece ser el candidato perfecto para servir como fuente de datos para un gráfico dinámico porque cuando se cambia la clasificación o el filtrado, la representación de los datos en el gráfico cambiará para reflejar el estado actual del[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Para que la demostración sea fácil de entender, crearemos el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)desde cero y avance paso a paso como se describe a continuación.

1.  Crear un vacío[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Acceder al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primero[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserte algunos datos en las celdas.
1.  Crear[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)en base a los datos insertados.
1.  Crear[**Gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basado en el rango de datos de[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Uso de fórmulas dinámicas**

 En caso de que no desee utilizar el[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)como fuente de datos para el gráfico dinámico, la otra opción es usar funciones de Excel (o fórmulas) para crear un rango dinámico de datos y un control (como ComboBox) para desencadenar el cambio en los datos. En este escenario, usaremos la función BUSCARV para obtener los valores apropiados según la selección de ComboBox. Cuando se cambia la selección, la función BUSCARV actualizará el valor de la celda. Si un rango de celdas usa la función BUSCARV, todo el rango se puede actualizar con la interacción del usuario, por lo tanto, se puede usar como fuente para el gráfico dinámico.

Para que la demostración sea fácil de entender, crearemos el Libro de trabajo desde cero y avanzaremos paso a paso como se describe a continuación.

1.  Crear un vacío[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Acceder al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primero[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserte algunos datos en las celdas creando un rango con nombre. Estos datos servirán como una serie para el gráfico dinámico.
1.  Crear[**Caja combo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)basado en el rango con nombre creado en el paso anterior.
1. Inserte algunos datos más en las celdas que servirán como fuente para la función BUSCARV.
1. Inserte la función BUSCARV (con los parámetros apropiados) en un rango de celdas. Este rango servirá como fuente para el gráfico dinámico.
1.  Crear[**Gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)basado en el rango creado en el paso anterior.
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
