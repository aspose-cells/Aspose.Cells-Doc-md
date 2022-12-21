---
title: GridWeb ダブルクリック イベントの操作
type: docs
weight: 80
url: /ja/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb には、次の 3 種類のダブルクリック イベントが含まれています。

- CellDoubleClick は、セルがダブルクリックされたときに発生します。
- ColumnDoubleClick は、列ヘッダーがダブルクリックされたときに発生します。
- RowDoubleClick、行ヘッダーがダブルクリックされたときに発生します。

このトピックでは、Aspose.Cells.GridWeb でダブルクリック イベントを有効にする方法について説明します。また、これらのイベントのイベント ハンドラーの作成についても説明します。

{{% /alert %}} 
## **ダブルクリック イベントの有効化**
GridWeb コントロールの EnableDoubleClickEvent プロパティを true に設定することにより、すべてのタイプのダブルクリック イベントをクライアント側で有効にすることができます。

{{% alert color="primary" %}} 

デフォルトでは、EnableDoubleClickEvent プロパティは false に設定されています。これは、デフォルトではダブルクリック イベントが有効になっていないことを意味します。このようなイベントを実装するには、まず機能を有効にします。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



ダブルクリック イベントを有効にすると、任意のダブルクリック イベントのイベント ハンドラーを作成できます。これらのイベント ハンドラーは、特定のダブルクリック イベントが発生したときに特定のタスクを実行します。
## **ダブルクリック イベントの処理**
Visual Studio でイベント ハンドラーを作成するには:

1. でイベントをダブルクリックします。**イベント**プロパティ ペインに一覧表示されます。

この例では、さまざまなダブルクリック イベントのイベント ハンドラーを実装しました。
### **ダブルクリック Cell**
CellDoubleClick イベントのイベント ハンドラーは、ダブルクリックされたセルの完全な情報を提供する CellEventArgs 型の引数を提供します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **列ヘッダーをダブルクリック**
ColumnDoubleClick イベントのイベント ハンドラーは、ダブルクリックされたヘッダーの列のインデックス番号とその他の情報を提供する RowColumnEventArgs 型の引数を提供します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **行ヘッダーをダブルクリック**
RowDoubleClick イベントのイベント ハンドラーは、ダブルクリックされたヘッダーの行のインデックス番号とその他の関連情報を提供する RowColumnEventArgs 型の引数を提供します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
