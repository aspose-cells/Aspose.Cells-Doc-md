---
title: Split Panes in Python
type: docs
weight: 70
url: /java/split-panes-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Split Panes**
To split panes using **Aspose.Cells Java for Python**, simply invoke the **SplitPanes** method.

**Python Code**

{{< highlight java >}}

saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

# Split the worksheet window
workbook.getWorksheets().get(0).split();

# Save the Excel file
workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

# Print message
print "Panes split successfully."

{{< /highlight >}}

## **Download Running Code**
Download **Split Panes (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
