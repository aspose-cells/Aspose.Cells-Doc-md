---
title: Преобразование файлов Excel в HTML на Ruby
type: docs
weight: 20
url: /ru/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - Преобразование файлов Excel в HTML**
Чтобы преобразовать Excel в HTML с использованием Aspose.Cells for Java на Ruby, просто вызовите метод worksheet_to_html() модуля Converter.

**Код на Ruby**

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
## **Скачать работающий код**
Скачать **Преобразование файлов Excel в HTML (Aspose.Cells)** с любого из перечисленных ниже социальных сайтов для программистов:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
