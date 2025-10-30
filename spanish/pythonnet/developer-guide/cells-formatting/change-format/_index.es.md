---
title: Cambiar el formato de una celda
description: Cómo usar la biblioteca Aspose.Cells para Python via .NET para cambiar el formato de las celdas, incluyendo fuente, color, borde, etc. Al ajustar estas propiedades, tendrás más control sobre la apariencia de las celdas.
keywords: Biblioteca Aspose.Cells para Python via .NET, formateo de celdas, Python, fuente, color, borde
type: docs
weight: 20
url: /es/python-net/how-to-change-format-of-cell/
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

Para cambiar el formato de una celda usando Aspose.Cells para Python via .NET, puedes usar los siguientes métodos:
1. [Cell.set_style(estilo)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style)
2. [Cell.set_style(estilo, bandera_explícita)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-bool)
3. [Cell.set_style(estilo, indicador)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-aspose.cells.StyleFlag)


## **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de cálculo y obtenemos dos celdas ("A2" y "B3"). Luego, obtenemos el estilo de la celda, establecemos varias opciones de formato (por ejemplo, color de fuente, negrita) y cambiamos el formato de la celda. Finalmente, guardamos el libro en un nuevo archivo.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-change-format.py" >}}

{{< app/cells/assistant language="python-net" >}}
