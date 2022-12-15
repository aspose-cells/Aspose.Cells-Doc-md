---
title: Ruby'de Satır Sütun Başlıklarını Görüntüleme veya Gizleme
type: docs
weight: 20
url: /tr/java/display-or-hide-row-column-headers-in-ruby/
---
## **Aspose.Cells - Satır Sütun Başlıklarını Görüntüle veya Gizle**
### **Satır/Sütun Başlıklarını Gizleme**
kullanarak satır/sütun başlıklarını gizlemek için**Yakut için Aspose.Cells Java** , aramak**DisplayHideRowColumnHeaders** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the headers of rows and columns

worksheet.setRowColumnHeadersVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Headers of rows and columns are now hidden, please check the output file."

{{< /highlight >}}
### **Satır/Sütun Başlıklarını Görünür Hale Getirme**
Worksheet sınıfının setRowColumnHeadersVisible(true) yöntemini kullanarak satır ve sütun başlıklarını görünür yapın.

**Yakut Kodu**

{{< highlight "ruby" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Satır Sütun Başlıklarını Görüntüle veya Gizle (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
