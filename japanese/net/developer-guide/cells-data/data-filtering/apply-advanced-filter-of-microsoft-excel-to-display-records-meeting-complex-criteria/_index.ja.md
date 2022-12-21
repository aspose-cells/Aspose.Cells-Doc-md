---
title: Microsoft Excel の高度なフィルターを適用して、複雑な基準を満たすレコードを表示する
type: docs
weight: 280
url: /ja/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **考えられる使用シナリオ**

Microsoft エクセルで申し込めます*高度なフィルター*複雑な基準を満たすレコードを表示するには、ワークシート データを使用します。高度なフィルターを Microsoft Excel で適用できます。*データ > 詳細*このスクリーンショットに示すようにコマンドを実行します。

![todo:画像_代替_文章](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells を使用して高度なフィルターを適用することもできます[**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)方法。 Microsoft Excel と同様に、次のパラメーターを受け入れます。

**isFilter**

リストを適切にフィルタリングするかどうかを示します。

**リスト範囲**

リスト範囲。

**基準範囲**

基準範囲。

**コピー先**

データのコピー先の範囲。

**uniqueRecordOnly**

一意の行のみを表示またはコピーします。

## **Microsoft Excel の高度なフィルターを適用して、複雑な基準を満たすレコードを表示する**

次のサンプル コードは、高度なフィルタを[サンプル Excel ファイル](48496692.xlsx)を生成し、[出力 Excel ファイル](48496691.xlsx).スクリーンショットは、比較のために両方のファイルを示しています。スクリーンショットでわかるように、データは複雑な条件に従って出力 Excel ファイル内でフィルター処理されています。

![todo:画像_代替_文章](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
