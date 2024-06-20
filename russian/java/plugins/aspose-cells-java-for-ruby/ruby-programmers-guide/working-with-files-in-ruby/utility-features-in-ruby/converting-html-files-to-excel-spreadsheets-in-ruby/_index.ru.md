---
title: Преобразование HTML файлов в электронные таблицы Excel на Ruby
type: docs
weight: 40
url: /ru/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---

## **Aspose.Cells - Преобразование HTML-файлов в электронные таблицы Excel**
Чтобы преобразовать HTML в электронную таблицу с использованием Aspose.Cells for Java на Ruby, просто вызовите метод html_to_excel() модуля Converter.

**Код на Ruby**

{{< highlight ruby >}}

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
## **Скачать работающий код**
Загрузите **Преобразование файлов HTML в электронные таблицы Excel (Aspose.Cells)** с любого из указанных ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
