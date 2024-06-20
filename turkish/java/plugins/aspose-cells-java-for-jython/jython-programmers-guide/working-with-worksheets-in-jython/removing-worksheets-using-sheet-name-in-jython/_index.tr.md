---
title: Jython kullanarak Çalışan Kodu İndirme ve Ekleme
type: docs
weight: 120
url: /tr/java/removing-worksheets-using-sheet-name-in-jython/
---

## **Aspose.Cells - Çalışan Kodu İndirme ve Ekleme**
**Aspose.Cells Java for Jython** ile belgeler eklemek için. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

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
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Append Documents (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetName.py)
