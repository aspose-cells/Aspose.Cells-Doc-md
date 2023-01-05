---
title: Konvertera arbetsblad till SVG i Jython
type: docs
weight: 40
url: /sv/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - Konvertera arbetsblad till SVG**
 För att lägga till dokument med hjälp av**Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Code**

{{< highlight "java" >}}

 från aspose-celler importera inställningar

från com.aspose.cells import arbetsbok

från com.aspose.cells importera ImageFormat

från com.aspose.cells importera ImageOrPrintOptions

från com.aspose.cells importera SheetRender

från com.aspose.cells importera SaveFormat



class ConvertingWorksheetToSVG:

 def__i det__(själv):

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



 saveFormat = SaveFormat

 arbetsbok = Arbetsbok(dataDir + "Book1.xls")

 #Konvertera varje kalkylblad till svg-format på en enda sida.

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(True)

 #Konvertera varje kalkylblad till svg-format

 sheetCount = workbook.getWorksheets().getCount()

 #for(i=0; i<sheetCount; i++)

        for i in range(sheetCount):



            sheet = workbook.getWorksheets().get(i)

            sr = SheetRender(sheet, imgOptions)

            pageCount = sr.getPageCount()

            #for (k = 0 k < pageCount k++)

            for k in range(pageCount):



                #Output the worksheet into Svg image format

                sr.toImage(k, dataDir + sheet.getName() + ".out.svg")





        # Print message

        print "Excel to SVG conversion completed successfully."



if __name__ == '__main__':        

    ConvertingWorksheetToSVG()

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Bifoga dokument (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
