---
title: تحويل ورق العمل إلى صورة في Python
type: docs
weight: 40
url: /ar/java/converting-worksheet-to-image-in-python/
---

## **Aspose.Cells - تحويل ورقة العمل إلى صورة**
لتحويل ورقة العمل إلى صورة باستخدام Aspose.Cells for Java في Ruby، قم ببساطة باستدعاء وحدة Converter.

**كود Python**

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
## **تحميل رمز التشغيل**
تحميل **ورقة العمل إلى صورة (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
