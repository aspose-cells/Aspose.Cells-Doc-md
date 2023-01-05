---
title: Excel'i Ruby'de PDF Dosyalarına Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - Excel'i PDF Dosyalarına Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Excel'i PDF dosyasına dönüştürmek için excel'i çağırmanız yeterlidir_ile_Dönüştürücü modülünün pdf() yöntemi.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Excel'i PDF Dosyalarına Dönüştürme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
