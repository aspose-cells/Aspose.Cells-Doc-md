---
title: 共有数式の最大行を指定する
type: docs
weight: 40
url: /ja/java/specify-maximum-rows-of-shared-formula/
---
## **考えられる使用シナリオ**

共有数式のデフォルトの最大行数は 64 です。これは、1000 など、任意の数にすることができます。共有数式のパフォーマンスは、行数によって異なります。したがって、Aspose.Cells は[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)共有数式の最大行を指定するために使用できるプロパティ。次のスクリーンショットに示すように、共有数式の合計行がそれより多い場合、共有数式は複数の共有数式に分割されます。

![todo:画像_代替_文章](specify-maximum-rows-of-shared-formula_1.png)

## **共有数式の最大行を指定する**

次のサンプル コードは、[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)財産。共有数式の最大行数を 5 に設定し、共有数式をセル D1 に 100 行追加して、[出力エクセルファイル](61767869.xlsx).出力されたExcelファイルの内容を抽出して確認すると、*sheet1.xml*、上記のスクリーンショットで強調表示されているように、共有数式が 5 行ごとに分割されていることがわかります。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
