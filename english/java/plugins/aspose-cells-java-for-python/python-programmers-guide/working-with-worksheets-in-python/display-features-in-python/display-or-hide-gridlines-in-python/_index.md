---
title: Display or Hide Gridlines in Python
type: docs
weight: 10
url: /java/display-or-hide-gridlines-in-python/
description: Learn how to display or hide gridlines using the Aspose.Cells for Python via Java API.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - How to Display or Hide Gridlines**
### **How to Hide Gridlines**
To hide gridlines in a worksheet using **Aspose.Cells for Python via Java**, call the **displayHideGridlines** module.

**Python Code**

{{< highlight java >}}
workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()
worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file
worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in the default (that is Excel 2000) format
workbook.save(self.dataDir + "output.xls")

# Print message
print "Grid lines are now hidden on sheet 1, please check the output document."
{{< /highlight >}}

### **How to Display Gridlines**
To make gridlines visible, use the Worksheet class's `setGridlinesVisible(true)` method.

**Python Code**

{{< highlight python >}}
# Displaying the gridlines of the worksheet
worksheet.setGridlinesVisible(True)
{{< /highlight >}}

## **Download Running Code**
Download **DisplayHideGridlines (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
