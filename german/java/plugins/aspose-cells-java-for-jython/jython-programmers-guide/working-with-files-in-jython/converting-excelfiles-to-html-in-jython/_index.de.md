---
title: Excel Dateien in Html in Jython konvertieren
type: docs
weight: 10
url: /de/java/converting-excelfiles-to-html-in-jython/
---

## **Aspose.Cells - Konvertieren von Excel-Dateien in Html**
Zum Anfügen von Dokumenten mit **Aspose.Cells Java für Jython**. Hier sehen Sie Beispielscode.

**Jython-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Dokumente anfügen (Aspose.Cells)** von einer der unten genannten Plattformen für soziale Codierung herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingExcelFilesToHtml.py)
