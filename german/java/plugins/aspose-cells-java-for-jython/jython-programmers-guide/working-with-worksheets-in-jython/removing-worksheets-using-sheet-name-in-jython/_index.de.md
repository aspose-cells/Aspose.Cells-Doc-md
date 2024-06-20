---
title: Arbeitsblätter unter Verwendung des Blattnamens in Jython entfernen
type: docs
weight: 120
url: /de/java/removing-worksheets-using-sheet-name-in-jython/
---

## **Aspose.Cells - Arbeitsblätter unter Verwendung des Blattnamens entfernen**
Zum Anfügen von Dokumenten mit **Aspose.Cells Java für Jython**. Hier sehen Sie Beispielscode.

**Jython-Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from java.io import FileInputStream;


class RemovingWorksheetsusingSheetName:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetName/'



        #Creating a file stream containing the Excel file to be opened

        fstream = FileInputStream(dataDir + "Book1.xls");

        #Instantiating a Workbook object with the stream

        workbook = Workbook(fstream);

        #Removing a worksheet using its sheet name

        workbook.getWorksheets().removeAt("Sheet1");

        #Saving the Excel file

        workbook.save(dataDir + "book.out.xls");

        #Closing the file stream to free all resources

        fstream.close();

        #Print Message

        print "Sheet removed successfully.";

if __name__ == '__main__':        

    RemovingWorksheetsusingSheetName()

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Dokumente anfügen (Aspose.Cells)** von einer der unten genannten Plattformen für soziale Codierung herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetName.py)
