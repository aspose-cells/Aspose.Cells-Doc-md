---
title: Combine Multiple Workbooks into a Single Workbook
type: docs
weight: 80
url: /java/combine-multiple-workbooks-into-a-single-workbook/
description: Combine multiple workbooks into single workbooks by using Java code and Aspose.Cells for Java API.
keywords: combine multiple workbooks into one, combine multiple workbooks into one java, combine multiple workbooks into one with java, combine multiple workbooks into single workbook with java, combine multiple workbooks into single workbook java, java code to combine multiple workbooks into single workbook, how to combine multiple workbooks into single workbook with java, how to combine multiple workbooks into one with java, merge multiple workbooks into one with java, how to merge multiple workbooks into one java, how to merge multiple workbooks into one with java
---

{{% alert color="primary" %}}

Sometimes, you need to combine workbooks with various content like images, charts, and data into a single workbook. Aspose.Cells supports this feature. This article shows how to create a simple application to combine workbooks with a few, simple lines of code using Aspose.Cells.

{{% /alert %}}

## **Combining Workbooks**

The example code combines two workbooks into a single workbook using Aspose.Cells for Java. The code loads the source workbooks, uses the [**Workbook.combine()**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) method to combine them and saves the output workbook.

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

The following code snippet shows how to combine multiple workbooks into a single workbook.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorkbooks-CombineMultipleWorkbooks.java" >}}

## **Additional Resources**

{{% alert color="primary" %}}

You may find the [Combine Multiple Worksheets into a Single Worksheet](/cells/java/combine-multiple-worksheets-into-a-single-worksheet/) article useful for more information.

{{% /alert %}}
