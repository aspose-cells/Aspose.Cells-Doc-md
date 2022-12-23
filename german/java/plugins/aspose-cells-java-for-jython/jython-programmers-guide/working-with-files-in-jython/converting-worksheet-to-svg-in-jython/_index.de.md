---
title: Konvertieren des Arbeitsblatts in SVG in Jython
type: docs
weight: 40
url: /de/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - Konvertieren des Arbeitsblatts in SVG**
 Zum Anhängen von Dokumenten mit**Aspose.Cells Java für Jython**. Hier sehen Sie Beispielcode.

**Jython-Code**

{{< highlight "java" >}}

 aus aspose-cells Importeinstellungen

aus com.aspose.cells import Workbook

aus com.aspose.cells import ImageFormat

aus com.aspose.cells import ImageOrPrintOptions

aus com.aspose.cells importiert SheetRender

aus com.aspose.cells importiere SaveFormat



Klasse ConvertingWorksheetToSVG:

 def__drin__(selbst):

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



 saveFormat = SaveFormat

 Arbeitsmappe = Arbeitsmappe(dataDir + "Book1.xls")

 #Konvertieren Sie jedes Arbeitsblatt auf einer einzigen Seite in das SVG-Format.

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(True)

 #Konvertieren Sie jedes Arbeitsblatt in das SVG-Format

 sheetCount = arbeitsmappe.getWorksheets().getCount()

 #für(i=0; ich<sheetCount; i++)

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
## **Laufcode herunterladen**
 Download**Dokumente anhängen (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
