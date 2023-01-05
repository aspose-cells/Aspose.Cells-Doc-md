---
title: Заморозить панели в Jython
type: docs
weight: 60
url: /ru/java/freeze-panes-in-jython/
---
## **Aspose.Cells - Замораживание панелей**
 Для добавления документов с помощью**Aspose.Cells Java для Jython**. Здесь вы можете увидеть пример кода.

**Код Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class FreezePanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/FreezePanes/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Applying freeze panes settings

        worksheet.freezePanes(3,2,3,2)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "book.out.xls")

        #Print Message

        print "Panes freeze successfull."

if __name__ == '__main__':        

    FreezePanes()

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Добавить документы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/FreezePanes.py)
