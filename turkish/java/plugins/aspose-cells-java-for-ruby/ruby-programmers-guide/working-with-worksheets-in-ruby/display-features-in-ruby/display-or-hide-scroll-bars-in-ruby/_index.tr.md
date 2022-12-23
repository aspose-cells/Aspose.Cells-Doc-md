---
title: Ruby'de Kaydırma Çubuklarını Görüntüleme veya Gizleme
type: docs
weight: 30
url: /tr/java/display-or-hide-scroll-bars-in-ruby/
---
## **Aspose.Cells - Kaydırma Çubuklarını Görüntüle veya Gizle**
### **Kaydırma Çubuklarını Gizleme**
 kullanarak Kaydırma Çubuklarını gizlemek için**Yakut için Aspose.Cells Java** , Arama**kaydırma çubuklarını görüntüle** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
### **Kaydırma Çubuklarını Görünür Hale Getirmek**
Workbook sınıfının setVerticalScrollBarHidden() veya setHorizontalScrollBarHidden() yöntemlerini true olarak ayarlayarak kaydırma çubuklarını görünür yapın.

**Yakut Kodu**

{{< highlight "ruby" >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Kaydırma Çubuklarını Görüntüle veya Gizle (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
