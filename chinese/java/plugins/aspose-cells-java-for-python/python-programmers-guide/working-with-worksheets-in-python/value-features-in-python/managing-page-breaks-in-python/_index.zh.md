---
title: 在Python中管理分页符
type: docs
weight: 20
url: /zh/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - 管理分页符**
### **添加分页**
使用**Aspose.Cells Java for Ruby**添加分页符，请调用**pagebreaks**模块的**add_page_breaks**方法。下面是代码示例。

**Python 代码**

{{< highlight python >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **清除所有分页符**
要使用**Aspose.Cells Java for Python**清除所有分页符，请调用**pagebreaks**模块的**clear_all_page_breaks**方法。下面是代码示例。

**Python 代码**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **移除特定分页符**
要使用**Aspose.Cells Java for Python**移除特定的分页符，请调用**pagebreaks**模块的**remove_page_break**方法。下面是代码示例。

**Python 代码**

{{< highlight python >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**管理分页符（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
