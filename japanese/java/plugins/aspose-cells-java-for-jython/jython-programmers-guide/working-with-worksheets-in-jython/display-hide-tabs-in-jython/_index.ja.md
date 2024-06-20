---
title: Jythonでタブを表示/非表示
type: docs
weight: 50
url: /ja/java/display-hide-tabs-in-jython/
---

## **Aspose.Cells - タブを表示または非表示にする**
**Aspose.Cells Java for Jython**を使用してドキュメントを追加します。ここでは例を示します。

**Jythonコード**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideTabs:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideTabs/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Hiding the tabs of the Excel file

        workbook.getSettings().setShowTabs(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Tabs are now hidden, please check the output file."

if __name__ == '__main__':        

    DisplayHideTabs()

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に示すいずれかのソーシャルコーディングサイトから**Aspose.Cellsのドキュメントを追加する**をダウンロード:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideTabs.py)
