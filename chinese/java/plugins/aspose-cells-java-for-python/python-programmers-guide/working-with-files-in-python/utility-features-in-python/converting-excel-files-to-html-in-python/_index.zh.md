---
title: 在Python中将Excel文件转换为HTML
type: docs
weight: 10
url: /zh/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - 将Excel文件转换为HTML**
使用Python中的Aspose.Cells for Java将Excel转换为HTML，只需调用Converter模块的worksheet_to_html()方法。

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
从以下任一社交编码网站下载**将Excel文件转换为HTML（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
