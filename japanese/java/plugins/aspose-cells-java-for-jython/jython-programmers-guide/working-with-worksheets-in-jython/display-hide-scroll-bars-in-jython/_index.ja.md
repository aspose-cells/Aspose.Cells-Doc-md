---
title: Jython でスクロール バーを非表示にする
type: docs
weight: 40
url: /ja/java/display-hide-scroll-bars-in-jython/
---
## **Aspose.Cells - 非表示スクロール バーの表示**
を使用してドキュメントを追加するには**Aspose.Cells Jython の場合は Java**.ここでサンプルコードを見ることができます。

**Jython コード**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideScrollBars:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideScrollBars/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Hiding the vertical scroll bar of the Excel file

        workbook.getSettings().setVScrollBarVisible(False)

        #Hiding the horizontal scroll bar of the Excel file

        workbook.getSettings().setHScrollBarVisible(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Scroll bars are now hidden, please check the output document."



if __name__ == '__main__':        

    DisplayHideScrollBars()

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**添付書類 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideScrollBars.py)
