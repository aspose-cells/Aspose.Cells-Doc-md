---
title: Display or Hide Gridlines in Python
type: docs
weight: 10
url: /java/display-or-hide-gridlines-in-python/
description: Learn how to  Display or Hide Gridlines through the Aspose.Cells for Python Via Java API.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---

## **Aspose.Cells - How to Display or Hide Gridlines**
### **How to Hide Gridlines**
To hide worksheet using **Aspose.Cells Java for Ruby**, call **displayhidegridlines** module.

**Python Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **How to Display Gridlines**
To make gridlines visible, use the the Worksheet class' setGridlinesVisible(true) method.

**Python Code**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Download Running Code**
Download **DisplayHideGridlines (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
