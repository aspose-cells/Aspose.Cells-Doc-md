---
title: 日付と時間の管理方法
type: docs
weight: 600
url: /ja/python-net/how-to-manage-dates-and-times/
description: Aspose.Cells for .NET APIを使用して日付と時間の管理方法を学ぶ。
keywords: 日付と時間の管理方法、1900年の日付システム、1904年の日付システム、日付と時間の設定、日付と時間の取得、日付と時間の管理、Excelでの日付と時間の格納、セルでの日付と時間の表示。
---

## **Excelでの日付と時間の格納方法**
日付と時間はセルに数値として格納されます。したがって、日付と時間を含むセルの値は数値型です。日付と時間を指定する数値は、日付（整数部）と時間（小数部）のコンポーネントで構成されます。Cell.DoubleValueプロパティは、この数値を返します。

## **Aspose.Cellsでの日付と時間の表示方法**
番号を日付と時間として表示するには、セルに必要な日時フォーマットを適用します。 [Style.number](https://reference.aspose.com/cells/python-net/aspose.cells/style/number/) または [Style.Custom]() プロパティを使用します。CellValue.DateTimeValue プロパティは、セルに含まれる数字が表す日時を示す DateTime オブジェクトを返します。
<br>
<image src="1.png" width="70%" />

## **Aspose.Cellsでの2つの日付システムの切り替え方法**
MS-Excelは、日付をシリアル値と呼ばれる数値として格納します。シリアル値は、日付システムの最初の日から経過した日数を示す整数です。Excelは、シリアル値のために以下の日付システムをサポートしています。

1. 1900年の日付システム。最初の日付は1900年1月1日で、そのシリアル値は1です。最後の日付は9999年12月31日で、そのシリアル値は2,958,465です。この日付システムはワークブックのデフォルトで使用されます。
1. 1904日付システム。最初の日付は1904年1月1日で、そのシリアル値は0です。最後の日付は9999年12月31日で、そのシリアル値は2,957,003です。この日付システムをWorkbookで使用するには、[**Workbook.settings.date1904**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/date1904/) プロパティをtrueに設定します。


この例は、異なる日付システムで同じ日付に格納されたシリアル値が異なることを示しています。
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Datetime-1904.py" >}}
出力結果：
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Aspose.Cellsでの日時値の設定方法**
この例では、セルA1とA2に日時値を設定し、A1のカスタム形式とA2の数値形式を設定し、値のタイプを出力します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Set-Datetime.py" >}}

出力結果：
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Aspose.Cellsでの日時値の取得方法**
この例では、セルA1とA2に日時値を設定し、A1のカスタム形式とA2の数値形式を設定し、2つのセルの値のタイプをチェックし、日時値とフォーマットされた文字列を出力します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Get-Datetime.py" >}}

出力結果：
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
