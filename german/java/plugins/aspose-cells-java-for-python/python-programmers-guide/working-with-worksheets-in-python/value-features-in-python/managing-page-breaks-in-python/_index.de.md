---
title: Seitenumbrüche verwalten in Python
type: docs
weight: 20
url: /de/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - Seitenumbrüche verwalten**
### **Seitenumbrüche hinzufügen**
Um Seitenumbrüche mit **Aspose.Cells Java für Ruby** hinzuzufügen, rufen Sie die Methode **add_page_breaks** des Moduls **pagebreaks** auf. Im Folgenden finden Sie ein Codebeispiel.

**Python-Code**

{{< highlight python >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **Alle Seitenumbrüche löschen**
Um alle Seitenumbrüche mit **Aspose.Cells Java für Python** zu löschen, rufen Sie die Methode **clear_all_page_breaks** des Moduls **pagebreaks** auf. Im Folgenden finden Sie ein Codebeispiel.

**Python-Code**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Bestimmten Seitenumbruch entfernen**
Um einen bestimmten Seitenumbruch mit **Aspose.Cells Java für Python** zu entfernen, rufen Sie die Methode **remove_page_break** des Moduls **pagebreaks** auf. Im Folgenden finden Sie ein Codebeispiel.

**Python-Code**

{{< highlight python >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Seitenumbrüche verwalten (Aspose.Cells)** von einer der unten genannten sozialen Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
