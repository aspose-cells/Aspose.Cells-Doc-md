---
title: Показать скрыть линии сетки в Jython
type: docs
weight: 30
url: /ru/java/display-hide-gridlines-in-jython/
---
## **Aspose.Cells - Показать скрыть линии сетки**
 Для добавления документов с помощью**Aspose.Cells Java для Jython**. Здесь вы можете увидеть пример кода.

**Код Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideGridlines:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideGridlines/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Hiding the grid lines of the first worksheet of the Excel file

        worksheet.setGridlinesVisible(False)

        #Saving the modified Excel file in default (that is Excel 2000) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Grid lines are now hidden on sheet 1, please check the output document."



if __name__ == '__main__':        

    DisplayHideGridlines()

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Добавить документы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideGridlines.py)
