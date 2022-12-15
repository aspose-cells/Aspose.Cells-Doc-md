---
title: Konvertera arbetsblad till bild i Python
type: docs
weight: 40
url: /sv/java/converting-worksheet-to-image-in-python/
---
## **Aspose.Cells - Konvertera arbetsblad till bild**
För att konvertera kalkylblad till bild med Aspose.Cells for Java i Ruby, anropa omvandlarmodulen.

**Python Kod**

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
## **Ladda ner Running Code**
 Ladda ner**Kalkylblad till bild (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
