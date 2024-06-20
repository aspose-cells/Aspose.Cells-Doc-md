---
title: Ruby de MHTML Dosyalarına Dönüştürme
type: docs
weight: 50
url: /tr/java/converting-to-mhtml-files-in-ruby/
---

## **Aspose.Cells - MHTML Dosyalarına Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Çalışma Sayfasını MHTML dosyasına dönüştürmek için, basitçe Converter modülünün worksheet_to_mhtml() metodunu çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

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
**Aspose.Cells ile MHTML Dosyalarına Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
