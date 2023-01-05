---
title: ワークブックの読み込み中に定義された名前をフィルター処理する
type: docs
weight: 50
url: /ja/net/filter-defined-names-while-loading-workbook/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用すると、ワークブック内に存在する定義済みの名前をフィルター処理または削除できます。使ってください[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)定義された名前をロードして ~ を使用する[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)ワークブックのロード中にそれらを削除します。定義された名前を削除すると、ワークブック内の数式が壊れる可能性があることに注意してください。

## **ワークブックの読み込み中に定義された名前をフィルター処理する**

次のサンプル コードは、[サンプル Excel ファイル](61767860.xlsx)セルに数式がある**C1**定義された名前を含む*=SUM(MyName1, MyName2)*～を使っているので[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)ワークブックの読み込み中に定義された名前を削除するには、セル C1 の数式[出力エクセルファイル](61767861.xlsx)壊れて、あなたが見る*#NAME?*代わりは。サンプル Excel ファイルに対するコードの効果を示す次のスクリーンショットを参照してください。

![todo:画像_代替_文章](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
