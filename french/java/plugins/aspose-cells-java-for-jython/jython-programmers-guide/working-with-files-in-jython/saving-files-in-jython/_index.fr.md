---
title: Enregistrement de fichiers dans Jython
type: docs
weight: 80
url: /fr/java/saving-files-in-jython/
---
## **Aspose.Cells - Enregistrement de fichiers**
 Pour joindre des documents à l'aide de**Aspose.Cells Java pour Jython**. Ici vous pouvez voir un exemple de code.

**Code Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import FileFormatType


class SavingFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/SavingFiles/'



        fileFormatType = FileFormatType





        #Creating an Workbook object with an Excel file path

        workbook = Workbook(dataDir + "Book1.xls")

        #Save in default (Excel2003) format

        workbook.save(dataDir + "book.default.out.xls")

        #Save in Excel2003 format

        workbook.save(dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

        #Save in Excel2007 xlsx format

        workbook.save(dataDir + "book.out.xlsx", fileFormatType.XLSX)

        #Save in SpreadsheetML format

        workbook.save(dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)



        #Print Message

        print("<BR>")

        print("Worksheets are saved successfully.")





if __name__ == '__main__':        

    SavingFiles()

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Joindre des documents (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/SavingFiles.py)
