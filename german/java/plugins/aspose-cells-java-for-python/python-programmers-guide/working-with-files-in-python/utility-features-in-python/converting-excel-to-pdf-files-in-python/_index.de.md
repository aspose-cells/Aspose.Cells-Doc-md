---
title: Konvertieren von Excel in PDF-Dateien in Python
type: docs
weight: 20
url: /de/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - Konvertieren von Excel in PDF**
Um Excel mit Aspose.Cells for Java in Python in eine PDF-Datei zu konvertieren, rufen Sie einfach Excel auf_zu_pdf()-Methode des Converter-Moduls.

**Python Code**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Konvertieren von Excel in PDF (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
