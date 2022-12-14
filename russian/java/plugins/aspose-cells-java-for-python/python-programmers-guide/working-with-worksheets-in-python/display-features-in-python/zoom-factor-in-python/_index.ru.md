---
title: Коэффициент масштабирования в Python
type: docs
weight: 80
url: /ru/java/zoom-factor-in-python/
---
## **Aspose.Cells - Коэффициент масштабирования**
 Чтобы установить коэффициент масштабирования с помощью**Aspose.Cells Java для Python** , просто вызовите**ZoomFactor** модуль.

**Python Код**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Коэффициент масштабирования (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
