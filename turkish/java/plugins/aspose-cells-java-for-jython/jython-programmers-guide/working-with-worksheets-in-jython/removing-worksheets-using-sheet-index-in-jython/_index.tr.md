---
title: Jython kullanarak Sayfa Düzenini Ayarlama
type: docs
weight: 110
url: /tr/java/removing-worksheets-using-sheet-index-in-jython/
---

## **Aspose.Cells - Sayfa Düzenini Ayarlama**
**Aspose.Cells Java for Jython** ile belgeler eklemek için. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from java.io import FileInputStream;


class RemovingWorksheetsusingSheetIndex:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex/'



        fstream=FileInputStream(dataDir + "Book1.xls");

        #Instantiating a Workbook object with the stream

        workbook = Workbook(fstream)

        #Removing a worksheet using its sheet index

        workbook.getWorksheets().removeAt(0)

        #Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        #Closing the file stream to free all resources

        fstream.close()


        #Print Message

        print "Sheet removed successfully."

if __name__ == '__main__':        

    RemovingWorksheetsusingSheetIndex()

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Append Documents (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/RemovingWorksheetsusingSheetIndex.py)
