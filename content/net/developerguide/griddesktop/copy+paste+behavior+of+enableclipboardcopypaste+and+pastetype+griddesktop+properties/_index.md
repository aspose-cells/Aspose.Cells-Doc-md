---
title : "Copy Paste Behavior Of EnableClipboardCopyPaste and PasteType GridDesktop Properties" 
description : "" 
weight : 12653 
toc : false
type: docs
url: /net/developerguide/griddesktop/copy+paste+behavior+of+enableclipboardcopypaste+and+pastetype+griddesktop+properties/
---

# Aspose.Cells for .NET : Copy Paste Behavior Of EnableClipboardCopyPaste and PasteType GridDesktop Properties


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Set EnableClipboardCopyPaste Property True To Enable PasteType Property](#set-enableclipboardcopypaste-property-true-to-enable pastetype-property)
*   3 [Behavior Of EnableClipboardCopyPaste and PasteType Properties](#behavior-of-enableclipboardcopypaste-and-pastetype-properties)
{{< /panel >}}
 

## Possible Usage Scenarios

GridDesktop provides different types of copy paste type options with `Aspose.Cells.GridDesktop.GridDesktop.PasteType` property. These options are specified with `Aspose.Cells.GridDesktop.Data.GridPasteType` enumeration. Some of these are as follows

*   `GridPasteType.All`

It copies and paste everything from source cells to target cells.

*   `GridPasteType.Formulas`

It copies and paste formulas from source cells to target cells.

*   `GridPasteType.Comments`

It copies and paste comments from source cells to target cells.

*   `GridPasteType.RowHeights`

It copies and paste rows heights from source cells to target cells.

*   `GridPasteType.ColumnWidths`

It copies and paste columns widths from source cells to target cells.

etc.

## Set EnableClipboardCopyPaste Property True To Enable PasteType Property

`Aspose.Cells.GridDesktop.GridDesktop.PasteType` property works only if you set `Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste` property `true` as shown in this screenshot.

![image](55541835.png)

## Behavior Of EnableClipboardCopyPaste and PasteType Properties

Given that `EnableClipboardCopyPaste` is `false` and `PasteType` is `All`, the following screenshot shows that when cell B3 is copied and pasted to cell C5, cell formatting is not copied and only content of cell B3 is copied.

![image](55541834.png)

Given that `EnableClipboardCopyPaste` is `true` and `PasteType` is `All`, the following screenshot shows that when cell B3 is copied and pasted to cell C5, it also copies the formatting of the cell B3 to cell C5.

![image](55541833.png)

