---
title: Activando Hojas y Activando una Celda en la Hoja de Trabajo
type: docs
weight: 5
url: /es/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

A veces, necesitas que una hoja de cálculo específica esté activa y se muestre cuando un usuario abre un archivo de Microsoft Excel en Excel. Del mismo modo, es posible que desees activar una celda específica y configurar las barras de desplazamiento para mostrar la celda activa. Aspose.Cells es capaz de realizar todas estas tareas como se demuestra a continuación.

- Una **hoja activa** es una hoja en la que estás trabajando: el nombre de la hoja activa en la pestaña es negrita por defecto.
- Una **celda activa** es una celda seleccionada, la celda en la que se introduce datos cuando comienzas a escribir. Solo una celda está activa a la vez. La celda activa está resaltada por un borde pesado.

{{% /alert %}}

## **Activando Hojas y Activando una Celda**

Aspose.Cells proporciona llamadas de API específicas para activar una hoja y una celda. Por ejemplo, la propiedad [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) es útil para establecer la hoja activa en un libro. De manera similar, la propiedad [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) se puede utilizar para establecer y obtener una celda activa en la hoja de trabajo.

Para asegurarte de que las barras de desplazamiento horizontal o vertical estén en la posición del índice de fila y columna que deseas mostrar datos específicos, utiliza las propiedades [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) y [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn).

El siguiente ejemplo muestra cómo activar una hoja de cálculo y hacer una celda activa en ella. La siguiente salida se genera al ejecutar el código. Las barras de desplazamiento se desplazan para hacer que la 2ª fila y la 2ª columna sean su primera fila y columna visibles.

**Establecer la celda B2 como celda activa**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Código Java para establecer una hoja de cálculo activa en Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

En el modo de **evaluación**, es decir, sin establecer una licencia válida, la hoja de cálculo activa siempre será aquella que contenga la marca de agua de evaluación. Este comportamiento solo se puede anular configurando la licencia al inicio de la aplicación.

{{% /alert %}}
