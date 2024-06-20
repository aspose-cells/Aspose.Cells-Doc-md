---
title: Konvertera kalkylblad till bild i Python
type: docs
weight: 40
url: /sv/java/converting-worksheet-to-image-in-python/
---

## **Aspose.Cells - Konvertering av kalkylblad till bild**
För att konvertera kalkylblad till bild med Aspose.Cells for Java i Ruby, helt enkelt anropa Converter modulen.

**Python-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Kalkylblad till bild (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
