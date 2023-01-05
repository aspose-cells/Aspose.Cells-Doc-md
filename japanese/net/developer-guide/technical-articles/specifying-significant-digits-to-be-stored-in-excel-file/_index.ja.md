---
title: Excelファイルに格納する有効数字を指定する
type: docs
weight: 30
url: /ja/net/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **考えられる使用シナリオ**

デフォルトでは、Aspose.Cells は、有効桁数 15 桁のみを格納する MS-Excel とは異なり、Excel ファイル内に有効桁数 17 桁の double 値を格納します。を使用して、Aspose.Cells のデフォルトの動作を 17 桁から 15 桁に変更できます。[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)財産。

## **Excelファイルに格納する有効数字を指定する**

次のサンプル コードは、Aspose.Cells が 15 桁の有効数字を使用するように強制し、Excel ファイル内に double 値を格納します。を確認してください[出力エクセルファイル](22774105.xlsx).拡張子を .zip に変更して解凍すると、Excel ファイル内に有効数字が 15 桁しか格納されていないことがわかります。次のスクリーンショットは、[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)出力 Excel ファイルのプロパティ。

![todo:画像_代替_文章](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
