---
title: オートフィルターを更新した後にすべての非表示の行インデックスを取得する
type: docs
weight: 320
url: /ja/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **考えられる使用シナリオ**

ワークシートのセルに自動フィルターを適用すると、一部の行が自動的に非表示になります。ただし、一部の行が Excel エンド ユーザーによって手動で既に非表示にされており、それらが自動フィルターによって非表示にされていない場合があります。したがって、どの行が自動フィルターによって非表示にされ、どの行が Excel エンド ユーザーによって手動で非表示にされているかを知ることが難しくなります。 Aspose.Cells は int[] を使用してこの問題を処理します[**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)方法。このメソッドは、自動フィルターによって非表示になり、Excel エンド ユーザーによって手動で非表示にされたすべての行の行インデックスを返します。

## **オートフィルターを更新した後にすべての非表示の行インデックスを取得する**

をロードする次のサンプル コードを参照してください。[サンプル Excel ファイル](64716909.xlsx)これには、Excel エンド ユーザーによって手動で非表示にされた行が含まれています。コードは自動フィルターを適用し、int[] を使用して更新します[**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)自動フィルターによってすべての非表示行の行インデックスを返すメソッド。次に、非表示の行のインデックスをセルの名前と値とともにコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

## **コンソール出力**

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
