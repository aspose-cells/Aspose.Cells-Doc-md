---
title: Konvertera Excel till PDF filer i Python
type: docs
weight: 20
url: /sv/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Konvertera Excel till Pdf**
För att konvertera Excel till Pdf-fil med Aspose.Cells for Java i Python, helt enkelt anropa excel_to_pdf() metoden för Converter modulen.

**Python-kod**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Konvertera Excel till Pdf (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
