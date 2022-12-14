---
title: Ruby'de Sekmeleri Görüntüleme veya Gizleme
type: docs
weight: 40
url: /tr/java/display-or-hide-tabs-in-ruby/
---
## **Aspose.Cells - Sekmeleri Görüntüle veya Gizle**
### **Sekmeleri Gizleme**
 kullanarak sekmeleri gizlemek için**Yakut için Aspose.Cells Java** , aramak**sekmeleri göster** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Sekmeleri Görünür Hale Getirmek**
Workbook sınıfının setSheetTabBarHidden(false) yöntemiyle sekmeleri görünür yapın.

**Yakut Kodu**

{{< highlight "ruby" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Sekmeleri Gizle veya Görüntüle veya Gizle (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
