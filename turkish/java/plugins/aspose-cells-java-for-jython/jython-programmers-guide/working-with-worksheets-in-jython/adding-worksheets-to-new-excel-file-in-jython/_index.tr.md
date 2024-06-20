---
title: Jython da Yeni Excel Dosyasına Çalışsayfa Ekleme
type: docs
weight: 10
url: /tr/java/adding-worksheets-to-new-excel-file-in-jython/
---

## **Aspose.Cells - Yeni Excel'e Çalışsayfa Ekleme**
**Aspose.Cells Java for Jython** ile belgeler eklemek için. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class AddingWorksheetstoNewExcelFile:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/AddingWorksheetstoNewExcelFile/'



        workbook = Workbook(dataDir + "Book1.xls")

        #Adding a new worksheet to the Workbook object

        worksheets = workbook.getWorksheets()

        sheetIndex = worksheets.add()

        worksheet = worksheets.get(sheetIndex)

        #Setting the name of the newly added worksheet

        worksheet.setName("My Worksheet")

        #Saving the Excel file

        workbook.save(dataDir + "book.out.xls")

        #Print Message

        print "Sheet added successfully."

if __name__ == '__main__':        

    AddingWorksheetstoNewExcelFile()

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Append Documents (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/AddingWorksheetstoNewExcelFile.py)
