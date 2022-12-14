---
title: Verwalten von Seitenumbrüchen in Python
type: docs
weight: 20
url: /de/java/managing-page-breaks-in-python/
---
## **Aspose.Cells – Verwalten von Seitenumbrüchen**
### **Seitenumbrüche hinzufügen**
 So fügen Sie Seitenumbrüche hinzu mit**Aspose.Cells Java für Rubin** , Anruf**add_page_breaks** Methode von**Seitenumbrüche** Modul. Unten sehen Sie ein Codebeispiel.

**Python Code**

{{< highlight "python" >}}

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
### **Löschen aller Seitenumbrüche**
 Um alle Seitenumbrüche zu löschen, verwenden Sie**Aspose.Cells Java für Python** , Anruf**clear_all_page_breaks** Methode von**Seitenumbrüche** Modul. Unten sehen Sie ein Codebeispiel.

**Python Code**

{{< highlight "python" >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Entfernen eines bestimmten Seitenumbruchs**
 So entfernen Sie einen bestimmten Seitenumbruch mit**Aspose.Cells Java für Python** , Anruf**remove_page_break** Methode von**Seitenumbrüche** Modul. Unten sehen Sie ein Codebeispiel.

**Python Code**

{{< highlight "python" >}}



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
## **Laufcode herunterladen**
 Download**Seitenumbrüche verwalten (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
