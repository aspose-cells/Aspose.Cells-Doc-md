---
title: オートフィルタを更新した後のすべての非表示行のインデックスを取得する
type: docs
weight: 320
url: /ja/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aspose.Cells for Python via .NET API を使用して AutoFilter を更新した後、非表示のすべての行インデックスを取得する方法を学びます。
keywords: Python Excel ライブラリ、Python AutoFilter を更新した後に非表示のすべての行インデックスを取得、Python AutoFilter を更新した後に非表示のすべての行インデックスを取得、Python AutoFilter を更新した後に非表示のすべての行インデックスを取得
---

## **可能な使用シナリオ**

ワークシートのセルにオートフィルタを適用すると、いくつかの行が自動的に非表示になります。 ただし、自動フィルタによって非表示にされている行と、Excel エンドユーザーによって手動で非表示にされている行の区別が困難な場合があります。 そのような場合、Aspose.Cells for Python via .NET は [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) メソッドを使用してこの問題に対処します。 このメソッドは、自動フィルタによって非表示にされており、Excel エンドユーザーによって手動で非表示にされていない行の行インデックスを返します。

## **オートフィルタの更新後の非表示行インデックスの取得**

以下のサンプルコードでは、Excel エンドユーザーによって手動で非表示にされた行がいくつか含まれる [サンプル Excel ファイル](64716909.xlsx) を読み込みます。 その後、[**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) メソッドを使用してオートフィルタを適用し、更新します。 このメソッドは、オートフィルタによって非表示にされたすべての行の行インデックスを取得し、非表示の行のインデックスをセル名と値とともにコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

## **コンソール出力**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
