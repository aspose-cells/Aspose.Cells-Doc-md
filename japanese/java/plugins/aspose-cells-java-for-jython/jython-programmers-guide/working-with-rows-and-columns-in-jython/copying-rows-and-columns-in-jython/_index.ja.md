---
title: Jython での行と列のコピー
type: docs
weight: 30
url: /ja/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - 行と列のコピー**
を使用してドキュメントを追加するには**Aspose.Cells Jython の場合は Java**.ここでサンプルコードを見ることができます。

**Jython コード**

{{< highlight "java" >}}

from aspose-cells import 設定

com.aspose.cells インポート ワークブックから

クラス RowsAndColumns:

デフォルト__初期化__（自己）：



 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



 # 行のコピー

self.copy_rows()

 # 列のコピー

self.copy_columns()



 def copy_rows (dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Excel ファイル パスによる Workbook オブジェクトのインスタンス化

ワークブック = ワークブック (dataDir + 'Book1.xls')

 Excel ファイルの最初のワークシートにアクセスする

ワークシート = workbook.getWorksheets().get(0)

 # データ、フォーマット、画像、および描画オブジェクトを含む 2 行目をコピーします

 ワークシートの 12 行目に。

 worksheet.getCells().copyRow(worksheet.getCells(),1,11)

 # 変更した Excel ファイルをデフォルト (Excel 2003) 形式で保存

workbook.save(dataDir + "Copy Rows.xls")

 print "行のコピーに成功しました。"



 def copy_columns (dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Excel ファイル パスによる Workbook オブジェクトのインスタンス化

ワークブック = ワークブック()

 Excel ファイルの最初のワークシートにアクセスする

ワークシート = workbook.getWorksheets().get(0)

 # データをヘッダー行に入れる (A1:A4)

私は= 0

私がいる間< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**添付書類 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
