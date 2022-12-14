---
title: 在 Python 中转换为 MHTML 文件
type: docs
weight: 30
url: /zh/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells - 转换为 MHTML**
要使用 Python 中的 Aspose.Cells for Java 将工作表转换为 MHTML 文件，只需调用工作表_至_Converter 模块的 mhtml() 方法。

**Python 代码**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

# Specify the file path

filePath = self.dataDir + "Book1.xlsx"

# Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

# Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

# Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **下载运行代码**
下载**转换为 MHTML (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
