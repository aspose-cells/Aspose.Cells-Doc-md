---
title: Speichern von Dateien in Python
type: docs
weight: 20
url: /de/java/saving-files-in-python/
---
## **Aspose.Cells – Speichern von Dateien**
### **Datei an einem Ort speichern**
 Wenn Entwickler ihre Dateien mit speichern müssen**Aspose.Cells Java für Python** zu einem Speicherort, dann können sie einfach den Dateinamen (mit vollständigem Speicherpfad) und das gewünschte Dateiformat (mithilfe der**Dateiformattyp**Aufzählung) beim Aufrufen der**sparen**Methode von**Arbeitsmappe**Objekt.

**Python Code**

{{< highlight "python" >}}

 fileFormatType = self.FileFormatType


# Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

# Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

# Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

# Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

# Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

 Download**Datei speichern (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
