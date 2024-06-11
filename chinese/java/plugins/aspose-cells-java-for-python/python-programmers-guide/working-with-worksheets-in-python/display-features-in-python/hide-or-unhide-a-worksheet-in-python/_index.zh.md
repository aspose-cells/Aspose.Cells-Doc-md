---
title: 在Python中隐藏或取消隐藏工作表
type: docs
weight: 50
url: /zh/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - 隐藏或取消隐藏工作表**
### **隐藏工作表**
通过Aspose.Cells Java for Ruby使用**hideunhideworksheet**模块来隐藏工作表。

**Python 代码**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **显示工作表**
开发者可以通过设置**Worksheet**类的*setVisible(* *true* *)*方法来使工作表可见。

**Python 代码**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**隐藏或取消隐藏工作表 (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
