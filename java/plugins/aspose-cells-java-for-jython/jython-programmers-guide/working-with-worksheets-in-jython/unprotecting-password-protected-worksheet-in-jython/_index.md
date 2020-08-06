---
title: Unprotecting Password Protected Worksheet in Jython
type: docs
weight: 150
url: /java/unprotecting-password-protected-worksheet-in-jython/
---

## **Aspose.Cells - Append Documents**
To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat

from com.aspose.cells import FileFormatType;


class UnprotectingPasswordProtectedWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet/'



        filesFormatType = FileFormatType

        #Instantiating a Workbook object

        workbook = Workbook(dataDir + "book1.xls")

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        protection = worksheet.getProtection()

        #Unprotecting the worksheet with a password

        worksheet.unprotect("aspose")

        # Save the excel file.

        workbook.save(dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

        #Print Message

        print "Worksheet unprotected successfully."

if __name__ == '__main__':        

    UnprotectingPasswordProtectedWorksheet()

{{< /highlight >}}
## **Download Running Code**
Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

- [CodePlex](http://asposecellsjavajython.codeplex.com/SourceControl/latest#asposecells/WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet.py)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet.py)
