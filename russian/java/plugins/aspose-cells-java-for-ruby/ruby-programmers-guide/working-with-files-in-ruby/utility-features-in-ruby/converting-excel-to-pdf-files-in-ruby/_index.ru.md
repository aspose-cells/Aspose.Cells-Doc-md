---
title: Преобразование файлов Excel в PDF в Ruby
type: docs
weight: 30
url: /ru/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - Преобразование файлов Excel в PDF**
Чтобы преобразовать файл Excel в файл Pdf, используя Aspose.Cells for Java в Ruby, просто вызовите excel_к_pdf() модуля Converter.

**Рубиновый код**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Преобразование Excel в файлы PDF (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
