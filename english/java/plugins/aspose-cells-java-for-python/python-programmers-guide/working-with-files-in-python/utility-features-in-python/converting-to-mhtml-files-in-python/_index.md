---
title: Converting To MHTML Files in Python
type: docs
weight: 30
url: /java/converting-to-mhtml-files-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting To MHTML**
To convert Worksheet to MHTML file using Aspose.Cells for Java in Python, simply invoke worksheet_to_mhtml() method of Converter module.

**Python Code**

{{< highlight java >}}

 saveFormat = self.SaveFormat

#Specify the file path

filePath = self.dataDir + "Book1.xlsx"

#Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

#Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

#Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Download Running Code**
Download **Converting To MHTML (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
