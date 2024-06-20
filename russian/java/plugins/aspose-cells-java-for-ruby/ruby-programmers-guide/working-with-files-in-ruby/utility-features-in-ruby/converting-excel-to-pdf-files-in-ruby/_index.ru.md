---
title: Преобразование Excel в PDF файлы на Ruby
type: docs
weight: 30
url: /ru/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - Преобразование Excel в PDF-файлы**
Чтобы преобразовать Excel в Pdf-файл с использованием Aspose.Cells for Java на Ruby, просто вызовите метод excel_to_pdf() модуля Converter.

**Код на Ruby**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Преобразование Excel в PDF-файлы (Aspose.Cells)** с любого из перечисленных ниже социальных сайтов для программистов:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
