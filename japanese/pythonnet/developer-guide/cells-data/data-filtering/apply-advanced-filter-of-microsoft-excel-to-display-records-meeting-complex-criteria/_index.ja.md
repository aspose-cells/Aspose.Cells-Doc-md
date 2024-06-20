---
title: 複雑な基準を満たすレコードを表示するためにMicrosoft Excelの高度なフィルタを適用する方法
type: docs
weight: 280
url: /ja/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aspose.Cells for Python via .NET APIを使用して、Microsoft Excelの高度なフィルタを適用して複雑な基準を満たすレコードを表示する方法を学びます。
keywords: Python Excelライブラリ、Python高度なフィルタの適用、Pythonセット高度なフィルタ、Python追加高度フィルタ、Python高度なフィルタの作成、Pythonを使用した範囲への高度なフィルタの追加方法。
---

## **可能な使用シナリオ**

Microsoft Excelでは、ワークシートデータに*高度なフィルタ*を適用して複雑な基準を満たすレコードを表示できます。このスクリーンショットに示すように、Microsoft Excelでは*データ > 高度なフィルタ*のコマンドを使用して高度なフィルタを適用できます。

![todo:image_alt_text](1.png)

Aspose.Cells for Python via .NETでも、[**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool)メソッドを使用して高度なフィルタを適用できます。Microsoft Excelと同様に、次のパラメータを受け入れます。

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

![todo:image_alt_text](2.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
