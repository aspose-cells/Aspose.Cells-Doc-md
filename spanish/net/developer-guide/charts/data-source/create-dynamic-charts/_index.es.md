---
title: Crear gráficos dinámicos
description: Aprenda a crear gráficos dinámicos en Aspose.Cells for .NET. Nuestra guía le mostrará cómo actualizar dinámicamente los datos, las series y el formato de los gráficos según sus requisitos, lo que le permitirá presentar datos cambiantes visualmente en sus hojas de trabajo.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /es/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Los gráficos dinámicos (o interactivos) tienen la capacidad de cambiar cuando cambia el alcance de los datos. En otras palabras, los gráficos dinámicos pueden reflejar automáticamente los cambios cuando se cambia la fuente de datos. Para activar el cambio en la fuente de datos, se puede usar la opción de filtrado de Tablas de Excel o usar un control como ComboBox o Lista desplegable.

Este artículo demuestra el uso de las API Aspose.Cells for .NET para crear gráficos dinámicos utilizando los dos enfoques mencionados anteriormente.

{{% /alert %}}

##  **Usando tablas de Excel**

{{% alert color="primary" %}}

 Las tablas de Excel se denominan ListObjects en la perspectiva Aspose.Cells, por lo tanto, usaremos el término "ListObject" en lugar de "Tabla" para mayor claridad. Por favor lea detalladamente cómo[crear lista de objetos](/cells/es/net/create-and-format-table/)con Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects proporciona la funcionalidad incorporada para ordenar y filtrar los datos tras la interacción del usuario. Ambas opciones de clasificación y filtrado se proporcionan a través de las listas desplegables que se agregan automáticamente a la fila del encabezado del[**Lista de objetos**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Debido a estas características (clasificación y filtrado), el[**Lista de objetos**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) parece ser el candidato perfecto para servir como fuente de datos para un gráfico dinámico porque cuando se cambia la clasificación o el filtrado, la representación de los datos en el gráfico cambiará para reflejar el estado actual del[**Lista de objetos**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Para que la demostración sea sencilla de entender, crearemos el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)desde cero y avance paso a paso como se describe a continuación.

1.  crear un vacio[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Acceder al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primero[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserte algunos datos en las celdas.
1.  Crear[**Lista de objetos**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)basado en los datos insertados.
1.  Crear[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basado en el rango de datos de[**Lista de objetos**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **Usar fórmulas dinámicas**

En caso de que no desee utilizar el[**Lista de objetos**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Como fuente de datos para el gráfico dinámico, la otra opción es usar funciones (o fórmulas) de Excel para crear un rango dinámico de datos y un control (como ComboBox) para activar el cambio en los datos. En este escenario, usaremos la función BUSCARV para recuperar los valores apropiados según la selección de ComboBox. Cuando se cambia la selección, la función BUSCARV actualizará el valor de la celda. Si un rango de celdas utiliza la función BUSCARV, todo el rango se puede actualizar tras la interacción del usuario, por lo tanto, se puede utilizar como fuente para el gráfico dinámico.

Para que la demostración sea fácil de entender, crearemos el Libro de trabajo desde cero y avanzaremos paso a paso como se describe a continuación.

1.  crear un vacio[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Acceder al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) del primero[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Inserte algunos datos en las celdas creando un rango con nombre. Estos datos servirán como una serie para el gráfico dinámico.
1.  Crear[**Caja combo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)basado en el rango con nombre creado en el paso anterior.
1. Inserte algunos datos más en las celdas que servirán como fuente para la función BUSCARV.
1. Inserte la función BUSCARV (con los parámetros apropiados) en un rango de celdas. Este rango servirá como fuente para el gráfico dinámico.
1.  Crear[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)basado en el rango creado en el paso anterior.
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
