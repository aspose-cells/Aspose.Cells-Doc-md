---
title: Cambiar el formato de una celda
description: Cómo usar la biblioteca Aspose.Cells en C# para cambiar el formato de las celdas, incluida la fuente, el color, el borde, etc. Al ajustar estas propiedades, tiene un mayor control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, formato de celda, C#, fuente, color, borde
type: docs
weight: 105
url: /es/net/how-to-change-format-of-cell/
---


## **Escenarios de uso posibles**
Cuando desee resaltar ciertos datos, puede cambiar el estilo de las celdas.

## **Cómo cambiar el formato de una celda en Excel**

Para cambiar el formato de una sola celda en Excel, siga estos pasos:

1. Abra Excel y abra el libro que contiene la celda que desea formatear.

2. Localice la celda que desea formatear.

3. Haga clic con el botón derecho en la celda y seleccione "Formato de celdas" en el menú contextual. Alternativamente, puede seleccionar la celda, ir a la pestaña Inicio en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Celdas" y seleccionar "Formato de celdas".

4. Aparecerá el cuadro de diálogo "Formato de celdas". Aquí, puede elegir varias opciones de formato para aplicar a la celda seleccionada. Por ejemplo, puede cambiar el estilo de fuente, el tamaño de fuente, el color de fuente, el formato de número, los bordes, el color de fondo, etc. Explore las diferentes pestañas en el cuadro de diálogo para acceder a varias opciones de formato.

5. Después de realizar los cambios de formato deseados, haga clic en el botón "Aceptar" para aplicar el formato a la celda seleccionada.


## **Cómo cambiar el formato de una celda utilizando C#**

Para cambiar el formato de una celda usando Aspose.Cells, puede usar los siguientes métodos:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


## **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de cálculo y obtenemos dos celdas ("A2" y "B3"). Luego, obtenemos el estilo de la celda, establecemos varias opciones de formato (por ejemplo, color de fuente, negrita) y cambiamos el formato de la celda. Finalmente, guardamos el libro en un nuevo archivo.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
