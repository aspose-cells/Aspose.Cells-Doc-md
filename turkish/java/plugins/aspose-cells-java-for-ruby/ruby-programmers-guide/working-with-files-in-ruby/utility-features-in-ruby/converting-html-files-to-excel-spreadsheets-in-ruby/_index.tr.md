---
title: HTML dosyalarını Ruby'de Excel Elektronik Tablolarına dönüştürme
type: docs
weight: 40
url: /tr/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---
## **Aspose.Cells - HTML dosyalarını Excel Elektronik Tablolarına dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak HTML'yi Elektronik Tabloya dönüştürmek için html'yi çağırmanız yeterlidir_ile_Dönüştürücü modülünün excel() yöntemi.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
İndirmek**HTML dosyalarını Excel Elektronik Tablolarına dönüştürme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
