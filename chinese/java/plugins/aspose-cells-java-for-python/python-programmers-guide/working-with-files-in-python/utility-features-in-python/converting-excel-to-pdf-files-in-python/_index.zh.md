---
title: 在Python中将Excel转换为PDF文件
type: docs
weight: 20
url: /zh/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - 将Excel转换为Pdf**
要使用Aspose.Cells for Java在Python中将Excel转换为Pdf文件，只需调用Converter模块的excel_to_pdf()方法。

**Python 代码**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **下载运行代码**
从以下提到的社交编码网站之一下载**将Excel转换为Pdf(Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
