---
title: 在 Ruby 中将 HTML 文件转换为 Excel 电子表格
type: docs
weight: 40
url: /zh/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---
## **Aspose.Cells - 将 HTML 文件转换为 Excel 电子表格**
要在 Ruby 中使用 Aspose.Cells for Java 将 HTML 转换为电子表格，只需调用 html_至_Converter 模块的 excel() 方法。

**红宝石代码**

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
## **下载运行代码**
下载**将 HTML 文件转换为 Excel 电子表格 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
