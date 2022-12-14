---
title: 在 Ruby 中将 Excel 文件转换为 PDF 文件
type: docs
weight: 30
url: /zh/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - 将 Excel 转换为 PDF 文件**
要在 Ruby 中使用 Aspose.Cells for Java 将 Excel 转换为 Pdf 文件，只需调用 excel_至_Converter 模块的 pdf() 方法。

**红宝石代码**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **下载运行代码**
下载**将 Excel 转换为 PDF 文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
