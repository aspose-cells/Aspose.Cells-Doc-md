---
title: JythonでワークシートをSVGに変換する
type: docs
weight: 40
url: /ja/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - ワークシートを SVG に変換中**
を使用してドキュメントを追加するには**Aspose.Cells Jython の場合は Java**.ここでサンプルコードを見ることができます。

**Jython コード**

{{< highlight "java" >}}

from aspose-cells import 設定

com.aspose.cells インポート ワークブックから

from com.aspose.cells import ImageFormat

com.aspose.cells から ImageOrPrintOptions をインポート

from com.aspose.cells import SheetRender

from com.aspose.cells import SaveFormat



クラス ConvertingWorksheetToSVG:

デフォルト__初期化__（自己）：

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



 saveFormat = 保存形式

ワークブック = ワークブック(dataDir + "Book1.xls")

 # 各ワークシートを単一ページの svg 形式に変換します。

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(True)

 #各ワークシートをsvg形式に変換

sheetCount = workbook.getWorksheets().getCount()

 #for(i=0; 私は<sheetCount; i++)

        for i in range(sheetCount):



            sheet = workbook.getWorksheets().get(i)

            sr = SheetRender(sheet, imgOptions)

            pageCount = sr.getPageCount()

            #for (k = 0 k < pageCount k++)

            for k in range(pageCount):



                #Output the worksheet into Svg image format

                sr.toImage(k, dataDir + sheet.getName() + ".out.svg")





        # Print message

        print "Excel to SVG conversion completed successfully."



if __name__ == '__main__':        

    ConvertingWorksheetToSVG()

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**添付書類 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
