---
title: Konvertierung von Excel in PDF Dateien in Python
type: docs
weight: 20
url: /de/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Konvertierung von Excel in PDF**
Um Excel in PDF-Datei mit Aspose.Cells for Java in Python zu konvertieren, rufen Sie einfach die Methode excel_to_pdf() des Converter-Moduls auf.

**Python-Code**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Konvertierung von Excel in PDF (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
