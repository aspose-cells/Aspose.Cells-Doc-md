---
title: 在Jython中调整行高度和列宽度
type: docs
weight: 10
url: /zh/java/adjusting-row-height-and-column-width-in-jython/
---

## **Aspose.Cells - 调整行高和列宽**
使用**Aspose.Cells Java for Jython**进行文档追加。这里您可以查看示例代码

**Jython代码**

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
## **下载运行代码**
从以下任何社交编码网站下载**追加文档（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
