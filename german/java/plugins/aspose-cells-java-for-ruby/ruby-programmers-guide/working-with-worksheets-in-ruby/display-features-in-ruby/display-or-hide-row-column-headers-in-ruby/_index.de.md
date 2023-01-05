---
title: Zeilen-Spalten-Überschriften in Ruby anzeigen oder ausblenden
type: docs
weight: 20
url: /de/java/display-or-hide-row-column-headers-in-ruby/
---
## **Aspose.Cells – Zeilen-Spalten-Überschriften anzeigen oder ausblenden**
### **Zeilen-/Spaltenüberschriften ausblenden**
 Zeilen-/Spaltenüberschriften ausblenden mit**Aspose.Cells Java für Rubin** , Anruf**DisplayHideRowColumnHeader** Modul.

**Ruby-Code**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the headers of rows and columns

worksheet.setRowColumnHeadersVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Headers of rows and columns are now hidden, please check the output file."

{{< /highlight >}}
### **Zeilen-/Spaltenüberschriften sichtbar machen**
Machen Sie Zeilen- und Spaltenüberschriften sichtbar, indem Sie die setRowColumnHeadersVisible(true)-Methode der Worksheet-Klasse verwenden.

**Ruby-Code**

{{< highlight "ruby" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Zeilen-Spalten-Überschriften anzeigen oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
