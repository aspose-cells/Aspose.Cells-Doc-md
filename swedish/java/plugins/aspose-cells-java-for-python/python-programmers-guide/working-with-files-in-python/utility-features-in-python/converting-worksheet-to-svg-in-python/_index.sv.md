---
title: Konvertera arbetsblad till SVG i Python
type: docs
weight: 50
url: /sv/java/converting-worksheet-to-svg-in-python/
---
## **Aspose.Cells - Konvertera arbetsblad till SVG**
För att konvertera kalkylblad till SVG med Aspose.Cells for Java i Python, anropa kalkylblad_till_svg()-metoden för omvandlarmodulen.

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
## **Ladda ner Running Code**
 Ladda ner**Konvertera arbetsblad till SVG(Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
