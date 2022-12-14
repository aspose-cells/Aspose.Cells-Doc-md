---
title: Conversion d'une feuille de calcul en SVG dans Jython
type: docs
weight: 40
url: /fr/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - Conversion de la feuille de calcul en SVG**
 Pour joindre des documents à l'aide de**Aspose.Cells Java pour Jython**. Ici vous pouvez voir un exemple de code.

**Code Jython**

{{< highlight "java" >}}

 à partir des paramètres d'importation de cellules aspose

à partir de com.aspose.cells importer le classeur

de com.aspose.cells importer ImageFormat

à partir de com.aspose.cells importer ImageOrPrintOptions

de com.aspose.cells importer SheetRender

de com.aspose.cells importer SaveFormat



classe ConvertingWorksheetToSVG :

 définitivement__initialiser__(soi):

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



 saveFormat = Enregistrer le format

 classeur = classeur(dataDir + "Book1.xls")

#Convertir chaque feuille de calcul au format svg en une seule page.

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(True)

 #Convertir chaque feuille de calcul au format svg

 sheetCount = classeur.getWorksheets().getCount()

 #pour(je=0; je<sheetCount; i++)

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
## **Télécharger le code d'exécution**
 Télécharger**Joindre des documents (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
