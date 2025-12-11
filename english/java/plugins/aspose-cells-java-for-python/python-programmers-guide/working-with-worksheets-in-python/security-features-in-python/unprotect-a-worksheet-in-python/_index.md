---
title: Unprotect a Worksheet in Python
type: docs
weight: 20
url: /java/unprotect-a-worksheet-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Unprotect a Worksheet**
To unprotect a worksheet using **Aspose.Cells Java for Python**, call the **unprotect_worksheet** method of the **protection** module.

**Python Code**

{{< highlight python >}}
filesFormatType = self.FileFormatType

# Instantiating a Workbook object
workbook = self.Workbook(self.dataDir + "Book1.xls")
worksheets = workbook.getWorksheets()
worksheet = worksheets.get(0)
protection = worksheet.getProtection()

# The following three methods are only for Excel 2000 and earlier formats
protection.setAllowEditingContent(False)
protection.setAllowEditingObject(False)
protection.setAllowEditingScenario(False)

# Unprotecting the worksheet
worksheet.unprotect()

# Save the Excel file.
workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

# Print message
print "Worksheet unprotected successfully."
{{< /highlight >}}

## **Download Running Code**
Download **Unprotect a Worksheet (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
