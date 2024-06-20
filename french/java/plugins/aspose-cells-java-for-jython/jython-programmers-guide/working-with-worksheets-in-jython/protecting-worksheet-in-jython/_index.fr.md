---
title: Protéger la feuille de calcul en Jython
type: docs
weight: 100
url: /fr/java/protecting-worksheet-in-jython/
---

## **Aspose.Cells - Protéger la feuille de calcul**
Pour ajouter des documents en utilisant **Aspose.Cells Java for Jython**. Vous pouvez voir ici le code d'exemple.

**Code Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class ProtectingWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ProtectingWorksheet/'



        #Instantiating a Excel object by excel file path

        excel = Workbook(dataDir + "Book1.xls")

        #Accessing the first worksheet in the Excel file

        worksheets = excel.getWorksheets()

        worksheet = worksheets.get(0)

        protection = worksheet.getProtection()

        #The following 3 methods are only for Excel 2000 and earlier formats

        protection.setAllowEditingContent(False)

        protection.setAllowEditingObject(False)

        protection.setAllowEditingScenario(False)

        #Protects the first worksheet with a password "1234"

        protection.setPassword("1234")

        #Saving the modified Excel file in default format

        excel.save(dataDir + "output.xls")

        #Print Message

        print "Sheet protected successfully."

if __name__ == '__main__':        

    ProtectingWorksheet()

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Ajouter des documents (Aspose.Cells)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/ProtectingWorksheet.py)
