---
title: Ruby de Excel Dosyalarını PDF e Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - Excel Dosyalarını PDF'e Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Excel'i Pdf dosyasına dönüştürmek için, basitçe Converter modülünün excel_to_pdf() metodunu çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells ile Excel'den PDF Dosyalarına Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
