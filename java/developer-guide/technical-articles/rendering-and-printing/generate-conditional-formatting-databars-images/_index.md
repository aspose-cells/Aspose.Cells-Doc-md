---
title: Generate Conditional Formatting DataBars Images
type: docs
weight: 170
url: /java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}} 

Sometimes, you need to generate images of Conditional Formatting DataBars. You can use Aspose.Cells [DataBar.toImage()](https://apireference.aspose.com/java/cells/com.aspose.cells/databar#toImage\(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions\)) method to generate these images. This article shows how to generate a DataBar image using Aspose.Cells.

{{% /alert %}} 
#### **Example**
The following sample code generates the DataBar image of cell C1. First, it accesses the format condition object of the cell, and then from that object, it accesses the DataBar object and uses its [DataBar.toImage()](https://apireference.aspose.com/java/cells/com.aspose.cells/databar#toImage\(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions\)) method to generate the image of the cell. Finally, it saves the image on disk.



{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
