---
title: Registerkarten im Jython ausblenden
type: docs
weight: 50
url: /de/java/display-hide-tabs-in-jython/
---

## **Aspose.Cells - Anzeigen und Ausblenden von Registerkarten**
Zum Anfügen von Dokumenten mit **Aspose.Cells Java für Jython**. Hier sehen Sie Beispielscode.

**Jython-Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideTabs:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideTabs/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Hiding the tabs of the Excel file

        workbook.getSettings().setShowTabs(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Tabs are now hidden, please check the output file."

if __name__ == '__main__':        

    DisplayHideTabs()

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Dokumente anfügen (Aspose.Cells)** von einer der unten genannten Plattformen für soziale Codierung herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideTabs.py)
