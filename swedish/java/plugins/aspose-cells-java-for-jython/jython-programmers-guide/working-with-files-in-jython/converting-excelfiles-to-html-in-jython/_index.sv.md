---
title: Konvertering av Excelfiler till HTML i Jython
type: docs
weight: 10
url: /sv/java/converting-excelfiles-to-html-in-jython/
---

## **Aspose.Cells - Konvertering av Excelfiler till HTML**
Att lägga till dokument med **Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Kod**

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
## **Ladda ned körbar kod**
Ladda ned **Hämta dokument (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)
