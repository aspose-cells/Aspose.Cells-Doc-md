---
title: ワークブックの読み込み中に定義された名前をフィルター処理する
type: docs
weight: 50
url: /ja/java/filter-defined-names-while-loading-workbook/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用すると、ワークブック内に存在する定義済みの名前をフィルター処理または削除できます。使ってください[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)定義された名前をロードして ~ を使用する[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)ワークブックのロード中にそれらを削除します。定義された名前を削除すると、ワークブック内の数式が壊れる可能性があることに注意してください。

## **ワークブックの読み込み中に定義された名前をフィルター処理する**

次のサンプル コードは、[サンプル Excel ファイル](61767873.xlsx)定義された名前を含むセルC1に数式があります。*=SUM(MyName1, MyName2)*.以来、私たちは〜を使用しています[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)ワークブックの読み込み中に定義された名前を削除するには、セル C1 の数式[出力エクセルファイル](61767872.xlsx)壊れて、あなたが見る*#NAME?*代わりは。サンプル Excel ファイルに対するコードの効果を示す次のスクリーンショットを参照してください。

![todo:画像_代替_文章](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
