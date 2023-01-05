---
title: Visa eller dölj rutnät i rubin
type: docs
weight: 10
url: /sv/java/display-or-hide-gridlines-in-ruby/
---
## **Aspose.Cells - Visa eller dölj rutnätslinjer**
### **Dölja rutnät**
 För att dölja kalkylblad med**Aspose.Cells Java för Ruby** , ringa upp**visahidegridlines** modul.

**Ruby kod**

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
### **Gör rutnät synliga**
För att göra rutnätslinjer synliga, använd arbetsbladsklassens setGridlinesVisible(true) metod.

**Ruby kod**

{{< highlight "ruby" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Visa eller dölj rutnät (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
