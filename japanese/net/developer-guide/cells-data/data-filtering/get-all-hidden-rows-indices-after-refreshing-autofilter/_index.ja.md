---
title: オートフィルタを更新した後のすべての非表示行のインデックスを取得する
type: docs
weight: 320
url: /ja/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aspose.Cells for .NET APIを使用してAutofilterを更新すると、更新後に隠れたすべての行インデックスを取得する方法を学んでください。
keywords: Autofilterを更新後にすべての隠れた行のインデックスを取得する、Autofilterを更新後の隠れた行インデックスを取得する、Autofilterを更新後の隠れた行インデックスを取得する
---

## **可能な使用シナリオ**

ワークシートセルにオートフィルタを適用すると、一部の行が自動的に非表示になります。ただし、Excelエンドユーザーによって手動で非表示にされた行があり、それがオートフィルタによって非表示にされている行かどうかがわかりにくい場合があります。Aspose.Cellsはこの問題を解決するためにint[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)を使用します。このメソッドはオートフィルタによって非表示にされた行の行インデックスを返し、Excelエンドユーザーによって手動で非表示にされた行の行インデックスではありません。

## **オートフィルタの更新後の非表示行インデックスの取得**

[サンプルExcelファイル](64716909.xlsx)を読み込み、Excelエンドユーザーによって手動で非表示にされた行の一部を示しています。コードはオートフィルタを適用し、int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)メソッドを使用して自動フィルタによって非表示にされたすべての行の行インデックスを取得し、非表示にされた行のインデックスとセル名、値をコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
