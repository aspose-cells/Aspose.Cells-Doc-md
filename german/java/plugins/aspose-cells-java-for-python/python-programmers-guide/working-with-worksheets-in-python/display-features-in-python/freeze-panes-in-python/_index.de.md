---
title: Fenster einfrieren in Python
type: docs
weight: 40
url: /de/java/freeze-panes-in-python/
---
## **Aspose.Cells - Fenster einfrieren**
 So frieren Sie Fenster im Tabellenkalkulationsdokument ein**Aspose.Cells Java for Python** , einfach aufrufen**FreezePanes** Modul.

**Python Code**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

# Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Hello World (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
