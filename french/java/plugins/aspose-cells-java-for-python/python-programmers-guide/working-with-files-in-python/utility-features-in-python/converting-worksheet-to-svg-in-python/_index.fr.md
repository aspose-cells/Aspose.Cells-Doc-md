---
title: Conversion de la feuille de calcul en SVG en Python
type: docs
weight: 50
url: /fr/java/converting-worksheet-to-svg-in-python/
---
## **Aspose.Cells - Conversion de la feuille de travail en SVG**
Pour convertir la feuille de calcul en SVG en utilisant Aspose.Cells for Java dans Python, appelez simplement la feuille de calcul_à_Méthode svg() du module Converter.

**Code Python**

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
## **Télécharger le code d'exécution**
 Télécharger**Conversion de la feuille de calcul en SVG(Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
