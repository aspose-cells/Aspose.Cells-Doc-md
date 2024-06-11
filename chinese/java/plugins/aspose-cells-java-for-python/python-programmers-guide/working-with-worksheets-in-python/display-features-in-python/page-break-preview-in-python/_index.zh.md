---
title: 在Python中进行分页预览
type: docs
weight: 60
url: /zh/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
要使用**Aspose.Cells Java for Python**设置工作表为分页预览，只需调用**PageBreakPreview** 模块。

**Python 代码**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**分页预览 (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
