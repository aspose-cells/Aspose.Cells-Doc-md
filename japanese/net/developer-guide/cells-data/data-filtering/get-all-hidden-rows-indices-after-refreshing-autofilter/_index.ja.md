---
title: オートフィルターを更新した後にすべての非表示の行インデックスを取得する
type: docs
weight: 320
url: /ja/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: オートフィルターを更新した後に、Aspose.Cells for .NET API を使用してすべての非表示の行インデックスを取得する方法を学習します。
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **考えられる使用シナリオ**

ワークシートのセルに自動フィルターを適用すると、一部の行が自動的に非表示になります。ただし、行の一部がすでに Excel エンド ユーザーによって手動で非表示になっており、自動フィルターによって非表示になっていない場合もあります。したがって、どの行が自動フィルターによって非表示になっているのか、どの行が Excel エンド ユーザーによって手動で非表示になっているのかを知ることが困難になります。 Aspose.Cells は int[] を使用してこの問題に対処しています。[**AutoFilter.Refresh(bool HideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)方法。このメソッドは、Excel エンド ユーザーが手動で非表示にしたのではなく、自動フィルターによって非表示になったすべての行の行インデックスを返します。

##  **オートフィルターを更新した後にすべての非表示の行インデックスを取得する**

をロードする次のサンプルコードを参照してください。[サンプル Excel ファイル](64716909.xlsx)これには、Excel エンド ユーザーが手動で非表示にした行の一部が含まれています。このコードは自動フィルターを適用し、int[] を使用してフィルターを更新します。[**AutoFilter.Refresh(bool HideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)自動フィルターによって非表示になっているすべての行の行インデックスを返すメソッド。次に、非表示の行のインデックスをセル名と値とともにコンソールに出力します。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **コンソール出力**

{{< highlight "java" >}}

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
