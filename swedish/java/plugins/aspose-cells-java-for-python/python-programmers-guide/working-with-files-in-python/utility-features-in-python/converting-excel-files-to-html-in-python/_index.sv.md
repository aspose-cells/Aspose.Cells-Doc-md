---
title: Konvertera Excel-filer till HTML i Python
type: docs
weight: 10
url: /sv/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells - Konvertera Excel-fil till HTML**
För att konvertera Excel till HTML med Aspose.Cells for Java i Python, anropa helt enkelt kalkylbladet_till_html()-metoden för konverteringsmodulen.

**Python Kod**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Konvertera Excel-fil till HTML (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
