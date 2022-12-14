---
title: 在 Python 中保存文件
type: docs
weight: 20
url: /zh/java/saving-files-in-python/
---
## **Aspose.Cells - 保存文件**
### **将文件保存到某个位置**
如果开发人员需要使用**Aspose.Cells Java 为 Python**到某个存储位置，然后他们可以简单地指定文件名（及其完整的存储路径）和所需的文件格式（使用**文件格式类型**枚举），同时调用**节省**的方法**工作簿**目的。

**Python 代码**

{{< highlight "python" >}}

 fileFormatType = self.FileFormatType


# Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

# Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

# Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

# Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

# Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

下载**保存文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
