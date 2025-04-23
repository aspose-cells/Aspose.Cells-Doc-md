---
title: 複雑な基準を満たすレコードを表示するためにMicrosoft Excelの高度なフィルタを適用する方法
type: docs
weight: 190
url: /ja/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **可能な使用シナリオ**
Microsoft Excelでは、ワークシートデータに*高度なフィルタ*を適用して複雑な基準を満たすレコードを表示できます。このスクリーンショットに示すように、Microsoft Excelでは*データ > 高度なフィルタ*のコマンドを使用して高度なフィルタを適用できます。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cellsは、[Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter-boolean-java.lang.String-java.lang.String-java.lang.String-boolean-)メソッドを使用してアドバンスドフィルタを適用することも可能です。Microsoft Excelと同様に、このメソッドは以下のパラメータを受け入れます。

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
次のサンプルコードは、[Sample Excel File](48496702.xlsx) に高度なフィルタを適用し、[Output Excel File](48496705.xlsx) を生成しています。スクリーンショットでは、サンプルExcelファイルと出力Excelファイルを比較したものが表示されています。スクリーンショットの内側を見ると、出力Excelファイル内でデータが複雑な条件に従ってフィルタリングされているのがわかります。

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
{{< app/cells/assistant language="java" >}}
