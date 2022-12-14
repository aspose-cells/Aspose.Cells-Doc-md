---
title: Conversion de la feuille de calcul en image dans Python
type: docs
weight: 40
url: /fr/java/converting-worksheet-to-image-in-python/
---
## **Aspose.Cells - Conversion de la feuille de calcul en image**
Pour convertir une feuille de calcul en image à l'aide de Aspose.Cells for Java dans Ruby, appelez simplement le module Converter.

**Code Python**

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
## **Télécharger le code d'exécution**
 Télécharger**Feuille de travail à l'image (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
