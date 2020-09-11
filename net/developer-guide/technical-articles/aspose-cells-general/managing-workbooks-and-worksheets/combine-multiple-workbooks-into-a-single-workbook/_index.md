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

The example code combines two workbooks into a single workbook using Aspose.Cells. The code loads the source workbooks, uses the [**Workbook.combine()**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) method to combine them and saves the output workbook.

### **Source Workbooks**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Output Workbooks**

- [combined.xlsx](5473095.xlsx)

### **Screenshots**

Below are screenshots of the source and output workbooks.

{{% alert color="primary" %}}

You can use any source workbooks. These images are just for illustration purposes.

{{% /alert %}}

**The first worksheet of the charts workbook - stacked** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Second worksheet of charts workbook - line** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**First worksheet of the picture workbook - picture** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**All three worksheets in the combined workbook - stacked, line, picture** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}
