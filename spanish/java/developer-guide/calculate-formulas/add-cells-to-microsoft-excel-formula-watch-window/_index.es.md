---
title: Agregar Cells a Microsoft Ventana de visualización de fórmulas de Excel
type: docs
weight: 20
url: /es/java/add-cells-to-microsoft-excel-formula-watch-window/
---
## **Posibles escenarios de uso**

Microsoft Excel Watch Window es una herramienta útil para ver los valores de las celdas y sus fórmulas convenientemente en una ventana. Puedes abrir el*Ventana de vigilancia*usando Microsoft Excel haciendo clic en el*Fórmulas > Ver* *Ventana*. tiene el*Agregar reloj*botón que se puede usar para agregar las celdas para su inspección. Del mismo modo, puede utilizar[**Hoja de trabajo.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) método para agregar celdas en*Ventana de vigilancia*usando Aspose.Cells API.

## **Agregar Cells a Microsoft Ventana de visualización de fórmulas de Excel**

 El siguiente código de ejemplo establece la fórmula de las celdas C1 y E1 y agrega ambas a*Ventana de vigilancia*. A continuación, guarda el libro de trabajo como[archivo de salida de Excel](67338509.xlsx). Si abre el archivo de salida de Excel y ve el*Ventana de vigilancia*, verá ambas celdas como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
