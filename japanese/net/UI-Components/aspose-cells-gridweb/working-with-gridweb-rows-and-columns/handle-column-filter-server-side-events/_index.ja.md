---
title: 列フィルター サーバー側イベントの処理
type: docs
weight: 90
url: /ja/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

データ フィルタリングは、特定の基準に基づいてデータをフィルタリングできる、おそらく最も広く使用されている Excel 機能です。フィルタリングされたデータは、基準を満たさない行を非表示にすることで、条件を満たす行のみを表示します。
Aspose.Cells.GridWeb コンポーネントは、そのインターフェイスを使用してデータ フィルタリングを実行する機能を提供します。機能を拡張するために、Aspose.Cells.GridWeb コンポーネントは、GridWeb UI を介して実行されるフィルタリング メカニズムへのコールバックとして機能する 2 つのイベントも提供します。

{{% /alert %}} 
## **列フィルター適用時のサーバー側イベントの処理**
以下に詳述するように、2 つの主要なイベントがあります。

1. OnBeforeColumnFilter: フィルターが列に適用される前に発生します。
1. OnAfterColumnFilter: フィルターが列に適用された後に発生します。

前述のイベントを追加して割り当てる Aspose.Cells.GridWeb コンポーネントの ASPX スクリプトを次に示します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



これらのイベントを使用して、フィルターを適用する必要がある列のインデックスや値など、フィルター処理に関する有用な情報を取得できます。以下は、OnBeforeColumnFilter イベントを使用して、ユーザーがフィルタリングのために GridWeb UI で選択した列インデックスと値を取得する方法を示すスニペットです。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


一方、フィルタが適用された後にフィルタリングされた行の数を取得する必要がある場合は、以下に示すように OnAfterColumnFilter イベントを使用できます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

全ての紹介をチェック[GridWeb イベントの操作](/cells/ja/net/working-with-gridweb-events/)これらのイベントを処理する方法の詳細とともに。

{{% /alert %}}
