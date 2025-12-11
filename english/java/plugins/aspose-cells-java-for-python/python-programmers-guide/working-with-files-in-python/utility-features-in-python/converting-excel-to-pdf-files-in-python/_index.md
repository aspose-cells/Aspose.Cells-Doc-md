---
title: Converting Excel to PDF Files in Python
type: docs
weight: 20
url: /java/converting-excel-to-pdf-files-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting Excel To PDF**
To convert an Excel file to PDF using Aspose.Cells for Java in Python, simply invoke the `excel_to_pdf()` method of the Converter module.

**Python Code**

{{< highlight python >}}
saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format
workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

# Print message
print("\nExcel to PDF conversion performed successfully.")
{{< /highlight >}}

## **Download Running Code**
Download **Converting Excel To PDF (Aspose.Cells)** from any of the below-mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
