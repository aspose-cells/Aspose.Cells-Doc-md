---
title: Comportamiento de copiar y pegar de las propiedades EnableClipboardCopyPaste y PasteType GridDesktop
type: docs
weight: 80
url: /es/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
## **Posibles escenarios de uso**
GridDesktop proporciona diferentes tipos de opciones de tipo copiar y pegar con la propiedad Aspose.Cells.GridDesktop.GridDesktop.PasteType. Estas opciones se especifican con la enumeración Aspose.Cells.GridDesktop.Data.GridPasteType. Algunos de estos son los siguientes

- GridPasteType.All

Copia y pega todo, desde las celdas de origen hasta las celdas de destino.

- GridPasteType.Formulas

Copia y pega fórmulas desde las celdas de origen a las celdas de destino.

- GridPasteType.Comentarios

Copia y pega comentarios de las celdas de origen a las celdas de destino.

- GridPasteType.RowHeights

Copia y pega la altura de las filas de las celdas de origen a las celdas de destino.

- GridPasteType.ColumnWidths

Copia y pega anchos de columnas desde las celdas de origen a las celdas de destino.

etc.
## **Establezca la propiedad EnableClipboardCopyPaste en True para habilitar la propiedad PasteType**
La propiedad Aspose.Cells.GridDesktop.GridDesktop.PasteType solo funciona si configura la propiedad Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste como verdadera, como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Comportamiento de las propiedades EnableClipboardCopyPaste y PasteType**
Dado que EnableClipboardCopyPaste es false y PasteType es All, la siguiente captura de pantalla muestra que cuando la celda B3 se copia y se pega en la celda C5, el formato de la celda no se copia y solo se copia el contenido de la celda B3.

![todo:imagen_alternativa_texto](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_2.png)

Dado que EnableClipboardCopyPaste es verdadero y PasteType es Todo, la siguiente captura de pantalla muestra que cuando la celda B3 se copia y se pega en la celda C5, también se copia el formato de la celda B3 en la celda C5.

![todo:imagen_alternativa_texto](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)


