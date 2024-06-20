---
title: Kalkylblad till bild i Jython
type: docs
weight: 90
url: /sv/java/worksheet-to-image-in-jython/
---

## **Aspose.Cells - Kalkylblad till bild**
Att lägga till dokument med **Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Kod**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import ImageFormat

from com.aspose.cells import ImageOrPrintOptions

from com.aspose.cells import SheetRender

class WorksheetToImage:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/WorksheetToImage/'



        imageFormat = ImageFormat



        #Instantiate a workbook with path to an Excel file

        book = Workbook(dataDir + "Book1.xls")

        #Create an object for ImageOptions

        imgOptions = ImageOrPrintOptions()

        #Set the image type

        imgOptions.setImageFormat(imageFormat.getPng())

        #Get the first worksheet.

        sheet = book.getWorksheets().get(0)

        #Create a SheetRender object for the target sheet

        sr =SheetRender(sheet, imgOptions)

        for i in range(sr.getPageCount()):



            #Generate an image for the worksheet

            sr.toImage(i, dataDir + "mysheetimg" + ".png")



        # Print message

        print "Images generated successfully."



if __name__ == '__main__':        

    WorksheetToImage()

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Hämta dokument (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/WorksheetToImage.py)
