---
title: Копирование и вставка поведения свойств EnableClipboardCopyPaste и PasteType GridDesktop
type: docs
weight: 80
url: /ru/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
## **Возможные сценарии использования**
GridDesktop предоставляет различные типы параметров копирования и вставки со свойством Aspose.Cells.GridDesktop.GridDesktop.PasteType. Эти параметры указаны в перечислении Aspose.Cells.GridDesktop.Data.GridPasteType. Некоторые из них следующие

- GridPasteType.All

Он копирует и вставляет все из исходных ячеек в целевые.

- GridPasteType.Формулы

Он копирует и вставляет формулы из исходных ячеек в целевые ячейки.

- GridPasteType.Comments

Он копирует и вставляет комментарии из исходных ячеек в целевые ячейки.

- GridPasteType.RowHeights

Он копирует и вставляет высоты строк из исходных ячеек в целевые ячейки.

- GridPasteType.ColumnWidths

Он копирует и вставляет ширину столбцов из исходных ячеек в целевые ячейки.

и т.п.
## **Установите для свойства EnableClipboardCopyPaste значение True, чтобы включить свойство PasteType**
Свойство Aspose.Cells.GridDesktop.GridDesktop.PasteType работает, только если для свойства Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste установлено значение true, как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Поведение свойств EnableClipboardCopyPaste и PasteType**
Учитывая, что EnableClipboardCopyPaste имеет значение false, а PasteType — All, на следующем снимке экрана показано, что когда ячейка B3 копируется и вставляется в ячейку C5, форматирование ячейки не копируется, а копируется только содержимое ячейки B3.

![дело:изображение_альтернативный_текст](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_2.png)

Учитывая, что EnableClipboardCopyPaste имеет значение true, а PasteType — All, на следующем снимке экрана показано, что когда ячейка B3 копируется и вставляется в ячейку C5, форматирование ячейки B3 также копируется в ячейку C5.

![дело:изображение_альтернативный_текст](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)


