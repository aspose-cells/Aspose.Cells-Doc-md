---
title: Поведение копирования и вставки свойств EnableClipboardCopyPaste и PasteType GridDesktop
type: docs
weight: 80
url: /ru/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: копировать, вставить, тип вставки GridPasteType
description: В этой статье описывается, как использовать GridPasteType для выполнения операции копирования и вставки в GridDesktop.
---

## **Возможные сценарии использования**
GridDesktop предоставляет различные варианты типов копирования и вставки с помощью свойства Aspose.Cells.GridDesktop.GridDesktop.PasteType. Эти варианты указываются перечислением Aspose.Cells.GridDesktop.Data.GridPasteType. Некоторые из них следующие

- GridPasteType.All

Он копирует и вставляет все из исходных ячеек в целевые ячейки.

- GridPasteType.Formulas

Он копирует и вставляет формулы из исходных ячеек в целевые ячейки.

- GridPasteType.Comments

Он копирует и вставляет комментарии из исходных ячеек в целевые ячейки.

- GridPasteType.RowHeights

Он копирует и вставляет высоты строк из исходных ячеек в целевые ячейки.

- GridPasteType.ColumnWidths

Он копирует и вставляет ширину столбцов из исходных ячеек в целевые ячейки.

и т.д.
## **Установите свойство EnableClipboardCopyPaste в True, чтобы включить свойство PasteType.**
Свойство Aspose.Cells.GridDesktop.GridDesktop.PasteType работает только в том случае, если вы установите свойство Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste в True, как показано на этом скриншоте.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Поведение свойств EnableClipboardCopyPaste и PasteType.**
При условии, что EnableClipboardCopyPaste является false, а PasteType - All, на следующем скриншоте показано, что при копировании ячейки B3 и вставке ее в ячейку C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

При условии, что EnableClipboardCopyPaste является true, а PasteType - All, после копирования изображения из Windows, на следующем скриншоте показано, что при копировании ячейки B3 и вставке ее в ячейку C5 также копируется изображение в ячейку C5.

![to do: скопировать изображение](copyimage.png)

![to do: после копирования выполнить вставку](aftercopy.png)


