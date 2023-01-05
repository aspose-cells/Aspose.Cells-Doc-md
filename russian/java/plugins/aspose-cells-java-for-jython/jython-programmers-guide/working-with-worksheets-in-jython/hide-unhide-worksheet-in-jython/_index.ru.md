---
title: Скрыть рабочий лист в Jython
type: docs
weight: 70
url: /ru/java/hide-unhide-worksheet-in-jython/
---
## **Aspose.Cells - Скрыть рабочий лист**
 Для добавления документов с помощью**Aspose.Cells Java для Jython**. Здесь вы можете увидеть пример кода.

**Код Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class HideUnhideWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/HideUnhideWorksheet/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Hiding the first worksheet of the Excel file

        worksheet.setVisible(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Worksheet 1 is now hidden, please check the output document."

if __name__ == '__main__':        

    HideUnhideWorksheet()

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Добавить документы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/HideUnhideWorksheet.py)
