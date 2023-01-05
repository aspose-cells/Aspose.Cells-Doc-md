---
title: Ruby'de Çalışma Sayfasını Gizle veya Göster
type: docs
weight: 60
url: /tr/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells - Bir Çalışma Sayfasını Gizle veya Göster**
### **Bir Çalışma Sayfasını Gizleme**
 Ruby için Aspose.Cells Java kullanarak çalışma sayfasını gizlemek için arayın**çalışma sayfasını gizle** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
### **Çalışma Sayfası Gösterme**
Geliştiriciler, ayarlayarak bir çalışma sayfasını görünür yapabilir.*setVisible(* *doğru* *)*yöntemi**Çalışma kağıdı**sınıf.

**Yakut Kodu**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Bir Çalışma Sayfasını Gizle veya Göster (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
