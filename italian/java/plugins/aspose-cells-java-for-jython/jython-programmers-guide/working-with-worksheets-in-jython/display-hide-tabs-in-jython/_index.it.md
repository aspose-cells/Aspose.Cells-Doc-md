---
title: Mostra Nascondi schede in Jython
type: docs
weight: 50
url: /it/java/display-hide-tabs-in-jython/
---
## **Aspose.Cells - Mostra Nascondi schede**
 Per aggiungere documenti utilizzando**Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

{{< highlight "java" >}}

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
## **Scarica il codice in esecuzione**
 Scarica**Aggiungi documenti (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideTabs.py)
