---
title: Combine Multiple Workbooks into a Single Workbook
type: docs
weight: 80
url: /java/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}} 

Sometimes, you need to combine workbooks with various content like images, charts, and data into a single workbook. Aspose.Cells supports this feature. This article shows how to create a simple application to combine workbooks with a few, simple lines of code using Aspose.Cells.

{{% /alert %}} 
### **Combining Workbooks**
The example code combines two workbooks into a single workbook using Aspose.Cells for Java. The code loads the source workbooks, uses the [Workbook.combine()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#combine\(com.aspose.cells.Workbook\)) method to combine them and saves the output workbook.
#### **Source Workbooks**
- [charts.xlsx](attachments/5276659/5473097.xlsx)
- [picture.xlsx](attachments/5276659/5473096.xlsx)
#### **Output Workbooks**
- [combined.xlsx](attachments/5276659/5473095.xlsx)
#### **Screenshots**
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

The following code snippet shows how to combine multiple workbooks into a single workbook.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorkbooks-CombineMultipleWorkbooks.java" >}}
### **Additional Resources**
{{% alert color="primary" %}} 

You may find the [Combine Multiple Worksheets into a Single Worksheet](/cells/java/combine-multiple-worksheets-into-a-single-worksheet/) article useful for more information.

{{% /alert %}}
