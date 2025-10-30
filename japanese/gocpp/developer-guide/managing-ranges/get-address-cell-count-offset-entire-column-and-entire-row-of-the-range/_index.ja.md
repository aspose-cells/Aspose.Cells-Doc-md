---
title: Golango経由で範囲のアドレス、セル数、オフセット、列全体、行全体を取得
linktitle: 範囲のアドレス、セル数、オフセット、全列、および全行の取得方法を学習します。
type: docs
weight: 330
url: /ja/go-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: 範囲のアドレス、セル数、オフセット、列全体、行全体を取得する方法をAspose.Cells for C++で学びます。
---

## **可能な使用シナリオ**
Aspose.Cellsは`Range`オブジェクトを提供し、便利なメソッドを備えています。このオブジェクトの以下のメソッドやプロパティの使用例を示します。

- **アドレス**

  範囲のアドレスを取得します。

- **セル数**

  範囲内のセルの合計数を取得します。

- **オフセット**

  オフセットによる範囲を取得します。

- **全列**

  指定した範囲を含む列（または列群）全体を表す`Range`オブジェクトを取得します。

- **全行**

  指定した範囲を含む行（または行群）全体を表す`Range`オブジェクトを取得します。

## **範囲のアドレス、セル数、オフセット、全列、全行の取得**
上記で説明した方法やプロパティの使用例を示すサンプルコードを下記に掲載します。コードのコンソール出力例も参考のために示します。

## **サンプルコード**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.go" >}}
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
