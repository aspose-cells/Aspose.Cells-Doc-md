---
title: 列フィルターサーバーサイドイベントを処理する
type: docs
weight: 90
url: /ja/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: この記事では、GridWeb で列フィルターイベントを処理する方法について紹介します。
---

{{% alert color="primary" %}} 

データフィルタリングは、特定の条件に基づいてデータをフィルタリングできる、おそらく最も広く使用される Excel の機能です。フィルタリングされたデータは、条件を満たす行のみを表示し、条件を満たさない行は非表示にします。
Aspose.Cells.GridWeb コンポーネントは、そのインターフェイスを使用してデータフィルタリングを行う機能を提供します。Aspose.Cells.GridWeb コンポーネントは、GridWeb UI を介したフィルタリング機構へのコールバックとして機能する 2 つのイベントも提供します。

{{% /alert %}} 
## **列フィルターの適用にサーバーサイドイベントを処理する**
以下に詳細が記載されている2つの主要なイベントがあります。

1. OnBeforeColumnFilter：列にフィルタが適用される前に発生します。
1. OnAfterColumnFilter：列にフィルタが適用された後に発生します。

以下はAspose.Cells.GridWebコンポーネントのASPXスクリプトで、上記のイベントを追加および割り当てる方法です。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



これらのイベントは、列インデックスやGridWeb UIでフィルタリング用にユーザーが選択した値など、フィルタリングプロセスに関する有用な情報を取得するために使用できます。以下は、OnBeforeColumnFilterイベントの使用例と、列インデックスおよびフィルタリングのためにユーザーが選択した値を取得するコードスニペットです。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


一方、フィルタが適用された後にフィルタされた行数を取得する必要がある場合は、以下に示すようにOnAfterColumnFilterイベントを使用できます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

これらのイベントの扱い方についての詳細や、すべての[Working with GridWeb Events](/cells/ja/net/aspose-cells-gridweb/working-with-gridweb-events/)に関する導入情報をチェックしてください。

{{% /alert %}}
