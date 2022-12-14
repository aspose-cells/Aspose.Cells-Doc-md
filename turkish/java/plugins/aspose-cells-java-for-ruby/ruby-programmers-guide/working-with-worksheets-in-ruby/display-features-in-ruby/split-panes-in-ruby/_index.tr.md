---
title: Ruby'de Bölme Bölmeleri
type: docs
weight: 80
url: /tr/java/split-panes-in-ruby/
---
## **Aspose.Cells - Bölmeli Bölmeler**
 Kullanarak Bölmeleri Bölmek için**Yakut için Aspose.Cells Java** , sadece çağırmak**Bölünmüş Paneller** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
İndirmek**Bölünmüş Bölmeler (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)
