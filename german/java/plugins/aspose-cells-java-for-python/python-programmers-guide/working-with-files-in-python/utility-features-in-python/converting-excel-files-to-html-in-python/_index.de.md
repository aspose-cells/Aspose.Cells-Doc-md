---
title: Konvertieren von Excel Dateien in HTML in Python
type: docs
weight: 10
url: /de/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - Konvertierung von Excel-Datei in HTML**
Um Excel in HTML mit Aspose.Cells for Java in Python zu konvertieren, rufen Sie einfach die Methode worksheet_to_html() des Converter-Moduls auf.

**Python-Code**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Konvertierung von Excel-Datei in HTML (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
