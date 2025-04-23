---
title: オートフィルタを更新した後のすべての非表示行のインデックスを取得する
type: docs
weight: 240
url: /ja/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **可能な使用シナリオ**

ワークシートのセルにオートフィルターを適用すると、一部の行が自動的に非表示になります。ただし、エンドユーザーが手動で非表示にした場合もあり、それらがオートフィルターによって非表示にされたかどうかはわかりにくいことがあります。Aspose.Cellsは、この問題に対処するためにint[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-)メソッドを使用します。このメソッドは、オートフィルターによって非表示になった行のインデックスをすべて返します。

## **オートフィルタの更新後の非表示行インデックスの取得**

以下のサンプルコードは、[sample Excel file](64716913.xlsx)をロードし、Excelエンドユーザーによって手動で非表示にされた行が含まれています。コードはオートフィルタを適用し、int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-)メソッドを使用してオートフィルタを更新し、オートフィルターによって非表示にされたすべての行のインデックスをコンソールに出力し、セルの名前と値とともに非表示にされた行のインデックスを印刷します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
{{< app/cells/assistant language="java" >}}
