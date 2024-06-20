---
title: Ruby de Bir Çalışsayı Gizle veya Göster
type: docs
weight: 60
url: /tr/java/hide-or-unhide-a-worksheet-in-ruby/
---

## **Aspose.Cells - Bir Çalışsayı Gizle veya Göster**
### **Bir Çalışsayıyı Gizleme**
Aspose.Cells Java for Ruby kullanarak çalışsayıyı gizlemek için **hideunhideworksheet** modülünü çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Bir Çalışsayıyı Gösterme**
Geliştiriciler, **Worksheet** sınıfının *setVisible(true)* metodunu kullanarak bir çalışsayıyı görünür yapabilirler.

**Ruby Kodu**

{{< highlight ruby >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Aspose.Cells** ile Bir Çalışsayıyı Gizle veya Göster'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
