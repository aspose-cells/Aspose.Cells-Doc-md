---
title: 在Python中将Excel转换为PDF文件
type: docs
weight: 20
url: /zh/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - 将Excel转换为Pdf**
使用Python中的Aspose.Cells for Java将Excel转换为PDF文件，只需调用Converter模块的excel_to_pdf()方法。

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
从以下任一社交编码网站下载**将Excel转换为Pdf（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
