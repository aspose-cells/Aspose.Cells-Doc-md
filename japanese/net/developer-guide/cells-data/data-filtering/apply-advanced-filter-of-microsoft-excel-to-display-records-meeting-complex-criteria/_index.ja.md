---
title: Microsoft Excel の高度なフィルターを適用して、複雑な基準を満たすレコードを表示する
type: docs
weight: 280
url: /ja/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Microsoft Excel の高度なフィルターを適用して、Aspose.Cells for .NET API を使用して複雑な条件を満たすレコードを表示する方法を説明します。
keywords: Apply Advanced Filter, Set Advanced Filter, Add Advanced Filter, Create Advanced Filter, How to add Advanced Filter to a range 
---
##  **考えられる使用シナリオ**

 Microsoft Excelで申請できます*高度なフィルター*ワークシート データに基づいて、複雑な基準を満たすレコードを表示します。 Microsoft Excel で高度なフィルターを適用できます。*データ > 詳細*このスクリーンショットに示すように、コマンドを実行します。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells を使用すると、高度なフィルターを適用することもできます。[**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)方法。 Microsoft Excel と同様に、次のパラメーターを受け入れます。

**isFilter**

リストを適切にフィルタリングするかどうかを示します。

**リスト範囲**

リスト範囲。

**基準範囲**

基準の範囲です。

**コピー先**

データのコピー先の範囲。

**固有のレコードのみ**

一意の行のみを表示またはコピーします。

##  **Microsoft Excel の高度なフィルターを適用して、複雑な基準を満たすレコードを表示する**

次のサンプル コードでは、高度なフィルターを適用します。[サンプル Excel ファイル](48496692.xlsx)そして、[Excelファイルの出力](48496691.xlsx)。スクリーンショットには、比較のために両方のファイルが示されています。スクリーンショット内にあるように、出力 Excel ファイル内でデータが複雑な基準に従ってフィルター処理されています。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
