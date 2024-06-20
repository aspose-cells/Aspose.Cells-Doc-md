---
title: Visa eller dölj rutnät i Ruby
type: docs
weight: 10
url: /sv/java/display-or-hide-gridlines-in-ruby/
---

## **Aspose.Cells - Visa eller dölj rutnät**
### **Gömmer rutnätslinjer**
För att dölja kalkylblad med **Aspose.Cells Java för Ruby**, anropa **displayhidegridlines** modulen.

**Ruby-kod**

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
### **Gör rutnätslinjer synliga**
För att göra rutnätet synligt, använd klassen Worksheet metod setGridlinesVisible(true).

**Ruby-kod**

{{< highlight ruby >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Visa eller Dölj rutnät (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
