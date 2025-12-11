---
title: Converting Worksheet to SVG in Python
type: docs
weight: 50
url: /java/converting-worksheet-to-svg-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting Worksheet to SVG**
To convert a worksheet to SVG using Aspose.Cells for Java in Python, simply invoke the `worksheet_to_svg()` method of the Converter module.

**Python Code**

{{< highlight python >}}
saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Convert each worksheet into SVG format on a single page.
imgOptions = ImageOrPrintOptions()
imgOptions.setSaveFormat(saveFormat.SVG)
imgOptions.setOnePagePerSheet(True)

# Convert each worksheet into SVG format
sheetCount = workbook.getWorksheets().getCount()

# for(i = 0; i < sheetCount; i++)
for i in range(sheetCount):
    sheet = workbook.getWorksheets().get(i)
    sr = SheetRender(sheet, imgOptions)
    pageCount = sr.getPageCount()

    # for (k = 0; k < pageCount; k++)
    for k in range(pageCount):
        # Output the worksheet into SVG image format
        sr.toImage(k, self.dataDir + sheet.getName() + ".out.svg")

# Print message
print("Excel to SVG conversion completed successfully.")
{{< /highlight >}}

## **Download Running Code**
Download **Converting Worksheet To SVG (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
