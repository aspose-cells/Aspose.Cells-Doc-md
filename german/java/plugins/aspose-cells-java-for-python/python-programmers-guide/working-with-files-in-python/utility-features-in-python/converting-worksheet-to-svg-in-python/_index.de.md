---
title: Arbeitsblatt in SVG in Python umwandeln
type: docs
weight: 50
url: /de/java/converting-worksheet-to-svg-in-python/
---

## **Aspose.Cells - Konvertierung von Arbeitsblatt in SVG**
Um ein Arbeitsblatt in Python mit Aspose.Cells for Java in SVG umzuwandeln, rufen Sie einfach die Methode worksheet_to_svg() des Converter-Moduls auf.

**Python-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Arbeitsblatt in SVG umwandeln (Aspose.Cells)** von einer der unten genannten sozialen Programmierseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
