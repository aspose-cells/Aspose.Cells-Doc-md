---
title: 将 Excel 转换为 Python 中的 PDF 文件
type: docs
weight: 20
url: /zh/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - 将 Excel 转换为 Pdf**
要使用 Python 中的 Aspose.Cells for Java 将 Excel 转换为 Pdf 文件，只需调用 excel_到_Converter 模块的 pdf() 方法。

**Python 代码**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **下载运行代码**
下载**将 Excel 转换为 Pdf (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
