##Copy Paste Behavior Of EnableClipboardCopyPaste and PasteType GridDesktop Properties
This article describes how to use the GridPasteType to do copy paste operation in GridDesktop.
## **Possible Usage Scenarios**
GridDesktop provides different types of copy paste type options with Aspose.Cells.GridDesktop.GridDesktop.PasteType property. These options are specified with Aspose.Cells.GridDesktop.Data.GridPasteType enumeration. Some of these are as follows
- GridPasteType.All
It copies and paste everything from source cells to target cells.
- GridPasteType.Formulas
It copies and paste formulas from source cells to target cells.
- GridPasteType.Comments
It copies and paste comments from source cells to target cells.
- GridPasteType.RowHeights
It copies and paste rows heights from source cells to target cells.
- GridPasteType.ColumnWidths
It copies and paste columns widths from source cells to target cells.
etc.
## **Set EnableClipboardCopyPaste Property True To Enable PasteType Property**
Aspose.Cells.GridDesktop.GridDesktop.PasteType property works only if you set Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste property true as shown in this screenshot.
![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Behavior Of EnableClipboardCopyPaste and PasteType Properties**
Given that EnableClipboardCopyPaste is false and PasteType is All, the following screenshot shows that when cell B3 is copied and pasted to cell C5.
![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)
Given that EnableClipboardCopyPaste is true and PasteType is All,after copy an image from windows . the following screenshot shows that when cell B3 is copied and pasted to cell C5, it also copies the image to cell C5.
![todo:do copy image](copyimage.png)
![todo:after copy do paste](aftercopy.png)
