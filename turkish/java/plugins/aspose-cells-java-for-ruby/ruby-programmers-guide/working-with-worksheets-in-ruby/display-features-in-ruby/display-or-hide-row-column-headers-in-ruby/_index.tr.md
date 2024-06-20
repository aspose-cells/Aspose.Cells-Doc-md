---
title: Ruby  ile Satır Sütun Başlıklarını Göster veya Gizle
type: docs
weight: 20
url: /tr/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - Satır Sütun Başlıklarını Göster veya Gizle**
### **Satır/Sütun Başlıklarını Gizleme**
**Aspose.Cells Java for Ruby** kullanarak satır/sütun başlıklarını gizlemek için **DisplayHideRowColumnHeaders** modülünü çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

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
### **Satır/Sütun Başlıklarını Görünür Yapma**
Satır ve sütun başlıklarını görünür yapmak için **Worksheet** sınıfının **setRowColumnHeadersVisible(true)** metodunu kullanın.

**Ruby Kodu**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells** ile **Satır Sütun Başlıklarını Göster veya Gizle**'yı aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
