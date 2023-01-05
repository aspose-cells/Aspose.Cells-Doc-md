---
title: Konvertieren in MHTML-Dateien in Python
type: docs
weight: 30
url: /de/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells - Umwandlung in MHTML**
Um Worksheet in eine MHTML-Datei mit Aspose.Cells for Java in Python zu konvertieren, rufen Sie einfach worksheet auf_zu_mhtml()-Methode des Converter-Moduls.

**Python Code**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

# Specify the file path

filePath = self.dataDir + "Book1.xlsx"

# Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

# Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

# Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Umwandlung in MHTML (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
