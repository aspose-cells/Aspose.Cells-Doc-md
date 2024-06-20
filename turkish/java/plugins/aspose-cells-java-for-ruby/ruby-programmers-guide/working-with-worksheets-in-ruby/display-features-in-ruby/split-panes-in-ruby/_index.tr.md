---
title: Ruby de Bölünmüş Panolar
type: docs
weight: 80
url: /tr/java/split-panes-in-ruby/
---

## **Aspose.Cells - Bölünmüş Panolar**
Bölünmüş Pencereleri **Aspose.Cells Java for Ruby** kullanarak, **SplitPanes** modülünü basitçe çağırın.

**Ruby Kodu**

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
## **Çalışan Kodu İndir**
İndirin **Bölünmüş Panolar (Aspose.Cells)** any of the aşağıda bahsedilen sosyal kodlama sitelerinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)
