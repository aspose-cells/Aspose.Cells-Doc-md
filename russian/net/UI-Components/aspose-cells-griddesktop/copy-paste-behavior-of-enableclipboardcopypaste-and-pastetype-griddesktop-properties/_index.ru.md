---
title: Поведение копирования и вставки свойств EnableClipboardCopyPaste и PasteType GridDesktop
type: docs
weight: 80
url: /ru/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **Возможные сценарии использования**
GridDesktop предоставляет различные типы параметров копирования и вставки с помощью свойства Aspose.Cells.GridDesktop.GridDesktop.PasteType. Эти параметры указаны с помощью перечисления Aspose.Cells.GridDesktop.Data.GridPasteType. Некоторые из них следующие:

- GridPasteType.All

Он копирует и вставляет все, от исходных ячеек до целевых ячеек.

- GridPasteType.Формулы

Он копирует и вставляет формулы из исходных ячеек в целевые.

- GridPasteType.Комментарии

Он копирует и вставляет комментарии из исходных ячеек в целевые ячейки.

- GridPasteType.RowHeights

Он копирует и вставляет высоты строк из исходных ячеек в целевые.

- GridPasteType.ColumnWidths

Он копирует и вставляет ширину столбцов из исходных ячеек в целевые ячейки.

и т. д.
##  **Установите для свойства EnableClipboardCopyPaste значение True, чтобы включить свойство PasteType.**
Свойство Aspose.Cells.GridDesktop.GridDesktop.PasteType работает, только если для свойства Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste установлено значение true, как показано на этом снимке экрана.

![задача: image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **Поведение свойств EnableClipboardCopyPaste и PasteType**
Учитывая, что EnableClipboardCopyPaste имеет значение false, а PasteType имеет значение All, на следующем снимке экрана показано, что при копировании и вставке ячейки B3 в ячейку C5.

![задача: image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Учитывая, что EnableClipboardCopyPaste имеет значение true, а PasteType имеет значение All, после копирования изображения из Windows. На следующем снимке экрана показано, что когда ячейка B3 копируется и вставляется в ячейку C5, изображение также копируется в ячейку C5.

![задача: скопировать изображение](copyimage.png)

![todo: после копирования сделать вставку](aftercopy.png)


