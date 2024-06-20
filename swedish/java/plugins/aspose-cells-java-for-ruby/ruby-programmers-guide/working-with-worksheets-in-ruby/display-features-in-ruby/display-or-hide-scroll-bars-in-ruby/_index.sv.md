---
title: Visa eller dölj rullningsfält i Ruby
type: docs
weight: 30
url: /sv/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - Visa eller dölj rullningsfält**
### **Dölja bildrullningsfält**
För att dölja rullningsfält med **Aspose.Cells Java för Ruby**, anropa modulen **displayhidescrollbars**.

**Ruby-kod**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."

{{< /highlight >}}
### **Gör bildrullningsfält synliga**
Gör rullningsfält synliga genom att ställa in klassen Workbook metod setVerticalScrollBarHidden() eller setHorizontalScrollBarHidden() till true.

**Ruby-kod**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Visa eller dölj rullningsfält (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
