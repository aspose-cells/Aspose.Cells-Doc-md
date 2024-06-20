---
title: Anzeigen oder Ausblenden von Gitterlinien in Ruby
type: docs
weight: 10
url: /de/java/display-or-hide-gridlines-in-ruby/
---

## **Aspose.Cells - Rasterspalten anzeigen oder ausblenden**
### **Rasterspalten ausblenden**
Um ein Arbeitsblatt mit **Aspose.Cells Java für Ruby** auszublenden, rufen Sie das Modul **displayhidegridlines** auf.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Anzeigen von Rasterlinien**
Um Gitterlinien sichtbar zu machen, verwenden Sie die Methode setGridlinesVisible(true) der Klasse Worksheet.

**Ruby-Code**

{{< highlight ruby >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Anzeigen oder Ausblenden von Gitternetzlinien (Aspose.Cells)** von einer der unten aufgeführten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
