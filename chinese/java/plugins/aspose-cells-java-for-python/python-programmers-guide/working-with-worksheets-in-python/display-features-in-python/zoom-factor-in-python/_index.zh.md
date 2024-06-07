---
title: 在 Python 中设置缩放系数
type: docs
weight: 80
url: /zh/java/zoom-factor-in-python/
---

## **Aspose.Cells - 缩放因子**
要在 Python 中设置缩放系数，只需调用 **ZoomFactor** 模块。

**Python 代码**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **下载运行代码**
从下面任何社交编码网站下载 **Zoom Factor (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
