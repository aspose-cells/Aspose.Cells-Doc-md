---
title: Arbeitsblatt in Bild umwandeln in Python
type: docs
weight: 40
url: /de/java/converting-worksheet-to-image-in-python/
---
## **Aspose.Cells – Arbeitsblatt in Bild konvertieren**
Um Worksheet in Image mit Aspose.Cells for Java in Ruby zu konvertieren, rufen Sie einfach das Converter-Modul auf.

**Python Code**

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
## **Laufcode herunterladen**
 Download**Arbeitsblatt zu Bild (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
