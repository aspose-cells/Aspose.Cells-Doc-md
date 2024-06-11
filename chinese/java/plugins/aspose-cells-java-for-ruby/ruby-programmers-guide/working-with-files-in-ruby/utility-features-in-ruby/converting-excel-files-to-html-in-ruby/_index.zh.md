---
title: 在Ruby中将Excel文件转换为HTML
type: docs
weight: 20
url: /zh/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - 将Excel文件转换为HTML**
使用Ruby中的Aspose.Cells for Java将Excel转换为HTML，只需调用Converter模块的worksheet_to_html()方法。

**Ruby 代码**

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
## **下载运行代码**
从以下提到的任何社交编码站点下载**将Excel文件转换为HTML（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
