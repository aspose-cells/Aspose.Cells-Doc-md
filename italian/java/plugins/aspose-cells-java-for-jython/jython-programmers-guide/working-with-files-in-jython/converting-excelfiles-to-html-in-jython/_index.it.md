---
title: Convertire file Excel in Html in Jython
type: docs
weight: 10
url: /it/java/converting-excelfiles-to-html-in-jython/
---

## **Aspose.Cells - Convertire file Excel in Html**
Per aggiungere documenti utilizzando **Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class ConvertingExcelFilesToHtml:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingExcelFilesToHtml/'



        saveFormat = SaveFormat

        workbook = Workbook(dataDir + "Book1.xls")

        #Save the document in PDF format

        workbook.save(dataDir + "OutBook1.html", saveFormat.HTML)

        # Print message

        print "\n Excel to HTML conversion performed successfully."



if __name__ == '__main__':        

    ConvertingExcelFilesToHtml()

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Aggiungi documenti (Aspose.Cells)** da qualsiasi dei siti di codifica sociale qui sotto menzionati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)
