---
title: Dividere i riquadri in Ruby
type: docs
weight: 80
url: /it/java/split-panes-in-ruby/
---

## **Aspose.Cells - Dividi riquadri**
Per dividere i riquadri usando **Aspose.Cells Java per Ruby**, basta invocare il modulo **SplitPanes**.

**Codice Ruby**

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
## **Scarica il codice in esecuzione**
Scarica **Dividere i riquadri (Aspose.Cells)** da uno qualsiasi dei siti di codici sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)
