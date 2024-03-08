---
title: Comportamiento de copiar y pegar de las propiedades de EnableClipboardCopyPaste y PasteType GridDesktop
type: docs
weight: 80
url: /es/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **Posibles escenarios de uso**
GridDesktop proporciona diferentes tipos de opciones de copiar y pegar con la propiedad Aspose.Cells.GridDesktop.GridDesktop.PasteType. Estas opciones se especifican con la enumeración Aspose.Cells.GridDesktop.Data.GridPasteType. Algunos de estos son los siguientes

- GridPasteType.Todos

Copia y pega todo, desde las celdas de origen hasta las celdas de destino.

- GridPasteType.Fórmulas

Copia y pega fórmulas de las celdas de origen a las celdas de destino.

- GridPasteType.Comentarios

Copia y pega comentarios de las celdas de origen a las celdas de destino.

- GridPasteType.RowHeights

Copia y pega alturas de filas desde las celdas de origen a las celdas de destino.

- GridPasteType.ColumnWidths

Copia y pega anchos de columnas desde las celdas de origen a las celdas de destino.

etc.
##  **Establezca la propiedad EnableClipboardCopyPaste como verdadera para habilitar la propiedad PasteType**
La propiedad Aspose.Cells.GridDesktop.GridDesktop.PasteType solo funciona si establece la propiedad Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste como verdadera, como se muestra en esta captura de pantalla.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **Comportamiento de las propiedades EnableClipboardCopyPaste y PasteType**
Dado que EnableClipboardCopyPaste es falso y PasteType es Todo, la siguiente captura de pantalla muestra que cuando la celda B3 se copia y pega en la celda C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Dado que EnableClipboardCopyPaste es verdadero y PasteType es Todo, después de copiar una imagen desde Windows. La siguiente captura de pantalla muestra que cuando la celda B3 se copia y pega en la celda C5, también copia la imagen en la celda C5.

![todo: copiar imagen](copyimage.png)

![todo: después de copiar y pegar](aftercopy.png)


