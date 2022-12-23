---
title: Conversione del foglio di lavoro in SVG in Jython
type: docs
weight: 40
url: /it/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - Conversione del foglio di lavoro in SVG**
 Per aggiungere documenti utilizzando**Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

{{< highlight "java" >}}

 dalle impostazioni di importazione delle celle aspose

da com.aspose.cells importa cartella di lavoro

da com.aspose.cells importare ImageFormat

da com.aspose.cells importa ImageOrPrintOptions

da com.aspose.cells importare SheetRender

da com.aspose.cells importa SaveFormat



classe ConvertingWorksheetToSVG:

 def__dentro__(se stesso):

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



 saveFormat = SalvaFormato

 cartella di lavoro = Cartella di lavoro(dataDir + "Libro1.xls")

 # Converti ogni foglio di lavoro in formato svg in una singola pagina.

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(True)

 # Converti ogni foglio di lavoro in formato svg

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
## **Scarica il codice in esecuzione**
 Scaricamento**Aggiungi documenti (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
