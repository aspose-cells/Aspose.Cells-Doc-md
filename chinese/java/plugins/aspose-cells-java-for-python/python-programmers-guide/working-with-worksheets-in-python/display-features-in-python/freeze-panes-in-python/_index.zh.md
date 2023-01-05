---
title: Python 中的冻结窗格
type: docs
weight: 40
url: /zh/java/freeze-panes-in-python/
---
## **Aspose.Cells - 冻结窗格**
要冻结电子表格文档中的窗格，请使用**Aspose.Cells Java for Python** 只需调用**冻结窗格**模块。

**Python 代码**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

# Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **下载运行代码**
下载**Hello World (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
