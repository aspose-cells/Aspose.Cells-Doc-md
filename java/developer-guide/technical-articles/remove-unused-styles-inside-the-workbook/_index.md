---
title: Remove Unused Styles inside the Workbook
type: docs
weight: 470
url: /java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Unused styles in excel file not only takes space but also cause performance issues while converting to different formats like PDF, HTML, etc. Aspose.Cells provides the [Workbook.removeUnusedStyles()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#removeUnusedStyles\(\)) to remove all the unused styles inside the workbook.

{{% /alert %}} 
#### **Remove Unused Styles inside the Workbook**
The following code explains the usage of [Workbook.removeUnusedStyles()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#removeUnusedStyles\(\)). The code loads the [template excel file](5473451.xlsx) which you can download from the provided link. It contains an unused style named **AsposeStyle**, this style and all other unused styles will be removed after the execution of the code. Please see the following screenshot for more illustration.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
