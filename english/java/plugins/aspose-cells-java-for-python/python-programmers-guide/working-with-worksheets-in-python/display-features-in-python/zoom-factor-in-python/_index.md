---
title: Zoom Factor in Python
type: docs
weight: 80
url: /java/zoom-factor-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Zoom Factor**
To set Zoom Factor using **Aspose.Cells Java for Python**, simply invoke **ZoomFactor** module.

**Python Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **Download Running Code**
Download **Zoom Factor (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
