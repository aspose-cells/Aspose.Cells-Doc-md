---
title: Combine Multiple Workbooks into a Single Workbook
type: docs
weight: 140
url: /net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}} 

Sometimes, you need to combine workbooks with various content like images, charts and data into a single workbook. Aspose.Cells supports this feature. This article shows how to create a console application in Visual Studio and combine workbooks with a few, simple lines of code using Aspose.Cells.

{{% /alert %}} 
## **Combining Workbooks with Images and Charts**
The example code combines two workbooks into a single workbook using Aspose.Cells. The code loads the source workbooks, uses the [Workbook.combine()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/combine) method to combine them and saves the output workbook.
#### **Source Workbooks**
- [charts.xlsx](https://docs-qa.aspose.com/download/attachments/5276659/charts.xlsx?version=1&modificationDate=1447513883960&api=v2)
- [picture.xlsx](https://docs-qa.aspose.com/download/attachments/5276659/picture.xlsx?version=1&modificationDate=1447513883983&api=v2)
#### **Output Workbooks**
- [combined.xlsx](https://docs-qa.aspose.com/download/attachments/5276659/combined.xlsx?version=1&modificationDate=1447513884007&api=v2)
#### **Screenshots**
Below are screenshots of the source and output workbooks.

{{% alert color="primary" %}} 

You can use any source workbooks. These images are just for illustration purposes.

{{% /alert %}} 

**The first worksheet of the charts workbook - stacked** 

![todo:image_alt_text](/download/attachments/5276659/492304421)

**Second worksheet of charts workbook - line** 

![todo:image_alt_text](/download/attachments/5276659/513738217)

**First worksheet of the picture workbook - picture** 

![todo:image_alt_text](/download/attachments/5276659/1643767719)

**All three worksheets in the combined workbook - stacked, line, picture** 

![todo:image_alt_text](/download/attachments/5276659/386304632)

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}
