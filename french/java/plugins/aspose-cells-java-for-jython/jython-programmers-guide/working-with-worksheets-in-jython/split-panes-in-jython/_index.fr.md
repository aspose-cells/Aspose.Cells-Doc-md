---
title: Fenêtres fractionnées en Jython
type: docs
weight: 140
url: /fr/java/split-panes-in-jython/
---

## **Aspose.Cells - Diviser les volets**
Pour ajouter des documents en utilisant **Aspose.Cells Java for Jython**. Vous pouvez voir ici le code d'exemple.

**Code Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class SplitPanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SplitPanes/'



        saveFormat = SaveFormat;



        workbook = Workbook(dataDir + "Book1.xls")

        #Set the active cell

        workbook.getWorksheets().get(0).setActiveCell("A20");

        #Split the worksheet window

        workbook.getWorksheets().get(0).split();

        #Save the excel file

        workbook.save(dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

        #Print Message

        print "Panes split successfully."

if __name__ == '__main__':        

    SplitPanes()

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Ajouter des documents (Aspose.Cells)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SplitPanes.py)
