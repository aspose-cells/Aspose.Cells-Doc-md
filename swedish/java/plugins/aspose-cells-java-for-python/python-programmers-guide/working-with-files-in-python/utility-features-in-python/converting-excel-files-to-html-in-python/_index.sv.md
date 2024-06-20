---
title: Konvertera Excel filer till HTML i Python
type: docs
weight: 10
url: /sv/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - Konvertera Excel-fil till HTML**
För att konvertera Excel till HTML med Aspose.Cells for Java i Python, helt enkelt anropa worksheet_to_html() metoden för Converter modulen.

**Python-kod**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Konvertera Excel-fil till HTML (Aspose.Cells)** från någon av nedan angivna sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
