---
title: Ruby de Excel Dosyalarını HTML e Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - Excel Dosyalarını HTML'e Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Excel'i HTML'e dönüştürmek için, basitçe Converter modülünün worksheet_to_html() metodunu çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells ile Excel Dosyalarını HTML'e Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
