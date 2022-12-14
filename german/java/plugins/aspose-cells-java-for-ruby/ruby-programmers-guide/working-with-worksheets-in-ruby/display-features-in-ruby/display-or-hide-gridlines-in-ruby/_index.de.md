---
title: Rasterlinien in Ruby ein- oder ausblenden
type: docs
weight: 10
url: /de/java/display-or-hide-gridlines-in-ruby/
---
## **Aspose.Cells – Rasterlinien anzeigen oder ausblenden**
### **Ausblenden von Gitternetzlinien**
 Arbeitsblatt ausblenden mit**Aspose.Cells Java für Rubin** , Anruf**Rasterlinien ausblenden** Modul.

**Ruby-Code**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the gridlines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Gridlines are now hidden, please check the output file."

{{< /highlight >}}
### **Rasterlinien sichtbar machen**
Um Rasterlinien sichtbar zu machen, verwenden Sie die setGridlinesVisible(true)-Methode der Worksheet-Klasse.

**Ruby-Code**

{{< highlight "ruby" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Rasterlinien ein- oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
