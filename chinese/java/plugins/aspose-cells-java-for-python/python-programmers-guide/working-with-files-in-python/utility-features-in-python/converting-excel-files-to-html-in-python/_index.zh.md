---
title: 将 Excel 文件转换为 Python 中的 HTML
type: docs
weight: 10
url: /zh/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells - 将 Excel 文件转换为 HTML**
要使用 Python 中的 Aspose.Cells for Java 将 Excel 转换为 HTML，只需调用工作表_到_Converter 模块的 html() 方法。

**Python 代码**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **下载运行代码**
下载**将 Excel 文件转换为 HTML (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
