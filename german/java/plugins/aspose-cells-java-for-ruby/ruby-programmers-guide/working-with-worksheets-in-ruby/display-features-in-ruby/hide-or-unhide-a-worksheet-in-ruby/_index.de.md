---
title: Ausblenden oder Einblenden eines Arbeitsblatts in Ruby
type: docs
weight: 60
url: /de/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells – Ausblenden oder Einblenden eines Arbeitsblatts**
### **Ausblenden eines Arbeitsblatts**
 Um das Arbeitsblatt mit Aspose.Cells Java für Ruby auszublenden, rufen Sie an**verbergenarbeitsblatt einblenden** Modul.

**Ruby-Code**

{{< highlight "ruby" >}}

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
### **Anzeigen eines Arbeitsblatts**
Entwickler können ein Arbeitsblatt sichtbar machen, indem sie das festlegen*setVisible(* *Stimmt* *)*Methode der**Arbeitsblatt**Klasse.

**Ruby-Code**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Ein Arbeitsblatt ein- oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
