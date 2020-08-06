---
title: Remove Unused Styles inside the Workbook
type: docs
weight: 340
url: /net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Unused styles in excel file not only take space but also cause performance issues while converting to different formats like PDF, HTML, etc. Aspose.Cells provides the [Workbook.RemoveUnusedStyles()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/removeunusedstyles) to remove all the unused styles inside the workbook.

{{% /alert %}} 

The following code explains the usage of [Workbook.RemoveUnusedStyles()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/removeunusedstyles). The code loads the [template excel file](attachments/5024962/5115520.xlsx) which you can download from the provided link. It contains an unused style named **AsposeStyle**, this style and all other unused styles will be removed after the execution of the code.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
