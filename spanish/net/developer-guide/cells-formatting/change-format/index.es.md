---
title: Cambiar el formato de una celda
description: Cómo usar la biblioteca Aspose.Cells en C# para cambiar el formato de las celdas, incluida la fuente, el color, el borde, etc. Al ajustar estas propiedades, tiene más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, cell formatting, C#, font, color, border
type: docs
weight: 105
url: /es/net/how-to-change-format-of-cell/
---
##  **Posibles escenarios de uso**
Cuando quieras resaltar ciertos datos, puedes cambiar el estilo de las celdas.

##  **Cómo cambiar el formato de una celda en Excel**

Para cambiar el formato de una sola celda en Excel, siga estos pasos:

1. Abra Excel y abra el libro que contiene la celda que desea formatear.

2. Localiza la celda que deseas formatear.

3. Haga clic derecho en la celda y seleccione "Formato Cells" en el menú contextual. Alternativamente, puede seleccionar la celda e ir a la pestaña Inicio en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Cells" y seleccionar "Formato Cells".

4. Aparecerá el cuadro de diálogo "Formato Cells". Aquí puede elegir varias opciones de formato para aplicar a la celda seleccionada. Por ejemplo, puede cambiar el estilo de fuente, el tamaño de fuente, el color de fuente, el formato de número, los bordes, el color de fondo, etc. Explore las diferentes pestañas en el cuadro de diálogo para acceder a varias opciones de formato.

5. Después de realizar los cambios de formato deseados, haga clic en el botón "Aceptar" para aplicar el formato a la celda seleccionada.


##  **Cómo cambiar el formato de una celda usando C#**

Para cambiar el formato de una celda usando Aspose.Cells, puede usar Puede usar los siguientes métodos:
1. [Cell.SetStyle(Estilo de estilo)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Estilo de estilo, bool explicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Estilo de estilo, indicador StyleFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


##  **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de trabajo y obtenemos dos celdas ("A2" y "B3"). Luego, obtenemos el estilo de la celda, configuramos varias opciones de formato (p. ej., color de fuente, negrita) y cambiamos el formato de la celda. Finalmente, guardamos el libro de trabajo en un archivo nuevo.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
