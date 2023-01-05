---
title: Преобразование в файлы MHTML в Ruby
type: docs
weight: 50
url: /ru/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - Преобразование в файлы MHTML**
Чтобы преобразовать рабочий лист в файл MHTML, используя Aspose.Cells for Java в Ruby, просто вызовите рабочий лист_к_Метод mhtml() модуля Converter.

**Рубиновый код**

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
## **Скачать рабочий код**
Скачать**Преобразование в файлы MHTML (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
