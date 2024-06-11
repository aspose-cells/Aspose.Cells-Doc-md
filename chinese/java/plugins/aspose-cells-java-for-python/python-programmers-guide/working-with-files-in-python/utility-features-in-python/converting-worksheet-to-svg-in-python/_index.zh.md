---
title: 在Python中将工作表转换为SVG
type: docs
weight: 50
url: /zh/java/converting-worksheet-to-svg-in-python/
---

## **Aspose.Cells - 将工作表转换为SVG**
使用Python中的Aspose.Cells for Java将工作表转换为SVG，只需调用Converter模块的worksheet_to_svg()方法。

**Python 代码**

{{< highlight java >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Convert each worksheet into svg format in a single page.

imgOptions = ImageOrPrintOptions()

imgOptions.setSaveFormat(saveFormat.SVG)

imgOptions.setOnePagePerSheet(True)

#Convert each worksheet into svg format

sheetCount = workbook.getWorksheets().getCount()

#for(i=0; i<sheetCount; i++)

for i in range(sheetCount):

sheet = workbook.getWorksheets().get(i)

sr = SheetRender(sheet, imgOptions)

pageCount = sr.getPageCount()

#for (k = 0 k < pageCount k++)

for k in range(pageCount):

#Output the worksheet into Svg image format

sr.toImage(k, self.dataDir + sheet.getName() + ".out.svg")



\# Print message

print "Excel to SVG conversion completed successfully."

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码网站上下载**转换工作表为SVG（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
