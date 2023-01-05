---
title: Преобразование файлов HTML в электронные таблицы Excel в Ruby
type: docs
weight: 40
url: /ru/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---
## **Aspose.Cells - Преобразование файлов HTML в электронные таблицы Excel**
Чтобы преобразовать HTML в электронную таблицу, используя Aspose.Cells for Java в Ruby, просто вызовите html_к_метод excel() модуля Converter.

**Рубиновый код**

{{< highlight "ruby" >}}

 def html_to_excel()

    load_format = Rjb::import('com.aspose.cells.LoadFormat')

    # Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat

    options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)



    # Load the Html file through file path while passing the instance of HTMLLoadOptions class

    workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)



    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    #Save the results to disc in Xlsx format

    workbook.save(@data_dir + "output.xlsx", save_format.XLSX)

    puts "XLSX saved successfully."

end

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Преобразование файлов HTML в электронные таблицы Excel (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
