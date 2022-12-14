---
title: Ruby'de Bölmeleri Dondur
type: docs
weight: 50
url: /tr/java/freeze-panes-in-ruby/
---
## **Aspose.Cells - Bölmeleri Dondur**
 Kullanarak Elektronik Tablo Belgesindeki Bölmeleri Dondurmak için**Yakut için Aspose.Cells Java** , sadece çağırmak**Donma bölmeleri** modül.

**Yakut Kodu**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Apply freeze panes settings, please check the output file."

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Bölmeleri Dondur (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/freezepanes.rb)
