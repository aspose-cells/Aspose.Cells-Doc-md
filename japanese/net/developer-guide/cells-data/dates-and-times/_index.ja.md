---
title: 日付と時刻を管理する方法
type: docs
weight: 600
url: /ja/net/how-to-manage-dates-and-times/
description: Aspose.Cells for .NET API を通じて日付と時刻を管理する方法を学びましょう。
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **Excelに日付と時刻を保存する方法**
日付と時刻は数値としてセルに保存されます。したがって、日付と時刻を含むセルの値は数値型になります。日付と時刻を指定する数値は、日付 (整数部分) と時刻 (小数部分) のコンポーネントで構成されます。 Cell.DoubleValue プロパティはこの数値を返します。

##  **Aspose.Cellsの日付と時刻を表示する方法**
数値を日付と時刻として表示するには、必要な日付と時刻の形式をセルに適用します。[スタイル.番号](https://reference.aspose.com/cells/net/aspose.cells/style/number/)または[スタイル.カスタム]()財産。 CellValue.DateTimeValue プロパティは、セルに含まれる数値で表される日付と時刻を指定する DateTime オブジェクトを返します。
<br>
<image src="1.png" width="70%" />

##  **Aspose.Cells で 2 つの日付システムを切り替える方法**
MS-Excel では、日付をシリアル値と呼ばれる数値として保存します。シリアル値は、日付システムの最初の日からの経過日数を表す整数です。 Excel では、シリアル値に対して次の日付システムがサポートされています。

1. 1900 年の日付システム。最初の日付は 1900 年 1 月 1 日で、シリアル値は 1 です。最後の日付は 9999 年 12 月 31 日で、シリアル値は 2,958,465 です。この日付システムはデフォルトでワークブックで使用されます。
1.  1904 年の日付システム。最初の日付は 1904 年 1 月 1 日で、シリアル値は 0 です。最後の日付は 9999 年 12 月 31 日で、シリアル値は 2,957,003 です。ワークブックでこの日付システムを使用するには、[Workbook.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/)プロパティを true に設定します。


この例は、同じ日付に異なる日付システムで保存されたシリアル値が異なることを示しています。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
出力結果:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **Aspose.Cells に DateTime 値を設定する方法**
この例では、セル A1 と A2 に DateTime 値を設定し、A1 のカスタム形式と A2 の数値形式を設定して、値の型を出力します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

出力結果:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **Aspose.Cells の DateTime 値を取得する方法**
この例では、セル A1 と A2 に DateTime 値を設定し、A1 のカスタム形式と A2 の数値形式を設定し、2 つのセルの値の型を確認して、DateTime 値と書式設定された文字列を出力します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

出力結果:
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
