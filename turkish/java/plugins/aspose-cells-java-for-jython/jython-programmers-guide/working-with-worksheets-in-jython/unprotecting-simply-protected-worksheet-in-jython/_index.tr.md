---
title: Jython ile Basitçe Korunan Çalışsayfaların Korumasız Bırakılması
type: docs
weight: 160
url: /tr/java/unprotecting-simply-protected-worksheet-in-jython/
---

## **Aspose.Cells - Basitçe Korunan Çalışsayfa Koruması**
**Aspose.Cells Java for Jython** ile belgeler eklemek için. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat

from com.aspose.cells import FileFormatType


class UnprotectingSimplyProtectedWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet/'



        filesFormatType = FileFormatType

        #Instantiating a Workbook object

        workbook = Workbook(dataDir + "Book1.xls")

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        protection = worksheet.getProtection()

        #The following 3 methods are only for Excel 2000 and earlier formats

        protection.setAllowEditingContent(False)

        protection.setAllowEditingObject(False)

        protection.setAllowEditingScenario(False)

        #Unprotecting the worksheet

        worksheet.unprotect()

        # Save the excel file.

        workbook.save(dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

        #Print Message

        print "Worksheet unprotected successfully."

if __name__ == '__main__':        

    UnprotectingSimplyProtectedWorksheet()

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Append Documents (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingSimplyProtectedWorksheet.py)
