---
title: Jython でペインを分割する
type: docs
weight: 140
url: /ja/java/split-panes-in-jython/
---
## **Aspose.Cells - ペインの分割**
を使用してドキュメントを追加するには**Aspose.Cells Jython の場合は Java**.ここでサンプルコードを見ることができます。

**Jython コード**

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
## **実行中のコードをダウンロード**
ダウンロード**添付書類 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SplitPanes.py)
