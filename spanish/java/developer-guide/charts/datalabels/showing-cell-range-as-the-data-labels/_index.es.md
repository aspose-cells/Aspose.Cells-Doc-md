---
title: Mostrar rango de celdas como las etiquetas de datos
type: docs
weight: 110
url: /es/java/showing-cell-range-as-the-data-labels/
---

## Mostrar rango de celdas como etiquetas de datos en MS Excel

En Microsoft Excel 2013, puede mostrar el rango de celdas para las etiquetas de datos. Puede seleccionar esta opción siguiendo estos pasos

- Seleccione las etiquetas de datos de la serie y haga clic derecho para abrir el menú emergente.
- Haga clic en **Dar formato a las etiquetas de datos...** y mostrará **Opciones de etiqueta**.
- Marca o desmarca la casilla de verificación **La etiqueta contiene - Valor de las celdas**.

### **Casilla de verificación para mostrar el rango de celdas como etiquetas de datos**

La siguiente captura de pantalla destaca esta opción para su referencia.

![todo:image_alt_text](showing-cell-range-as-the-data-labels_1.png)

## Mostrar rango de celdas como etiquetas de datos con Aspose.Cells

Aspose.Cells proporciona el método [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) para marcar o desmarcar la casilla de verificación **La etiqueta contiene - Valor de las celdas** como se muestra en la captura de pantalla anterior.

## Código Java para mostrar el rango de celdas como etiquetas de datos

El código de muestra a continuación accede a las Etiquetas de datos de la Serie de gráficos y luego establece el método [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) en true para marcar la opción **La etiqueta contiene - Valor de las celdas**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
{{< app/cells/assistant language="java" >}}
