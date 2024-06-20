---
title: Convertir Hoja de Cálculo a Imagen en Python
type: docs
weight: 40
url: /es/java/converting-worksheet-to-image-in-python/
---

## **Aspose.Cells - Convertir hoja de trabajo a imagen**
Para convertir una hoja de trabajo a imagen usando Aspose.Cells for Java en Ruby, simplemente invoque el módulo Converter.

**Código Python**

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
## **Descargar Código en Ejecución**
Descargar **Hoja de Cálculo a Imagen (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
