---
title: Formato de celdas
type: docs
weight: 50
url: /es/cpp/cells-formatting/
---

## **Formato de celda o rango de celdas**
Si quieres dar formato a una celda o a un rango de celdas, Aspose.Cells proporciona la clase [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Puedes lograr todo el formato de la celda o del rango de celdas utilizando esta clase. Algunas de las cosas relacionadas con el formato que se pueden lograr con la clase IStyle son las siguientes

- Establecer el color de relleno de la celda
- Establecer el ajuste de texto de la celda
- Establecer los bordes de las celdas como los bordes superior, izquierdo, inferior y derecho, etc.
- Establecer el color de fuente, tamaño de fuente, nombre de fuente, tachado, negrita, cursiva, subrayado, etc.
- Establecer la alineación horizontal o vertical del texto a derecha, izquierda, arriba, abajo, centro, etc.

Si desea establecer el estilo de una sola celda, por favor use el método [Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/), y si desea establecer el estilo de un rango de celdas, por favor use el método [Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).
## **Código de muestra**
El siguiente código de ejemplo formatea la celda C4 de la hoja de cálculo de varias formas y la captura de pantalla muestra el archivo de Excel de salida generado por ello para su referencia.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
