---
title: Conversione in file Mhtml in Jython
type: docs
weight: 20
url: /it/java/converting-to-mhtml-files-in-jython/
---
## **Aspose.Cells - Conversione in file Mhtml**
 Per aggiungere documenti utilizzando**Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import HtmlSaveOptions

from com.aspose.cells import SaveFormat


class ConvertingToMhtmlFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToMhtmlFiles/'



        saveFormat = SaveFormat

        #Specify the file path

        filePath = dataDir + "Book1.xlsx"

        #Specify the HTML saving options

        sv = HtmlSaveOptions(saveFormat.M_HTML)

        #Instantiate a workbook and open the template XLSX file

        wb = Workbook(filePath)

        #Save the MHT file

        wb.save(filePath + ".out.mht", sv)

        # Print message

        print "Excel to MHTML conversion performed successfully."



if __name__ == '__main__':        

    ConvertingToMhtmlFiles()

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scaricamento**Aggiungi documenti (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToMhtmlFiles.py)
