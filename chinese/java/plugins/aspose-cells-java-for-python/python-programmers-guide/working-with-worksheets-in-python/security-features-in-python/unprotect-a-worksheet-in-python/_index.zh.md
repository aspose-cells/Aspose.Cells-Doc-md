---
title: Python中取消保护工作表
type: docs
weight: 20
url: /zh/java/unprotect-a-worksheet-in-python/
---

## **Aspose.Cells - 取消保护工作表**
使用**Aspose.Cells Java for Python**调用**protection**模块的**unprotect_worksheet**方法来保护工作表。

**Python 代码**

{{< highlight java >}}

 filesFormatType = self.FileFormatType

#Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

#The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

#Unprotecting the worksheet

worksheet.unprotect()

\# Save the excel file.

workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

#Print Message

print "Worksheet unprotected successfully."

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**取消保护工作表（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
