---
title: Geteilte Fenster in Jython
type: docs
weight: 140
url: /de/java/split-panes-in-jython/
---

## **Aspose.Cells - Panes aufteilen**
Zum Anfügen von Dokumenten mit **Aspose.Cells Java für Jython**. Hier sehen Sie Beispielscode.

**Jython-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Dokumente anfügen (Aspose.Cells)** von einer der unten genannten Plattformen für soziale Codierung herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SplitPanes.py)
