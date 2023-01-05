---
title: Excelファイルに格納する有効数字を指定する
type: docs
weight: 20
url: /ja/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **考えられる使用シナリオ**

デフォルトでは、Aspose.Cells は有効数字 15 桁のみを格納する Excel アプリケーションとは異なり、スプレッドシートに double 値の有効数字 17 桁を格納します。この場合、Aspose.Cells のデフォルトの動作を変更できます。を使用しながら、有効桁数を 17 から 15 に変更できます。[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)財産。

## **Excelファイルに格納する有効数字を指定する**

次のサンプル コードは、Aspose.Cells が 15 桁の有効数字を使用するように強制し、Excel ファイル内に double 値を格納します。を確認してください[出力エクセルファイル](23166982.xlsx).拡張子を .zip に変更して解凍すると、Excel ファイル内に有効数字が 15 桁しか格納されていないことがわかります。次のスクリーンショットは、[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)出力 Excel ファイルのプロパティ。

![todo:画像_代替_文章](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
