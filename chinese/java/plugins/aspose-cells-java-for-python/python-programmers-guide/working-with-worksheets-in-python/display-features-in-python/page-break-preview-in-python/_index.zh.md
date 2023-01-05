---
title: Python 中的分页预览
type: docs
weight: 60
url: /zh/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
将工作表设置为分页预览使用**Aspose.Cells Java for Python** 只需调用**分页预览**模块。

**Python 代码**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **下载运行代码**
下载**分页预览 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
