---
title: EnableClipboardCopyPaste 和 PasteType GridDesktop 属性的复制粘贴行为
type: docs
weight: 80
url: /zh/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **可能的使用场景**
GridDesktop 通过 Aspose.Cells.GridDesktop.GridDesktop.PasteType 属性提供不同类型的复制粘贴类型选项。这些选项通过 Aspose.Cells.GridDesktop.Data.GridPasteType 枚举指定。其中一些如下

- GridPasteType.All

它将所有内容从源单元格复制并粘贴到目标单元格。

- GridPasteType.Formulas

它将公式从源单元格复制并粘贴到目标单元格。

- GridPasteType.Comments

它将注释从源单元格复制并粘贴到目标单元格。

- GridPasteType.RowHeights

它将行高从源单元格复制并粘贴到目标单元格。

- GridPasteType.ColumnWidths

它将列宽从源单元格复制并粘贴到目标单元格。

ETC。
##  **将 EnableClipboardCopyPaste 属性设置为 True 以启用 PasteType 属性**
仅当您将 Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste 属性设置为 true 时，Aspose.Cells.GridDesktop.GridDesktop.PasteType 属性才有效，如此屏幕截图所示。

![待办事项：图像_替代_文本](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **EnableClipboardCopyPaste 和 PasteType 属性的行为**
假定 EnableClipboardCopyPaste 为 false 并且 PasteType 为 All，以下屏幕截图显示了当单元格 B3 被复制并粘贴到单元格 C5 时。

![待办事项：图像_替代_文本](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

假设 EnableClipboardCopyPaste 为 true 并且 PasteType 为 All，从 windows 复制图像后。下面的屏幕截图显示，当单元格 B3 复制并粘贴到单元格 C5 时，它也会将图像复制到单元格 C5。

![待办事项：复制图像](copyimage.png)

![待办事项：复制后粘贴](aftercopy.png)


