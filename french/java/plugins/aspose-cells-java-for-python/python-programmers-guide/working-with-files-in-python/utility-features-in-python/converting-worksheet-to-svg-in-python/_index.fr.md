---
title: Conversion de feuille de calcul en SVG en Python
type: docs
weight: 50
url: /fr/java/converting-worksheet-to-svg-in-python/
---

## **Aspose.Cells - Conversion de feuille de calcul en SVG**
Pour convertir une feuille de calcul en SVG en utilisant Aspose.Cells for Java en Python, il suffit d'invoquer la méthode worksheet_to_svg() du module Convertisseur.

**Code Python**

{{< highlight java >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Convert each worksheet into svg format in a single page.

imgOptions = ImageOrPrintOptions()

imgOptions.setSaveFormat(saveFormat.SVG)

imgOptions.setOnePagePerSheet(True)

#Convert each worksheet into svg format

sheetCount = workbook.getWorksheets().getCount()

#for(i=0; i<sheetCount; i++)

for i in range(sheetCount):

sheet = workbook.getWorksheets().get(i)

sr = SheetRender(sheet, imgOptions)

pageCount = sr.getPageCount()

#for (k = 0 k < pageCount k++)

for k in range(pageCount):

#Output the worksheet into Svg image format

sr.toImage(k, self.dataDir + sheet.getName() + ".out.svg")



\# Print message

print "Excel to SVG conversion completed successfully."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Conversion de feuille de calcul en SVG(Aspose.Cells)** à partir d'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
