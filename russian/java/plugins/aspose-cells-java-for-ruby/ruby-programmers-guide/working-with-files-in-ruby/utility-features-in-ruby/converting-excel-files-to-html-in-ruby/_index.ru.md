---
title: Преобразование файлов Excel в HTML в Ruby
type: docs
weight: 20
url: /ru/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - Преобразование файлов Excel в HTML**
Чтобы преобразовать Excel в HTML, используя Aspose.Cells for Java в Ruby, просто вызовите рабочий лист_к_html() модуля Converter.

**Рубиновый код**

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
## **Скачать рабочий код**
Скачать**Преобразование файлов Excel в HTML (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
