---
title: Excel Dosyalarını Ruby'de HTML'e Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - Excel Dosyalarını HTML'e Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Excel'i HTML'e dönüştürmek için çalışma sayfasını çağırmanız yeterlidir_ile_Dönüştürücü modülünün html() yöntemi.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
İndirmek**Excel Dosyalarını HTML'e (Aspose.Cells) Dönüştürme**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
