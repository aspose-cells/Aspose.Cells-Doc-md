---
title: 在 Python 中冻结窗格
type: docs
weight: 40
url: /zh/java/freeze-panes-in-python/
---

## **Aspose.Cells - 冻结窗格**
要在电子表格文档中使用 **Aspose.Cells Java for Python** 冻结窗格，只需调用 **FreezePanes** 模块。

**Python 代码**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

#Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**Hello World（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
