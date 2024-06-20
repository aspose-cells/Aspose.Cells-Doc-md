---
title: Ein Arbeitsblatt in Python entschützen
type: docs
weight: 20
url: /de/java/unprotect-a-worksheet-in-python/
---

## **Aspose.Cells - Ein Arbeitsblatt entschützen**
Um ein Arbeitsblatt mit **Aspose.Cells Java for Python** zu schützen, rufen Sie die Methode **unprotect_worksheet** des Moduls **protection** auf.

**Python-Code**

{{< highlight java >}}

 filesFormatType = self.FileFormatType

#Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

#The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

#Unprotecting the worksheet

worksheet.unprotect()

\# Save the excel file.

workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

#Print Message

print "Worksheet unprotected successfully."

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Ein Arbeitsblatt entschützen (Aspose.Cells)** von einer der unten genannten sozialen Code-Seiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
