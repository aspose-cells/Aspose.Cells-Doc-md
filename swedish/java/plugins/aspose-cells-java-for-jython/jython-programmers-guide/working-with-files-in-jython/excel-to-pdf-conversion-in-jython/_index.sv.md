---
title: Excel till Pdf omvandling i Jython
type: docs
weight: 50
url: /sv/java/excel-to-pdf-conversion-in-jython/
---

## **Aspose.Cells - Excel till Pdf-omvandling**
Att lägga till dokument med **Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Kod**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat



class Excel2PdfConversion:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/Excel2PdfConversion/'



        saveFormat = SaveFormat

        workbook = Workbook(dataDir + "Book1.xls")

        #Save the document in PDF format

        workbook.save(dataDir + "OutBook1.pdf", saveFormat.PDF)

        # Print message

        print "\n Excel to PDF conversion performed successfully."



if __name__ == '__main__':        

    Excel2PdfConversion()

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Hämta dokument (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/Excel2PdfConversion.py)
