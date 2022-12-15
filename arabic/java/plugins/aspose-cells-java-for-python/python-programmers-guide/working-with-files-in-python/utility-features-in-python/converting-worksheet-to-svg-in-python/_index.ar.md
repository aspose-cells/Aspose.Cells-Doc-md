---
title: تحويل ورقة العمل إلى SVG في Python
type: docs
weight: 50
url: /ar/java/converting-worksheet-to-svg-in-python/
---
## **Aspose.Cells - تحويل ورقة العمل إلى SVG**
لتحويل ورقة العمل إلى SVG باستخدام Aspose.Cells for Java في Python ، ما عليك سوى استدعاء ورقة العمل_إلى_svg () طريقة وحدة المحول.

**Python كود**

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
## **تحميل كود الجري**
 تحميل**تحويل ورقة العمل إلى SVG (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
