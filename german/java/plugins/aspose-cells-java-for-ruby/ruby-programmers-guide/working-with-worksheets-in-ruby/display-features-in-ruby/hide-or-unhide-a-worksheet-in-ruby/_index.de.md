---
title: Arbeitsblatt in Ruby ausblenden oder wieder einblenden
type: docs
weight: 60
url: /de/java/hide-or-unhide-a-worksheet-in-ruby/
---

## **Aspose.Cells - Arbeitsblatt ausblenden oder einblenden**
### **Arbeitsblatt ausblenden**
Um ein Arbeitsblatt mit Aspose.Cells Java für Ruby auszublenden, rufen Sie das Modul **hideunhideworksheet** auf.

**Ruby-Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Ein Arbeitsblatt anzeigen**
Entwickler können ein Arbeitsblatt sichtbar machen, indem sie die Methode *setVisible(* *true* *)* der Klasse **Worksheet** setzen.

**Ruby-Code**

{{< highlight ruby >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Download von **Arbeitsblatt ausblenden oder einblenden (Aspose.Cells)** von einer der unten genannten sozialen Coding-Seiten:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
