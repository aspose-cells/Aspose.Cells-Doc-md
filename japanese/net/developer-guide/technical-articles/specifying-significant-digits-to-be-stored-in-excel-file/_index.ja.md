---
title: Excelファイルに保存する有効桁数を指定する
type: docs
weight: 30
url: /ja/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **可能な使用シナリオ**

デフォルトでは、Aspose.CellsはExcelファイル内の倍精度値の17桁の有効桁数を保存しますが、MS-Excelは15桁の有効桁数のみを保存します。[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) プロパティを使用して、Aspose.Cellsのデフォルトの動作を17桁の有効桁数から15桁の有効桁数に変更できます。

## **Excelファイルに保存する有効桁数を指定**

以下のサンプルコードは、Excelファイル内の倍精度値を保存する際にAspose.Cellsに15桁の有効桁数を使用するよう指定しています。[出力エクセルファイル](22774105.xlsx)をご確認ください。その拡張子を .zip に変更して解凍すると、Excelファイル内には15桁の有効桁数のみが保存されていることがわかります。以下のスクリーンショットは、[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) プロパティの出力エクセルファイルへの影響を説明しています。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
{{< app/cells/assistant language="csharp" >}}
