---
title : "Converting Worksheet to Image in Python" 
description : "" 
weight : 24753 
toc : false
type: docs
url: /java/plugins/python/guide/files/utility/converting+worksheet+to+image+in+python/
---

# Aspose.Cells for Java : Converting Worksheet to Image in Python


## Aspose.Cells - Converting Worksheet to Image

To convert Worksheet to Image using Aspose.Cells for Java in Ruby, simply invoke Converter module.

**Python Code**

imageFormat = self.ImageFormat#Instantiate a workbook with path to an Excel filebook = self.Workbook(self.dataDir + "Book1.xls")#Create an object for ImageOptionsimgOptions = self.ImageOrPrintOptions()#Set the image typeimgOptions.setImageFormat(imageFormat.getPng())#Get the first worksheet.sheet = book.getWorksheets().get(0)#Create a SheetRender object for the target sheetsr =self.SheetRender(sheet, imgOptions)for i in range(sr.getPageCount()):#Generate an image for the worksheetsr.toImage(i, self.dataDir + "mysheetimg" + ".png")# Print messageprint "Images generated successfully."

## Download Running Code

Download **Worksheet To Image (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

