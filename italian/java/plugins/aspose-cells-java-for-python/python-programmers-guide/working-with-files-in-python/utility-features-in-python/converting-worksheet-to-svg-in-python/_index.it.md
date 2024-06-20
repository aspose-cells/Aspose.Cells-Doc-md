---
title: Conversione del Foglio di lavoro in SVG in Python
type: docs
weight: 50
url: /it/java/converting-worksheet-to-svg-in-python/
---

## **Aspose.Cells - Conversione di un foglio di lavoro in SVG**
Per convertire un Foglio di lavoro in SVG usando Aspose.Cells for Java in Python, basta invocare il metodo worksheet_to_svg() del modulo Convertitore.

**Codice Python**

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
## **Scarica il codice in esecuzione**
Scarica **Conversione del Foglio di lavoro in SVG(Aspose.Cells)** da uno qualsiasi dei siti di coding social qui sotto menzionati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
