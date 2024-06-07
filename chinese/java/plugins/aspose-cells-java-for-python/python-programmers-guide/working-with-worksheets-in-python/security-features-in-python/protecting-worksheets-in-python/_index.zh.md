---
title: 在Python中保护工作表
type: docs
weight: 10
url: /zh/java/protecting-worksheets-in-python/
---

## **Aspose.Cells - 保护工作表**
要使用**Aspose.Cells Java for Python**保护工作表，请调用**protection**模块的**protect_worksheet**方法。

**Python 代码**

{{< highlight java >}}

 #Instantiating a Excel object by excel file path

excel = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = excel.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

#The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

#Protects the first worksheet with a password "1234"

protection.setPassword("1234")

#Saving the modified Excel file in default format

excel.save(self.dataDir + "output.xls")

#Print Message

print "Sheet protected successfully."

{{< /highlight >}}
## **下载运行代码**
从以下任一社交编码站点下载**保护工作表（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
