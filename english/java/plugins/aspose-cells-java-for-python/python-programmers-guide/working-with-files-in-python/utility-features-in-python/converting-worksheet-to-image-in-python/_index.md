---
title: Converting Worksheet to Image in Python
type: docs
weight: 40
url: /java/converting-worksheet-to-image-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting Worksheet to Image**
To convert a worksheet to an image using Aspose.Cells for Java in Python, simply invoke the Converter module.

**Python Code**

{{< highlight python >}}
imageFormat = self.ImageFormat

# Instantiate a workbook with the path to an Excel file
book = self.Workbook(self.dataDir + "Book1.xls")

# Create an object for ImageOptions
imgOptions = self.ImageOrPrintOptions()

# Set the image type
imgOptions.setImageFormat(imageFormat.getPng())

# Get the first worksheet.
sheet = book.getWorksheets().get(0)

# Create a SheetRender object for the target sheet
sr = self.SheetRender(sheet, imgOptions)

for i in range(sr.getPageCount()):
    # Generate an image for the worksheet
    sr.toImage(i, self.dataDir + "mysheetimg" + ".png")

# Print message
print "Images generated successfully."
{{< /highlight >}}

## **Download Running Code**
Download **Worksheet To Image (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
