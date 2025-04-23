---
title: Excelファイルに格納する有効桁数の指定
type: docs
weight: 20
url: /ja/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **可能な使用シナリオ**

デフォルトでは、Aspose.Cellsは、Excelアプリケーションが格納する有効桁数の15桁とは異なり、スプレッドシートでの倍精度値の17桁を格納します。この場合、Aspose.Cellsのデフォルトの動作を変更できます。つまり、[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)プロパティを使用して、有効桁数を17桁から15桁に変更できます。

## **Excelファイルに格納する有効桁数の指定**

以下のサンプルコードでは、Aspose.Cellsに15桁の有効桁数を使用して、Excelファイル内の倍精度値を強制します。[出力されたExcelファイル](23166982.xlsx)を確認してください。その拡張子を.zipに変更して解凍すると、Excelファイル内には15桁の有効桁数しか格納されていないことがわかります。以下のスクリーンショットは、[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)プロパティが出力されたExcelファイルに及ぼす影響を説明しています。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
{{< app/cells/assistant language="java" >}}
