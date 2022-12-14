---
title: 在 Ruby 中将 Excel 文件转换为 HTML
type: docs
weight: 20
url: /zh/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - 将 Excel 文件转换为 HTML**
要在 Ruby 中使用 Aspose.Cells for Java 将 Excel 转换为 HTML，只需调用工作表_至_Converter 模块的 html() 方法。

**红宝石代码**

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
## **下载运行代码**
下载**将 Excel 文件转换为 HTML (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
