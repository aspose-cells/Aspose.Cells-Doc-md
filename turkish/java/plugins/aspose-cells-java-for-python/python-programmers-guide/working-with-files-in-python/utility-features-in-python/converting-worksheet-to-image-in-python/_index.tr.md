---
title: Python da Çalışsayfayı Görsele Dönüştürme
type: docs
weight: 40
url: /tr/java/converting-worksheet-to-image-in-python/
---

## **Aspose.Cells - Çalışma Sayfasını Görüntüye Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Çalışma Sayfasını Görüntüye dönüştürmek için, Converter modülünü basitçe çağırın.

**Python Kodu**

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
## **Çalışan Kodu İndir**
Altta belirtilen sosyal kodlama sitelerinden herhangi birinden  **Görsele Dönüştürme (Aspose.Cells)**'ı İndir

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
