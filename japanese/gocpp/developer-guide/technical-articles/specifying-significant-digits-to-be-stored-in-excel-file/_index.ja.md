---
title: GolangとC++でExcelファイルに保存される有効桁数を指定
linktitle: 有意義な桁数の指定
type: docs
weight: 30
url: /ja/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: GolangとC++を使用したAspose.CellsでExcelファイルに保存される有効桁数の指定方法を学ぶ
---

## **可能な使用シナリオ**

デフォルトでは、Aspose.CellsはExcelファイル内に64ビットの値の有効数字17桁を格納します。これは、MS-Excelが有効数字15桁しか格納しないのとは異なります。Aspose.Cellsの既定の動作を、[**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) プロパティを使用して15桁に変更できます。

## **Excelファイルに保存する有効桁数を指定**

以下のサンプルコードは、Aspose.CellsがExcelファイル内に64ビットの値を格納する際に15桁の有効数字を使用するように強制します。[出力Excelファイル](22774105.xlsx)を確認してください。拡張子を.zipに変更して解凍すると、Excelファイル内に15桁だけが格納されていることがわかります。以下のスクリーンショットは、[**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) プロパティが出力Excelファイルに与える影響を示しています。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
