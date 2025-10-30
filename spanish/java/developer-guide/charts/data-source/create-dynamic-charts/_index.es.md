---
title: Crear Gráficos Dinámicos
type: docs
weight: 200
url: /es/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

Los gráficos dinámicos (o interactivos) tienen la capacidad de cambiar cuando cambia el alcance de los datos. En otras palabras, los gráficos dinámicos pueden reflejar automáticamente los cambios cuando se modifica la fuente de datos. Para desencadenar el cambio en la fuente de datos, se puede utilizar la opción de filtrado de las Tablas de Excel o utilizar un control como ComboBox o lista desplegable.

Este artículo demuestra el uso de Aspose.Cells for Java APIs para crear gráficos dinámicos utilizando ambos enfoques mencionados anteriormente.

{{% /alert %}}

## **Uso de Tablas de Excel**

{{% alert color="primary" %}}

Las tablas de Excel se denominan ListObjects desde la perspectiva de Aspose.Cells, por lo tanto usaremos el término "ListObject" en lugar de "Tabla" para mayor claridad. Por favor, lea con detalle cómo [crear ListObjects](/cells/es/java/creating-a-list-object/) con la API Aspose.Cells for Java.

{{% /alert %}}

ListObjects proporciona la funcionalidad integrada para ordenar y filtrar los datos mediante la interacción del usuario. Ambas opciones de ordenar y filtrar se proporcionan a través de listas desplegables que se añaden automáticamente a la fila de encabezado del ListObject. Debido a estas características (ordenar y filtrar), el ListObject parece ser el candidato perfecto para servir como fuente de datos para un gráfico dinámico, porque cuando se cambia la ordenación o el filtrado, la representación de los datos en el gráfico se modificará para reflejar el estado actual del ListObject.

Para mantener la demostración simple de entender, crearemos el libro de trabajo desde cero y avanzaremos paso a paso según se describe a continuación.

1. Crear un Libro de trabajo vacío.
1. Acceder a las celdas de la primera Hoja de cálculo en el Libro de trabajo.
1. Insertar algunos datos en las celdas.
1. Crear ListObject basado en los datos insertados.
1. Crear Gráfico basado en el rango de datos de ListObject.
1. Guardar el resultado en el disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Uso de Fórmulas Dinámicas**

En caso de que no desee utilizar ListObjects como fuente de datos para el gráfico dinámico, la otra opción es utilizar funciones de Excel (o fórmulas) para crear un rango dinámico de datos y un control (como ComboBox) para desencadenar el cambio en los datos. En este escenario, utilizaremos la función VLOOKUP para obtener los valores apropiados en función de la selección de ComboBox. Cuando se cambia la selección, la función VLOOKUP actualizará el valor de la celda. Si un rango de celdas está utilizando la función VLOOKUP, todo el rango puede actualizarse mediante la interacción del usuario, por lo tanto, puede utilizarse como fuente para el gráfico dinámico.

Para mantener la demostración simple de entender, crearemos el libro de trabajo desde cero y avanzaremos paso a paso según se describe a continuación.

1. Crear un Libro de trabajo vacío.
1. Acceder a las celdas de la primera Hoja de cálculo en el Libro de trabajo.
1. Insertar algunos datos en las celdas creando un Rango Nombrado. Estos datos servirán como series para el gráfico dinámico.
1. Crear un ComboBox basado en el Rango con nombre creado en el paso anterior.
1. Insertar más datos en las celdas que servirán como fuente para la función BUSCARV.
1. Insertar la función BUSCARV (con parámetros apropiados) en un rango de celdas. Este rango servirá como fuente para el gráfico dinámico.
1. Crear un gráfico basado en el rango creado en el paso anterior.
1. Guardar el resultado en el disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
