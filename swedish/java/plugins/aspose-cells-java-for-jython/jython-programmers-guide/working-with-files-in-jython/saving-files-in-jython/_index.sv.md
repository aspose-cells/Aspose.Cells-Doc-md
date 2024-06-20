---
title: Spara filer i Jython
type: docs
weight: 80
url: /sv/java/saving-files-in-jython/
---

## **Aspose.Cells - Spara filer**
Att lägga till dokument med **Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Kod**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import FileFormatType


class SavingFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/SavingFiles/'



        fileFormatType = FileFormatType





        #Creating an Workbook object with an Excel file path

        workbook = Workbook(dataDir + "Book1.xls")

        #Save in default (Excel2003) format

        workbook.save(dataDir + "book.default.out.xls")

        #Save in Excel2003 format

        workbook.save(dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

        #Save in Excel2007 xlsx format

        workbook.save(dataDir + "book.out.xlsx", fileFormatType.XLSX)

        #Save in SpreadsheetML format

        workbook.save(dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)



        #Print Message

        print("<BR>")

        print("Worksheets are saved successfully.")





if __name__ == '__main__':        

    SavingFiles()

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Hämta dokument (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/SavingFiles.py)
