---
title: Spalten einfrieren in Python
type: docs
weight: 40
url: /de/java/freeze-panes-in-python/
---

## **Aspose.Cells - Spalten einfrieren**
Um in einem Tabellendokument mit **Aspose.Cells Java für Python** Spalten einzufrieren, rufen Sie einfach das Modul **FreezePanes** auf.

**Python-Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

#Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Hello World (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
