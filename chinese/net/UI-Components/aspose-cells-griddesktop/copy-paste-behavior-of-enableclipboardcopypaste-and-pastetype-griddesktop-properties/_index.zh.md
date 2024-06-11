---
title: 启用ClipboardCopyPaste和GridDesktop属性PasteType的复制粘贴行为
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: 复制，粘贴，GridPasteType
description: 本文描述如何使用GridPasteType执行GridDesktop中的复制粘贴操作。
---

## **可能的使用场景**
GridDesktop通过Aspose.Cells.GridDesktop.GridDesktop.PasteType属性提供了不同类型的复制粘贴选项。 这些选项使用Aspose.Cells.GridDesktop.Data.GridPasteType枚举进行指定。 其中一些如下所示

- GridPasteType.All

它将从源单元格复制并粘贴到目标单元格的所有内容。

- GridPasteType.Formulas

它将从源单元格复制并粘贴到目标单元格的公式。

- GridPasteType.Comments

它将从源单元格复制并粘贴到目标单元格的批注。

- GridPasteType.RowHeights

它将从源单元格复制并粘贴到目标单元格的行高度。

- GridPasteType.ColumnWidths

它将从源单元格复制并粘贴到目标单元格的列宽度。

等等。
## **将EnableClipboardCopyPaste属性设置为True以启用PasteType属性**
仅当您将Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste属性设置为true时，Aspose.Cells.GridDesktop.GridDesktop.PasteType属性才会起作用，如本截图所示。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **启用ClipboardCopyPaste和PasteType属性的行为**
鉴于EnableClipboardCopyPaste为false且PasteType为All，以下截图显示了将单元格B3复制并粘贴到单元格C5的情况。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

假设EnableClipboardCopyPaste为true且PasteType为All，在Windows上复制图像后，当将B3单元格复制并粘贴到C5单元格时，如下屏幕截图所示，它也会将图像复制到C5单元格。

![todo:复制图像](copyimage.png)

![todo:复制后粘贴](aftercopy.png)


