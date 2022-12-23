---
title: 在 Ruby 中转换为 MHTML 文件
type: docs
weight: 50
url: /zh/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - 转换为 MHTML 文件**
要在 Ruby 中使用 Aspose.Cells for Java 将工作表转换为 MHTML 文件，只需调用工作表_到_Converter 模块的 mhtml() 方法。

**红宝石代码**

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
## **下载运行代码**
下载**转换为 MHTML 文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
