---
title: Crear gráficos dinámicos
type: docs
weight: 200
url: /es/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

Los gráficos dinámicos (o interactivos) tienen la capacidad de cambiar cuando cambia el alcance de los datos. En otras palabras, los gráficos dinámicos pueden reflejar cambios automáticamente cuando se cambia la fuente de datos. Para activar el cambio en la fuente de datos, se puede usar la opción de filtrado de tablas de Excel o usar un control como ComboBox o lista desplegable.

Este artículo demuestra el uso de las API Aspose.Cells for Java para crear gráficos dinámicos utilizando los dos enfoques mencionados anteriormente.

{{% /alert %}}

## **Uso de tablas de Excel**

{{% alert color="primary" %}}

 Las tablas de Excel se denominan ListObjects en la perspectiva Aspose.Cells, por lo que utilizaremos el término "ListObject" en lugar de "Table" para mayor claridad. Por favor, lea en detalle sobre cómo[crear ListObjects](/cells/es/java/creating-a-list-object/) con Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects proporciona la funcionalidad integrada para ordenar y filtrar los datos sobre la interacción del usuario. Las opciones de clasificación y filtrado se proporcionan a través de las listas desplegables que se agregan automáticamente a la fila de encabezado de ListObject. Debido a estas características (ordenación y filtrado), ListObject parece ser el candidato perfecto para servir como fuente de datos para un gráfico dinámico porque cuando se cambia la clasificación o el filtrado, la representación de los datos en el gráfico cambiará para reflejar la actual. estado del ListObject.

Para que la demostración sea fácil de entender, crearemos el Libro de trabajo desde cero y avanzaremos paso a paso como se describe a continuación.

1. Cree un libro de trabajo vacío.
1. Acceda al Cells de la primera Hoja de trabajo en el Libro de trabajo.
1. Inserte algunos datos en las celdas.
1. Crear ListObject basado en los datos insertados.
1. Cree un gráfico basado en el rango de datos de ListObject.
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Uso de fórmulas dinámicas**

En caso de que no desee utilizar ListObjects como fuente de datos para el gráfico dinámico, la otra opción es utilizar funciones (o fórmulas) de Excel para crear un rango dinámico de datos y un control (como ComboBox) para activar el cambio. en datos En este escenario, usaremos la función BUSCARV para obtener los valores apropiados según la selección de ComboBox. Cuando se cambia la selección, la función BUSCARV actualizará el valor de la celda. Si un rango de celdas está usando la función BUSCARV, el rango completo se puede actualizar con la interacción del usuario, por lo tanto, se puede usar como fuente para el gráfico dinámico.

Para que la demostración sea fácil de entender, crearemos el Libro de trabajo desde cero y avanzaremos paso a paso como se describe a continuación.

1. Cree un libro de trabajo vacío.
1. Acceda al Cells de la primera Hoja de trabajo en el Libro de trabajo.
1. Inserte algunos datos en las celdas creando un rango con nombre. Estos datos servirán como serie al gráfico dinámico.
1. Cree ComboBox basado en el rango con nombre creado en el paso anterior.
1. Inserte algunos datos más en las celdas que servirán como fuente para la función BUSCARV.
1. Inserte la función BUSCARV (con los parámetros apropiados) en un rango de celdas. Este rango servirá como fuente para el gráfico dinámico.
1. Cree un gráfico basado en el rango creado en el paso anterior.
1. Guarde el resultado en el disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
