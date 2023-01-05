---
title: Ruby'de Kılavuz Çizgilerini Görüntüleme veya Gizleme
type: docs
weight: 10
url: /tr/java/display-or-hide-gridlines-in-ruby/
---
## **Aspose.Cells - Kılavuz Çizgilerini Görüntüle veya Gizle**
### **Kılavuz Çizgilerini Gizleme**
 kullanarak çalışma sayfasını gizlemek için**Yakut için Aspose.Cells Java** , Arama**displayhidegridlines** modül.

**Yakut Kodu**

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
### **Kılavuz Çizgilerini Görünür Hale Getirme**
Kılavuz çizgilerini görünür yapmak için Worksheet sınıfının setGridlinesVisible(true) yöntemini kullanın.

**Yakut Kodu**

{{< highlight "ruby" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Kılavuz Çizgilerini Görüntüle veya Gizle (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
