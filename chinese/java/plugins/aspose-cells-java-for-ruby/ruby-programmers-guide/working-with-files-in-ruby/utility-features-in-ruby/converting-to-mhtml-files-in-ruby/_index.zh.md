---
title: 在Ruby中将文件转换为MHTML文件
type: docs
weight: 50
url: /zh/java/converting-to-mhtml-files-in-ruby/
---

## **Aspose.Cells - 将文件转换为MHTML文件**
使用Ruby中的Aspose.Cells for Java将工作表转换为MHTML文件，只需调用Converter模块的worksheet_to_mhtml()方法。

**Ruby 代码**

{{< highlight ruby >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**将文件转换为MHTML文件（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
