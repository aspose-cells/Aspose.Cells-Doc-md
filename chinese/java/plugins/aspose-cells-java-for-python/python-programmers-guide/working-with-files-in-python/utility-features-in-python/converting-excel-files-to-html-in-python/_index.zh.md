---
title: 在Python中将Excel文件转换为HTML
type: docs
weight: 10
url: /zh/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - 将Excel文件转换为HTML**
要使用Aspose.Cells for Java在Python中将Excel转换为HTML，只需调用Converter模块的worksheet_to_html()方法。

**Python 代码**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **下载运行代码**
从以下提到的社交编码网站之一下载**将Excel文件转换为HTML(Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
