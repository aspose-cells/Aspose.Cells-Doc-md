---
title: Jythonでグリッド線を表示/非表示
type: docs
weight: 30
url: /ja/java/display-hide-gridlines-in-jython/
---

## **Aspose.Cells - グリッド線を表示/非表示**
**Aspose.Cells Java for Jython**を使用してドキュメントを追加します。ここでは例を示します。

**Jythonコード**

{{< highlight java >}}

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
## **ランニングコードのダウンロード**
以下に示すいずれかのソーシャルコーディングサイトから**Aspose.Cellsのドキュメントを追加する**をダウンロード:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideGridlines.py)
