---
title: Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel
type: docs
weight: 20
url: /es/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Escenarios de uso posibles**

La ventana de seguimiento de fórmulas de Microsoft Excel es una herramienta útil para observar los valores de las celdas y sus fórmulas de manera conveniente en una ventana. Puedes abrir la *Ventana de seguimiento* usando Microsoft Excel haciendo clic en *Fórmulas > Seguimiento* *de fórmulas*. Tiene el botón *Agregar seguimiento* que se puede usar para agregar las celdas para su inspección. De manera similar, puedes utilizar el método [**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) para agregar celdas a la *Ventana de seguimiento* usando la API de Aspose.Cells.

## **Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel**

El siguiente código de ejemplo establece la fórmula de las celdas C1 y E1 y las agrega a la *Ventana de seguimiento*. Luego guarda el libro de trabajo como [archivo de Excel de salida](67338509.xlsx). Si abres el archivo de Excel de salida y ves la *Ventana de seguimiento*, verás ambas celdas como se muestra en esta captura de pantalla.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
