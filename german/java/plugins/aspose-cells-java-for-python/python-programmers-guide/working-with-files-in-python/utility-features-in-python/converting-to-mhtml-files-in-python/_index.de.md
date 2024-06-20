---
title: Konvertierung in MHTML Dateien in Python
type: docs
weight: 30
url: /de/java/converting-to-mhtml-files-in-python/
---

## **Aspose.Cells - Konvertierung in MHTML**
Um Arbeitsblatt in MHTML-Datei mit Aspose.Cells for Java in Python zu konvertieren, rufen Sie einfach die Methode worksheet_to_mhtml() des Converter-Moduls auf.

**Python-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Konvertierung in MHTML (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
