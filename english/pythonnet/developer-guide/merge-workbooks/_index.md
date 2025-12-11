---
title: Combine Multiple Workbooks into a Single Workbook
linktitle: Workbook Merger
type: docs
weight: 66
url: /python-net/combine-multiple-workbooks-into-a-single-workbook/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to combine workbooks with various content like images, charts, and data into a single workbook. Aspose.Cells for Python via .NET supports this feature. This article shows how to create a console application in Visual Studio and combine workbooks with a few simple lines of code using Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Combining Workbooks with Images and Charts**

The example code combines two workbooks into a single workbook using Aspose.Cells for Python via .NET. The code loads the source workbooks, uses the [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) method to combine them, and saves the output workbook.

### **Source Workbooks**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Output Workbooks**

- [combined.xlsx](5473095.xlsx)

### **Screenshots**

Below are screenshots of the source and output workbooks.

{{% alert color="primary" %}}

You can use any source workbooks. These images are provided for illustration purposes.

{{% /alert %}}

**The first worksheet of the charts workbook – stacked** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Second worksheet of the charts workbook – line** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**First worksheet of the picture workbook – picture** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**All three worksheets in the combined workbook – stacked, line, picture** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Advanced topics**
- [Combine Multiple Worksheets into a Single Worksheet](/cells/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Merge Files](/cells/python-net/merge-files/)

{{< app/cells/assistant language="python-net" >}}
