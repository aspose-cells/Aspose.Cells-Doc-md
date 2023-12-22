---
title: Cells Formateo
type: docs
weight: 50
url: /es/cpp/cells-formatting/
---
##  **Formato Cell o Rango de Cells**
 Si desea formatear una celda o un rango de celdas, entonces Aspose.Cells proporciona la[Estilo](https://reference.aspose.com/cells/cpp/aspose.cells/style/)clase. Puede realizar todo el formato de la celda o rango de celdas usando esta clase. Algunas de las cosas relacionadas con el formato que se pueden lograr con la clase IStyle son las siguientes

- Establecer color de relleno de la celda
- Establecer el ajuste del texto de la celda.
- Establezca los bordes de las celdas como los bordes superior, izquierdo, inferior y derecho, etc.
- Establezca el color de fuente, tamaño de fuente, nombre de fuente, tachado, negrita, cursiva, subrayado, etc.
- Establezca la alineación horizontal o vertical del texto a la derecha, izquierda, arriba, abajo, centro, etc.

 Si desea establecer el estilo de una sola celda, utilice[Cell->Establecer estilo()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) método y si desea establecer el estilo de un rango de celdas, utilice[Rango->AplicarEstilo()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)método.
##  **Código de muestra**
 El siguiente código de muestra formatea la celda C4 de la hoja de trabajo de varias maneras y la captura de pantalla muestra la[archivo de excel de salida](21266438.xlsx) generado por él para su referencia.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
