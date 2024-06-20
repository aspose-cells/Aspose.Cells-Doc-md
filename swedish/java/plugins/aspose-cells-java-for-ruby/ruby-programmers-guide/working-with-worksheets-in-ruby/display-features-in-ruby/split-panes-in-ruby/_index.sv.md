---
title: Dela rutor i Ruby
type: docs
weight: 80
url: /sv/java/split-panes-in-ruby/
---

## **Aspose.Cells - Dela fönster**
För att dela rutor med **Aspose.Cells Java för Ruby**, helt enkelt använd **SplitPanes**-modulen.

**Ruby-kod**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20")

\# Split the worksheet window

workbook.getWorksheets().get(0).split()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "SplitPanes output.xls")

puts "Panes split successfully."

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Delade rutor (Aspose.Cells)** från någon av nedan nämnda sociala kodbaser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)
