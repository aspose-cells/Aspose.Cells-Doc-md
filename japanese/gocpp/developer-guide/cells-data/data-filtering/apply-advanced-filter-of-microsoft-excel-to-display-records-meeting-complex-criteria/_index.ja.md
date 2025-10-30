---
title: Golang経由でMicrosoft Excelの高度なフィルタを適用し、複雑な条件を満たすレコードを表示
linktitle: 複雑な基準を満たすレコードを表示するためにMicrosoft Excelの高度なフィルタを適用する方法
type: docs
weight: 280
url: /ja/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aspose.Cells for C++ APIを使用してMicrosoft Excelの高度なフィルターを適用し、複雑な条件に合致するレコードを表示する方法を学びます。
keywords: 高度なフィルターを適用し、高度なフィルターを設定し、高度なフィルターを追加し、高度なフィルターを作成し、範囲に高度なフィルターを追加する方法
---

## **可能な使用シナリオ**

Microsoft Excelでは、複合条件を満たすレコードを表示するためにワークシートデータに *高度なフィルター* を適用できます。Excelの *データ > 詳細設定* コマンドを使ってこのフィルターを適用することができます（スクリーンショット参照）。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells もまた、 [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/) メソッドを使用して高度なフィルターを適用可能です。Microsoft Excelと同様に、以下のパラメータを受け付けます。

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

次のサンプルコードは、[サンプルExcelファイル](48496692.xlsx)に高度なフィルターを適用し、[出力Excelファイル](48496691.xlsx)を生成します。スクリーンショットは両方のファイルを比較表示しています。スクリーンショット内のデータは、複雑な条件に従ってフィルタリングされています。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
