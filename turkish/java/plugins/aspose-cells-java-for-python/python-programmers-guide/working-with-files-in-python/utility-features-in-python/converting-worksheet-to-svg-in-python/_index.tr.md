﻿---
title: Çalışma Sayfasını Python'de SVG'e Dönüştürme
type: docs
weight: 50
url: /tr/java/converting-worksheet-to-svg-in-python/
---
## **Aspose.Cells - Çalışma Sayfası SVG'e dönüştürülüyor**
Python'de Aspose.Cells for Java'i kullanarak Çalışma Sayfasını SVG'e dönüştürmek için çalışma sayfasını çağırmanız yeterlidir_ile_Dönüştürücü modülünün svg() yöntemi.

**Python Kod**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Convert each worksheet into svg format in a single page.

imgOptions = ImageOrPrintOptions()

imgOptions.setSaveFormat(saveFormat.SVG)

imgOptions.setOnePagePerSheet(True)

# Convert each worksheet into svg format

sheetCount = workbook.getWorksheets().getCount()

# for(i=0; i<sheetCount; i++)

for i in range(sheetCount):

sheet = workbook.getWorksheets().get(i)

sr = SheetRender(sheet, imgOptions)

pageCount = sr.getPageCount()

# for (k = 0 k < pageCount k++)

for k in range(pageCount):

# Output the worksheet into Svg image format

sr.toImage(k, self.dataDir + sheet.getName() + ".out.svg")



\# Print message

print "Excel to SVG conversion completed successfully."

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Çalışma Sayfası SVG(Aspose.Cells)'e Dönüştürülüyor** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
