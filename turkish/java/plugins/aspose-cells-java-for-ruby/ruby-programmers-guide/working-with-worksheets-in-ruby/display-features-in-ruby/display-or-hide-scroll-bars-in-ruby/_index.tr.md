---
title: Ruby  ile Kaydırma Çubuklarını Göster veya Gizle
type: docs
weight: 30
url: /tr/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - Kaydırma Çubuklarını Göster veya Gizle**
### **Kaydırma çubuklarını gizleme**
**Aspose.Cells Java for Ruby** kullanarak kaydırma çubuklarını gizlemek için **displayhidescrollbars** modülünü çağırın.

**Ruby Kodu**

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
### **Kaydırma Çubuklarını Görünür Yapma**
Kaydırma çubuklarını görünür yapmak için **Workbook** sınıfının **setVerticalScrollBarHidden()** veya **setHorizontalScrollBarHidden()** metodunu kullanarak true değerini ayarlayın.

**Ruby Kodu**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells** ile **Kaydırma Çubuklarını Göster veya Gizle**'yı aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
