---
title : "Worksheet To Image in Jython" 
description : "" 
weight : 20796 
toc : false
type: docs
url: /java/plugins/jython/guide/files/worksheet+to+image+in+jython/
---

# Aspose.Cells for Java : Worksheet To Image in Jython


## Aspose.Cells - Worksheet To Image

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import ImageFormatfrom com.aspose.cells import ImageOrPrintOptionsfrom com.aspose.cells import SheetRenderclass WorksheetToImage:    def \_\_init\_\_(self):        dataDir = Settings.dataDir + 'WorkingWithFiles/WorksheetToImage/'                imageFormat = ImageFormat                #Instantiate a workbook with path to an Excel file        book = Workbook(dataDir + "Book1.xls")        #Create an object for ImageOptions        imgOptions = ImageOrPrintOptions()        #Set the image type        imgOptions.setImageFormat(imageFormat.getPng())        #Get the first worksheet.        sheet = book.getWorksheets().get(0)        #Create a SheetRender object for the target sheet        sr =SheetRender(sheet, imgOptions)        for i in range(sr.getPageCount()):                    #Generate an image for the worksheet            sr.toImage(i, dataDir + "mysheetimg" + ".png")                # Print message        print "Images generated successfully." if \_\_name\_\_ == '\_\_main\_\_':            WorksheetToImage()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithFiles/WorksheetToImage.py)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/WorksheetToImage.py)

