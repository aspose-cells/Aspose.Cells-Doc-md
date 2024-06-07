---
title: 复制粘贴的启用ClipboardCopyPaste和PasteType GridDesktop 属性
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: 复制、粘贴、GridPasteType
description: 本文介绍如何使用 GridPasteType 进行复制粘贴操作在 GridDesktop 中
---

## **可能的使用场景**
GridDesktop 提供了不同类型的复制粘贴选项，通过 Aspose.Cells.GridDesktop.GridDesktop.PasteType 属性。这些选项使用 Aspose.Cells.GridDesktop.Data.GridPasteType 枚举来制定。其中一些如下

- GridPasteType.All

从源单元格复制并粘贴到目标单元格

- GridPasteType.Formulas

从源单元格复制并粘贴到目标单元格的公式

- GridPasteType.Comments

从源单元格复制并粘贴到目标单元格的注释

- GridPasteType.RowHeights

从源单元格复制并粘贴到目标单元格的行高

- GridPasteType.ColumnWidths

从源单元格复制并粘贴到目标单元格的列宽

等等
## **设置 EnableClipboardCopyPaste 属性为 True 以启用 PasteType 属性**
只有在将 Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste 属性设置为 true 时，Aspose.Cells.GridDesktop.GridDesktop.PasteType 属性才有效，如此屏幕截图所示。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **EnableClipboardCopyPaste 和 PasteType 属性的行为**
假设 EnableClipboardCopyPaste 为 false 而 PasteType 为 All，下面的截图显示了将单元格 B3 复制并粘贴到单元格 C5 时的情况。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

假设 EnableClipboardCopyPaste 为 true 而 PasteType 为 All，在从 Windows 复制图像之后。下面的截图显示了将单元格 B3 复制并粘贴到单元格 C5 时，也将图像复制到单元格 C5。

![待办：复制图像](copyimage.png)

![待办：复制后粘贴](aftercopy.png)


