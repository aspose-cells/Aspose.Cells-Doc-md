---
title: Activación de hojas y activación de un Cell en la hoja de trabajo
type: docs
weight: 5
url: /es/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

A veces, necesita que una hoja de trabajo específica esté activa y se muestre cuando un usuario abre un archivo de Excel Microsoft en Excel. De manera similar, es posible que desee activar una celda específica y configurar las barras de desplazamiento para mostrar la celda activa. Aspose.Cells es capaz de realizar todas estas tareas como se demuestra a continuación.

-  Un**hoja activa** es una hoja en la que está trabajando: el nombre de la hoja activa en la pestaña está en negrita de forma predeterminada.
-  Un**Célula activa** es una celda seleccionada, la celda en la que se ingresan los datos cuando comienza a escribir. Solo una celda está activa a la vez. La celda activa está resaltada por un borde grueso.

{{% /alert %}}

## **Activando Hojas y Activando un Cell**

Aspose.Cells proporciona llamadas API específicas para activar una hoja y una celda. Por ejemplo, el[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)La propiedad es útil para configurar la hoja activa en un libro de trabajo. Del mismo modo, el[**Hoja de trabajo.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)La propiedad se puede usar para establecer y obtener una celda activa en la hoja de cálculo.

Para asegurarse de que las barras de desplazamiento horizontal o vertical estén en la posición del índice de fila y columna en la que desea mostrar datos específicos, use el[**Hoja de trabajo.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)y[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)propiedades.

El siguiente ejemplo muestra cómo activar una hoja de trabajo y hacer una celda activa en ella. El siguiente resultado se genera al ejecutar el código. Las barras de desplazamiento se desplazan para hacer que la segunda fila y la segunda columna sean sus primeras filas y columnas visibles.

**Configuración de la celda B2 como una celda activa**

![todo:imagen_alternativa_texto](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java código para configurar una hoja de cálculo activa en Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 En**evaluación** modo, es decir; sin establecer una licencia válida, la hoja de trabajo activa siempre será la que contenga la marca de agua de evaluación. Este comportamiento solo se puede anular configurando la licencia al inicio de la aplicación.

{{% /alert %}}
