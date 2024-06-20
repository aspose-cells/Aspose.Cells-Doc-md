---
title: Comportamiento de Copiar Pegar de las Propiedades EnableClipboardCopyPaste y PasteType de GridDesktop
type: docs
weight: 80
url: /es/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: copiar,pegar,GridPasteType
description: Este artículo describe cómo usar GridPasteType para realizar operaciones de copiar y pegar en GridDesktop.
---

## **Escenarios de uso posibles**
GridDesktop proporciona diferentes opciones de tipo de copiar y pegar con la propiedad Aspose.Cells.GridDesktop.GridDesktop.PasteType. Estas opciones se especifican con la enumeración Aspose.Cells.GridDesktop.Data.GridPasteType. Algunas de estas son las siguientes:

- GridPasteType.All

Copia y pega todo, desde las celdas de origen a las celdas de destino.

- GridPasteType.Formulas

Copia y pega fórmulas desde las celdas de origen a las celdas de destino.

- GridPasteType.Comments

Copia y pega comentarios desde las celdas de origen a las celdas de destino.

- GridPasteType.RowHeights

Copia y pega alturas de filas desde las celdas de origen a las celdas de destino.

- GridPasteType.ColumnWidths

Copia y pega anchos de columnas desde las celdas de origen a las celdas de destino.

etc.
## **Establezca la propiedad EnableClipboardCopyPaste en True para habilitar la propiedad PasteType.**
La propiedad Aspose.Cells.GridDesktop.GridDesktop.PasteType funciona solo si se establece la propiedad Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste como true, como se muestra en esta captura de pantalla.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Comportamiento de las propiedades EnableClipboardCopyPaste y PasteType**
Dado que EnableClipboardCopyPaste es false y PasteType es All, la siguiente captura de pantalla muestra que al copiar y pegar la celda B3 en la celda C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Dado que EnableClipboardCopyPaste es true y PasteType es All, después de copiar una imagen desde Windows. La siguiente captura de pantalla muestra que al copiar y pegar la celda B3 en la celda C5, también copia la imagen en la celda C5.

![todo:hacer copia de imagen](copyimage.png)

![todo:después de copiar haz pegar](aftercopy.png)


