---
title: Cells Formateo
type: docs
weight: 50
url: /es/cpp/cells-formatting/
---
## **Formato Cell o Rango de Cells**
 Si desea formatear una celda o un rango de celdas, entonces Aspose.Cells proporciona el[estilo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)clase. Puede realizar todo el formato de la celda o rango de celdas usando esta clase. Algunas de las cosas relacionadas con el formato que se pueden lograr con la clase IStyle son las siguientes

- Establecer el color de relleno de la celda
- Establecer el ajuste de texto de la celda
- Establezca los bordes de las celdas como los bordes superior, izquierdo, inferior y derecho, etc.
- Establezca el color de la fuente, el tamaño de la fuente, el nombre de la fuente, el tachado, la negrita, la cursiva, el subrayado, etc.
- Establezca la alineación horizontal o vertical del texto a la derecha, izquierda, arriba, abajo, al centro, etc.

 Si desea establecer el estilo de una sola celda, utilice[ICell->Establecer EstiloI()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5) método y si desea establecer el estilo de un rango de celdas, utilice[IRange->AplicarIEstilo()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)método.
## **Código de muestra**
 El siguiente código de ejemplo da formato a la celda C4 de la hoja de trabajo de varias maneras y la captura de pantalla muestra el[archivo de salida de Excel](21266438.xlsx)generado por él para su referencia.

![todo:imagen_alternativa_texto](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
