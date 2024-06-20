---
title: Conversione del foglio di lavoro in un immagine in Python
type: docs
weight: 40
url: /it/java/converting-worksheet-to-image-in-python/
---

## **Aspose.Cells - Conversione di un foglio di lavoro in immagine**
Per convertire un foglio di lavoro in immagine utilizzando Aspose.Cells for Java in Ruby, basta invocare il modulo Converter.

**Codice Python**

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
## **Scarica il codice in esecuzione**
Scarica **Foglio di lavoro in Immagine (Aspose.Cells)** da uno qualsiasi dei siti di coding social qui sotto menzionati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
