---
title: Freeze Panes in Python
type: docs
weight: 40
url: /java/freeze-panes-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Freeze Panes**
To freeze panes in the spreadsheet document using **Aspose.Cells Java for Python**, simply invoke the **FreezePanes** module.

**Python Code**

{{< highlight java >}}
 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()
worksheet = worksheets.get(0)

# Applying freeze panes settings
worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format
workbook.save(self.dataDir + "book.out.xls")

# Print Message
print "Panes freeze successful."
{{< /highlight >}}

## **Download Running Code**
Download **Hello World (Aspose.Cells)** from any of the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
