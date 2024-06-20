---
title: 範囲のアドレス、セル数、オフセット、全列、および全行を取得する
type: docs
weight: 330
url: /ja/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して範囲のアドレス、セル数、オフセット、範囲の列全体および行全体を取得する方法について説明します。
keywords: Python Excelライブラリ、Pythonで範囲のアドレス、セル数、オフセット、範囲の列全体および行全体を取得する方法
---

## **可能な使用シナリオ**
Aspose.Cells for Python via .NETは、Excel範囲で簡単に作業できるようにユーザーを支援するさまざまなユーティリティメソッドを持つRangeオブジェクトを提供しています。この記事では、Rangeオブジェクトの次のメソッドまたはプロパティの使用法について説明します。

- **address**

範囲のアドレスを取得します。

- **cell_count**

範囲内のすべてのセル数を取得します。

- **get_offset**

オフセットによって範囲を取得します。

- **entire_column**

指定された範囲を含む列全体を表すRangeオブジェクトを取得します。

- **entire_row**

指定された範囲を含む行全体を表すRangeオブジェクトを取得します。

## **範囲のアドレス、セル数、オフセット、全列および全行を取得する**
以下のサンプルコードは、上記で説明したメソッドとプロパティの使用方法を説明します。参考のために、以下に示すコードのコンソール出力をご覧ください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.py" >}}
## **コンソール出力**
{{< highlight java >}}

 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
