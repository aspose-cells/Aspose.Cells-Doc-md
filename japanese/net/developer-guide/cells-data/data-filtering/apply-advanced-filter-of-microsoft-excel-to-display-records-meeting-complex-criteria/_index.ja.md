---
title: 複雑な基準を満たすレコードを表示するためにMicrosoft Excelの高度なフィルタを適用する方法
type: docs
weight: 280
url: /ja/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Microsoft Excelの高度なフィルターを使用して、複雑な基準を満たすレコードを表示するためにAspose.Cells for .NET APIを使用する方法について学びます。
keywords: 高度なフィルターを適用し、高度なフィルターを設定し、高度なフィルターを追加し、高度なフィルターを作成し、範囲に高度なフィルターを追加する方法 
---

## **可能な使用シナリオ**

Microsoft Excelでは、ワークシートデータに*高度なフィルタ*を適用して複雑な基準を満たすレコードを表示できます。このスクリーンショットに示すように、Microsoft Excelでは*データ > 高度なフィルタ*のコマンドを使用して高度なフィルタを適用できます。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cellsでは、[**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)メソッドを使用してAdvanced Filterを適用することもできます。Microsoft Excelと同様に、以下のパラメーターを受け入れます。

**isFilter**

リストをその場でフィルタ処理するかどうかを示します。

**listRange**

リストの範囲。

**criteriaRange**

基準の範囲。

**copyTo**

データをコピーする範囲。

**uniqueRecordOnly**

唯一の行を表示またはコピーします。

## **複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用**

次のサンプルコードは、[サンプルエクセルファイル](48496692.xlsx)に高度なフィルタを適用し、[出力エクセルファイル](48496691.xlsx)を生成します。スクリーンショットでは、両方のファイルが比較のために表示されています。スクリーンショット内でわかるように、出力エクセルファイル内でデータが複雑な基準に従ってフィルタ処理されています。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
