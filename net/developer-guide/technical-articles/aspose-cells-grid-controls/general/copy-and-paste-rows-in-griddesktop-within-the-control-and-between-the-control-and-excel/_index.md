---
title: Copy and Paste Rows in GridDesktop within the Control and between the Control and Excel
type: docs
weight: 70
url: /net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---

{{% alert color="primary" %}} 

If you want to enable copy and paste rows in GridDesktop within the control or between control and excel, then please set the GridDesktop.ClipboardCopyPaste property to true. You can set this property in design time or in code. The default value of this property is false. Currently, it can only copy and paste cell values and it will not copy any other setting of the cell like format, border style and so on.

{{% /alert %}} 
## **Setting GridDesktop.ClipboardCopyPaste property in Design Mode and Run Time**
The following sample code sets GridDesktop.ClipboardCopyPaste property in **Run Time**.



{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
