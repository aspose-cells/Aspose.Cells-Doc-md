---
title: Formato de rangos
type: docs
weight: 105
url: /es/net/how-to-format-a-range/
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
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


## **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de trabajo y definimos dos rangos ("A1:C3" y "A4:C5"). Luego, creamos nuevos estilos, establecemos varias opciones de formato (por ej., color de fuente, negrita) y aplicamos el estilo al rango. Finalmente, guardamos el libro en un nuevo archivo.
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
