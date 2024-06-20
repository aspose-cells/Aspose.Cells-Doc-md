---
title: Anzeigen oder Ausblenden von Zeilen und Spaltenüberschriften in Ruby
type: docs
weight: 20
url: /de/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - Anzeigen oder Ausblenden von Zeilen- und Spaltenüberschriften**
### **Zeilen-/Spaltenheader ausblenden**
Um Zeilen-/Spaltenüberschriften mithilfe von **Aspose.Cells Java für Ruby** auszublenden, rufen Sie das Modul **DisplayHideRowColumnHeaders** auf.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Anzeigen von Zeilen-/Spaltenüberschriften**
Zeigen Sie Zeilen- und Spaltenüberschriften an, indem Sie die Methode setRowColumnHeadersVisible(true) der Klasse Arbeitsblatt verwenden.

**Ruby-Code**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Display or Hide Row Column Headers (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
