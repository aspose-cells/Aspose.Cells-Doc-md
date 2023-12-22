---
title: Rangos de formato
type: docs
weight: 105
url: /es/net/how-to-format-a-range/
---
##  **Posibles escenarios de uso**
Cuando necesite aplicar un estilo a un rango, puede utilizar el formato de rango.

##  **Cómo formatear un rango en Excel**

Para dar formato a un rango de celdas en Excel, puede utilizar las opciones de formato integradas proporcionadas por Excel. A continuación se explica cómo puede formatear un rango de celdas directamente en Excel:

1. Abra Excel y abra el libro que contiene el rango que desea formatear.

2. Seleccione el rango de celdas que desea formatear. Puede hacer clic y arrastrar para seleccionar el rango, o puede usar atajos de teclado como Mayús + teclas de flecha para ampliar la selección.

3. Una vez seleccionado el rango, haga clic derecho en el rango seleccionado y elija "Formato Cells" en el menú contextual. Alternativamente, puede ir a la pestaña Inicio en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Cells" y seleccionar "Formato Cells".

4. Aparecerá el cuadro de diálogo "Formato Cells". Aquí puede elegir varias opciones de formato para aplicarlas al rango seleccionado. Por ejemplo, puede cambiar el estilo de fuente, el tamaño de fuente, el color de fuente, el formato de número, los bordes, el color de fondo, etc. Explore las diferentes pestañas en el cuadro de diálogo para acceder a varias opciones de formato.

5. Después de realizar los cambios de formato deseados, haga clic en el botón "Aceptar" para aplicar el formato al rango seleccionado.


##  **Cómo formatear un rango usando C#**

Para formatear un rango usando Aspose.Cells, puede usar Puede usar los siguientes métodos:
1. [Range.ApplyStyle (estilo de estilo, indicador StyleFlag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Estilo de estilo)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Estilo de estilo)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


##  **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de trabajo y definimos dos rangos ("A1:C3" y "A4:C5"). Luego, creamos nuevos estilos, configuramos varias opciones de formato (por ejemplo, color de fuente, negrita) y aplicamos el estilo al rango. Finalmente, guardamos el libro de trabajo en un archivo nuevo.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
