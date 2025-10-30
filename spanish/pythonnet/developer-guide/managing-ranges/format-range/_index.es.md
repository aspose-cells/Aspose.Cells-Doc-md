---
title: Formato de rangos
type: docs
weight: 105
url: /es/python-net/how-to-format-a-range/
description: Este artículo describe cómo formatear rangos con Aspose.Cells para la biblioteca de Python via .NET.
keywords: Biblioteca de Excel de Python, Cómo formatear un rango, Cómo formatear rangos.
---

## **Escenarios de uso posibles**
Cuando necesitas aplicar un estilo a un rango, puedes usar el formato de rango.

## **Cómo dar formato a un rango en Excel**

Para dar formato a un rango de celdas en Excel, puedes usar las opciones de formato integradas proporcionadas por Excel. Así es como puedes dar formato a un rango de celdas directamente en Excel:

1. Abre Excel y el libro que contiene el rango que deseas formatear.

2. Selecciona el rango de celdas que deseas formatear. Puedes hacer clic y arrastrar para seleccionar el rango, o puedes usar atajos de teclado como Shift + Flechas para extender la selección.

3. Una vez seleccionado el rango, haz clic derecho en el rango seleccionado y elige "Formato de celdas" en el menú contextual. Alternativamente, ve a la pestaña Inicio en la cinta de Excel, haz clic en el menú desplegable "Formato" en el grupo "Celdas", y selecciona "Formato de celdas".

4. Aparecerá el cuadro de diálogo "Formato de celdas". Aquí, puedes elegir varias opciones de formato para aplicar al rango seleccionado. Por ejemplo, puedes cambiar el estilo de fuente, tamaño de fuente, color de fuente, formato de número, bordes, color de fondo, etc. Explora las distintas pestañas en el cuadro de diálogo para acceder a varias opciones de formato.

5. Después de realizar los cambios de formato deseados, haz clic en el botón "Aceptar" para aplicar el formato al rango seleccionado.


## **Cómo dar formato a un rango usando C#**

Para dar formato a un rango usando Aspose.Cells, puedes usar los siguientes métodos:
1. [Range.apply_style(style, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag)
2. [Range.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style)
3. [Range.set_style(style, explicit_flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style-bool)


## **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de trabajo y definimos dos rangos ("A1:C3" y "A4:C5"). Luego, creamos nuevos estilos, establecemos varias opciones de formato (por ej., color de fuente, negrita) y aplicamos el estilo al rango. Finalmente, guardamos el libro en un nuevo archivo.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-FormatRanges.py" >}}
{{< app/cells/assistant language="python-net" >}}
