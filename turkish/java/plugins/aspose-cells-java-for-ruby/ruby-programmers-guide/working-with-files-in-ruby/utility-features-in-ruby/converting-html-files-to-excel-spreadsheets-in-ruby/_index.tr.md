---
title: Ruby de HTML dosyalarını Excel Elektronik Tablolarına Dönüştürme
type: docs
weight: 40
url: /tr/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---

## **Aspose.Cells - HTML dosyalarını Excel Elektronik Tablolarına Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak HTML'i Elektronik Tablo'ya dönüştürmek için, basitçe Converter modülünün html_to_excel() metodunu çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

 def html_to_excel()

    load_format = Rjb::import('com.aspose.cells.LoadFormat')

    # Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat

    options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)



    # Load the Html file through file path while passing the instance of HTMLLoadOptions class

    workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)



    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    #Save the results to disc in Xlsx format

    workbook.save(@data_dir + "output.xlsx", save_format.XLSX)

    puts "XLSX saved successfully."

end

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells ile HTML dosyalarını Excel Elektronik Tablolarına Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
