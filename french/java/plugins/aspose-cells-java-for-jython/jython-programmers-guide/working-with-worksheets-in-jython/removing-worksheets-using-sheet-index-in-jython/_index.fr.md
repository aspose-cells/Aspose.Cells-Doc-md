---
title: Suppression de feuilles de calcul à l'aide de l'index de feuilles dans Jython
type: docs
weight: 110
url: /fr/java/removing-worksheets-using-sheet-index-in-jython/
---
## **Aspose.Cells - Suppression de feuilles de calcul à l'aide de l'index des feuilles**
 Pour joindre des documents à l'aide de**Aspose.Cells Java pour Jython**. Ici vous pouvez voir un exemple de code.

**Code Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from java.io import FileInputStream;


class RemovingWorksheetsusingSheetIndex:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex/'



        fstream=FileInputStream(dataDir + "Book1.xls");

        #Instantiating a Workbook object with the stream

        workbook = Workbook(fstream)

        #Removing a worksheet using its sheet index

        workbook.getWorksheets().removeAt(0)

        #Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        #Closing the file stream to free all resources

        fstream.close()


        #Print Message

        print "Sheet removed successfully."

if __name__ == '__main__':        

    RemovingWorksheetsusingSheetIndex()

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Joindre des documents (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex.py)
