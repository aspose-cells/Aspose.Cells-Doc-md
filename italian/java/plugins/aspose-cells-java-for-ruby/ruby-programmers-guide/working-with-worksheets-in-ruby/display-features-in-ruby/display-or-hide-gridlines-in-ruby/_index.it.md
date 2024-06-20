---
title: Mostra o nascondi le linee della griglia in Ruby
type: docs
weight: 10
url: /it/java/display-or-hide-gridlines-in-ruby/
---

## **Aspose.Cells - Mostra o Nascondi le linee della griglia**
### **Nascondere le Linee della Griglia**
Per nascondere il foglio di lavoro usando **Aspose.Cells Java per Ruby**, chiamare il modulo **displayhidegridlines**.

**Codice Ruby**

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
### **Rendere Visibili le Linee della Griglia**
Per rendere visibili le linee della griglia, utilizzare il metodo `setGridlinesVisible(true)` della classe `Worksheet`.

**Codice Ruby**

{{< highlight ruby >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Mostra o Nascondi le linee della griglia (Aspose.Cells)** da uno dei siti di codice sociale di seguito elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
