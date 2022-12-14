---
title: Konvertera Excel till PDF-filer i Python
type: docs
weight: 20
url: /sv/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - Konvertera Excel till Pdf**
För att konvertera Excel till Pdf-fil med Aspose.Cells för Java i Python, anropa helt enkelt excel_till_pdf()-metoden för konverteringsmodulen.

**Python-kod**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Konvertera Excel till Pdf (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
