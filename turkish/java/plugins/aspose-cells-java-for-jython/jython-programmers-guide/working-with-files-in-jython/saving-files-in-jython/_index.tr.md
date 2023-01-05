﻿---
title: Jython'da Dosyaları Kaydetme
type: docs
weight: 80
url: /tr/java/saving-files-in-jython/
---
## **Aspose.Cells - Dosyaları Kaydetme**
 Belgeleri kullanarak eklemek için**Jython için Aspose.Cells Java**. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight "java" >}}

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
## **Çalışan Kodu İndir**
 İndirmek**Belgeleri Ekleyin (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/SavingFiles.py)
