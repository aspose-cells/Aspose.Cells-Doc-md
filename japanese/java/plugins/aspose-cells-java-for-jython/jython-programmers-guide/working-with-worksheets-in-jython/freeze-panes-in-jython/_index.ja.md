---
title: Jython でペインをフリーズする
type: docs
weight: 60
url: /ja/java/freeze-panes-in-jython/
---
## **Aspose.Cells - フリーズペイン**
を使用してドキュメントを追加するには**Aspose.Cells Jython の場合は Java**.ここでサンプルコードを見ることができます。

**Jython コード**

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
## **実行中のコードをダウンロード**
ダウンロード**添付書類 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/FreezePanes.py)
