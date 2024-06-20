---
title: 範囲のアドレス、セル数、オフセット、全列、および全行を取得する
type: docs
weight: 330
url: /ja/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **可能な使用シナリオ**
Aspose.Cellsは、Excelの範囲を簡単に扱うためのさまざまなユーティリティメソッドを持つRangeオブジェクトを提供します。この記事では、Rangeオブジェクトの次のメソッドやプロパティの使用方法を説明します。

- **アドレス**

範囲のアドレスを取得します。

- **セル数**

範囲内のすべてのセル数を取得します。

- **オフセット**

オフセットによって範囲を取得します。

- **全列**

指定された範囲を含む列全体を表すRangeオブジェクトを取得します。

- **全行**

指定された範囲を含む行全体を表すRangeオブジェクトを取得します。
## **範囲のアドレス、セル数、オフセット、全列および全行を取得する**
以下のサンプルコードは、上記で説明したメソッドとプロパティの使用方法を説明します。参考のために、以下に示すコードのコンソール出力をご覧ください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.cs" >}}
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
