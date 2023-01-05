---
title: Преобразование рабочего листа в изображение в Python
type: docs
weight: 40
url: /ru/java/converting-worksheet-to-image-in-python/
---
## **Aspose.Cells - Преобразование рабочего листа в изображение**
Чтобы преобразовать рабочий лист в изображение с помощью Aspose.Cells for Java в Ruby, просто вызовите модуль Converter.

**Python Код**

{{< highlight "python" >}}

 imageFormat = self.ImageFormat

# Instantiate a workbook with path to an Excel file

book = self.Workbook(self.dataDir + "Book1.xls")

# Create an object for ImageOptions

imgOptions = self.ImageOrPrintOptions()

# Set the image type

imgOptions.setImageFormat(imageFormat.getPng())

# Get the first worksheet.

sheet = book.getWorksheets().get(0)

# Create a SheetRender object for the target sheet

sr =self.SheetRender(sheet, imgOptions)

for i in range(sr.getPageCount()):

# Generate an image for the worksheet

sr.toImage(i, self.dataDir + "mysheetimg" + ".png")


\# Print message

print "Images generated successfully."

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Рабочий лист в изображение (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
