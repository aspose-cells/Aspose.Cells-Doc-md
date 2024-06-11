---
title: 在Python中转换为MHTML文件
type: docs
weight: 30
url: /zh/java/converting-to-mhtml-files-in-python/
---

## **Aspose.Cells - 转换为MHTML**
使用Python中的Aspose.Cells for Java将工作表转换为MHTML文件，只需调用Converter模块的worksheet_to_mhtml()方法。

**Python 代码**

{{< highlight java >}}

 saveFormat = self.SaveFormat

#Specify the file path

filePath = self.dataDir + "Book1.xlsx"

#Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

#Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

#Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码网站上下载**转换为MHTML（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
