---
title: Conversión de hoja de trabajo a SVG en Python
type: docs
weight: 50
url: /es/java/converting-worksheet-to-svg-in-python/
---
## **Aspose.Cells - Hoja de trabajo de conversión a SVG**
Para convertir la hoja de trabajo a SVG usando Aspose.Cells for Java en Python, simplemente invoque la hoja de trabajo_a_Método svg() del módulo Converter.

**Código Python**

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
## **Descargar código de ejecución**
 Descargar**Conversión de hoja de cálculo a SVG(Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
