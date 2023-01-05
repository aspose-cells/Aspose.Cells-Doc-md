---
title: Ruby'de MHTML Dosyalarına Dönüştürme
type: docs
weight: 50
url: /tr/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - MHTML Dosyalarına Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Worksheet'i MHTML dosyasına dönüştürmek için worksheet'i çağırmanız yeterlidir_ile_Dönüştürücü modülünün mhtml() yöntemi.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**MHTML Dosyalarına Dönüştürme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
