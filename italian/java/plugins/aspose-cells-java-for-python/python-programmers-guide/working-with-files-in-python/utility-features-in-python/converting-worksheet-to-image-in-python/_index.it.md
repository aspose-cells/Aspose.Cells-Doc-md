﻿---
title: Conversione del foglio di lavoro in immagine in Python
type: docs
weight: 40
url: /it/java/converting-worksheet-to-image-in-python/
---
## **Aspose.Cells - Conversione del foglio di lavoro in immagine**
Per convertire il foglio di lavoro in immagine utilizzando Aspose.Cells for Java in Ruby, è sufficiente richiamare il modulo Convertitore.

**Python Cod**

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
## **Scarica il codice in esecuzione**
 Scaricamento**Foglio di lavoro per immagine (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
