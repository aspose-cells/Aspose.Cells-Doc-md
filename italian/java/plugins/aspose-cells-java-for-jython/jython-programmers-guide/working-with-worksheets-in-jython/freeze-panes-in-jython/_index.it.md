---
title: Fissa i riquadri in Jython
type: docs
weight: 60
url: /it/java/freeze-panes-in-jython/
---

## **Aspose.Cells - Fissa i riquadri**
Per aggiungere documenti utilizzando **Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class FreezePanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/FreezePanes/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Applying freeze panes settings

        worksheet.freezePanes(3,2,3,2)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "book.out.xls")

        #Print Message

        print "Panes freeze successfull."

if __name__ == '__main__':        

    FreezePanes()

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Aggiungi documenti (Aspose.Cells)** da qualsiasi dei siti di codifica sociale qui sotto menzionati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/FreezePanes.py)
