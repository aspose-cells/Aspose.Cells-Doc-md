---
title: Enregistrement de fichiers en Jython
type: docs
weight: 80
url: /fr/java/saving-files-in-jython/
---

## **Aspose.Cells - Enregistrement de fichiers**
Pour ajouter des documents en utilisant **Aspose.Cells Java for Jython**. Vous pouvez voir ici le code d'exemple.

**Code Jython**

{{< highlight java >}}

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Ajouter des documents (Aspose.Cells)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/SavingFiles.py)
