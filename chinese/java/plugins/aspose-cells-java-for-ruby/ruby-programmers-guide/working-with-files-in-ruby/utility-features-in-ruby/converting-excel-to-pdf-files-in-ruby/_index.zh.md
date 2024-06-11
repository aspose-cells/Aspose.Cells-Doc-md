---
title: 在Ruby中将Excel转换为PDF文件
type: docs
weight: 30
url: /zh/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - 将Excel转换为PDF文件**
使用Ruby中的Aspose.Cells for Java将Excel转换为PDF文件，只需调用Converter模块的excel_to_pdf()方法。

**Ruby 代码**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**将Excel转换为PDF文件（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
