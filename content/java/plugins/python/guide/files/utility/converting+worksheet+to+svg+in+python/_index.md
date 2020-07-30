---
title : "Converting Worksheet to SVG in Python" 
description : "" 
weight : 24754 
toc : false
type: docs
url: /java/plugins/python/guide/files/utility/converting+worksheet+to+svg+in+python/
---

# Aspose.Cells for Java : Converting Worksheet to SVG in Python


## Aspose.Cells - Converting Worksheet to SVG

To convert Worksheet to SVG using Aspose.Cells for Java in Python, simply invoke worksheet\_to\_svg() method of Converter module.

**Python Code**

saveFormat = self.SaveFormatworkbook = self.Workbook(self.dataDir + "Book1.xls")#Convert each worksheet into svg format in a single page.imgOptions = ImageOrPrintOptions()imgOptions.setSaveFormat(saveFormat.SVG)imgOptions.setOnePagePerSheet(True)#Convert each worksheet into svg formatsheetCount = workbook.getWorksheets().getCount()#for(i=0; i<sheetCount; i++)for i in range(sheetCount):sheet = workbook.getWorksheets().get(i)sr = SheetRender(sheet, imgOptions)pageCount = sr.getPageCount()#for (k = 0 k < pageCount k++)for k in range(pageCount):#Output the worksheet into Svg image formatsr.toImage(k, self.dataDir + sheet.getName() + ".out.svg")# Print messageprint "Excel to SVG conversion completed successfully."

## Download Running Code

Download **Converting Worksheet To SVG(Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

