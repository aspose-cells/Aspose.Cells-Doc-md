---
title: Разделение панелей в Jython
type: docs
weight: 140
url: /ru/java/split-panes-in-jython/
---
## **Aspose.Cells - Разделенные панели**
 Для добавления документов с помощью**Aspose.Cells Java для Jython**. Здесь вы можете увидеть пример кода.

**Код Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class SplitPanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SplitPanes/'



        saveFormat = SaveFormat;



        workbook = Workbook(dataDir + "Book1.xls")

        #Set the active cell

        workbook.getWorksheets().get(0).setActiveCell("A20");

        #Split the worksheet window

        workbook.getWorksheets().get(0).split();

        #Save the excel file

        workbook.save(dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

        #Print Message

        print "Panes split successfully."

if __name__ == '__main__':        

    SplitPanes()

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Добавить документы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SplitPanes.py)
