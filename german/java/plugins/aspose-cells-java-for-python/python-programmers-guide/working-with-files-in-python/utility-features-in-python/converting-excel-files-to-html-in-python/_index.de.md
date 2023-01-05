---
title: Konvertieren von Excel-Dateien in HTML in Python
type: docs
weight: 10
url: /de/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells – Konvertieren einer Excel-Datei in HTML**
Um Excel mit Aspose.Cells for Java in Python in HTML zu konvertieren, rufen Sie einfach das Arbeitsblatt auf_zu_html()-Methode des Converter-Moduls.

**Python Code**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Konvertieren einer Excel-Datei in HTML (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
