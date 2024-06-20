---
title: Jythonで行と列を自動調整する
type: docs
weight: 20
url: /ja/java/autofit-rows-and-columns-in-jython/
---

## **Aspose.Cells - 行と列の自動調整**
**Aspose.Cells Java for Jython**を使用してドキュメントを追加します。ここでは例を示します。

**Jythonコード**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

class RowsAndColumns:

    def __init__(self):



        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



        # Auto Fit Row

        self.autofit_row()

        # Auto Fit Column

        self.autofit_column() 



    def autofit_row(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Auto-fitting the 3rd row of the worksheet

        worksheet.autoFitRow(2)

        # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

        # cells (from 1st to 9th column) within the row

        #worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Autofit Row.xls")

        print "Autofit Row Successfully." 



    def autofit_column(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Auto-fitting the 4th column of the worksheet

        worksheet.autoFitColumn(3)

        # Auto-fitting the 4th column of the worksheet based on the contents in a range of

        # cells (from 1st to 9th row) within the column

        #worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Autofit Column.xls")

        print "Autofit Column Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に示すいずれかのソーシャルコーディングサイトから**Aspose.Cellsのドキュメントを追加する**をダウンロード:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
