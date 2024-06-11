---
title: 在Python中将工作表转换为图像
type: docs
weight: 40
url: /zh/java/converting-worksheet-to-image-in-python/
---

## **Aspose.Cells - 将工作表转换为图像**
使用Ruby中的Aspose.Cells for Java将工作表转换为图像，只需调用Converter模块。

**Python 代码**

{{< highlight python >}}

 imageFormat = self.ImageFormat

#Instantiate a workbook with path to an Excel file

book = self.Workbook(self.dataDir + "Book1.xls")

#Create an object for ImageOptions

imgOptions = self.ImageOrPrintOptions()

#Set the image type

imgOptions.setImageFormat(imageFormat.getPng())

#Get the first worksheet.

sheet = book.getWorksheets().get(0)

#Create a SheetRender object for the target sheet

sr =self.SheetRender(sheet, imgOptions)

for i in range(sr.getPageCount()):

#Generate an image for the worksheet

sr.toImage(i, self.dataDir + "mysheetimg" + ".png")


\# Print message

print "Images generated successfully."

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码网站上下载**工作表到图像（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
