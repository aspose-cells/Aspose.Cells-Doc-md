---
title: Visa Dölj Scroll Bars i Jython
type: docs
weight: 40
url: /sv/java/display-hide-scroll-bars-in-jython/
---

## **Aspose.Cells - Visa Dölj Scroll Bars**
Att lägga till dokument med **Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Kod**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideScrollBars:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideScrollBars/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Hiding the vertical scroll bar of the Excel file

        workbook.getSettings().setVScrollBarVisible(False)

        #Hiding the horizontal scroll bar of the Excel file

        workbook.getSettings().setHScrollBarVisible(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Scroll bars are now hidden, please check the output document."



if __name__ == '__main__':        

    DisplayHideScrollBars()

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Hämta dokument (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideScrollBars.py)
