---
title: Ruby  ile Sekmeleri Göster veya Gizle
type: docs
weight: 40
url: /tr/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - Sekmeleri Göster veya Gizle**
### **Sekmeleri Gizleme**
Aspose.Cells Java for Ruby ile sekmeleri gizlemek için **displayhidetabs** modülünü çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Sekmeleri Görünür Yapma**
workbook sınıfının setSheetTabBarHidden(false) metodunu kullanarak sekmeleri görünür yapın.

**Ruby Kodu**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Aspose.Cells** ile Sekmeleri Gizle veya Göster'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
