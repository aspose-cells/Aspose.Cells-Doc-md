---
title: Регулировка высоты строки и ширины столбца в Jython
type: docs
weight: 10
url: /ru/java/adjusting-row-height-and-column-width-in-jython/
---

## **Aspose.Cells - Изменение высоты строки и ширины столбца**
Для добавления документов с помощью **Aspose.Cells Java для Jython**. Здесь вы можете увидеть примерный код.

**Код Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class RowsAndColumns:

    def __init__(self):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



        # Setting the Row Height

        self.set_row_height()

        # Setting the Width of a Column

        self.set_column_width()    

    def set_row_height(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        cells = worksheet.getCells()

        # Setting the height of the second row to 13

        cells.setRowHeight(1, 13)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Set Row Height.xls")

        print "Set Row Height Successfully." 



    def set_column_width(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'    

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        cells = worksheet.getCells()

        # Setting the width of the second column to 17.5

        cells.setColumnWidth(1, 17.5)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Set Column Width.xls")

        print "Set Column Width Successfully." 

if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Append Documents (Aspose.Cells)** c любого из упомянутых ниже социальных сайтов для кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
