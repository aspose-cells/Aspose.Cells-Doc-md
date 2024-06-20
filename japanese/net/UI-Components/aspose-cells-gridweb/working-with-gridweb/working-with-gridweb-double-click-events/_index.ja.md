---
title: GridWeb ダブルクリックイベントの動作
type: docs
weight: 80
url: /ja/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb,ダブルクリック,クリックイベント,イベント
description: この記事では、GridWeb でのダブルクリックイベントの使用方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb には、3種類のダブルクリックイベントが含まれています:

- CellDoubleClick: セルがダブルクリックされたときに発生します。
- ColumnDoubleClick: 列ヘッダがダブルクリックされたときに発生します。
- RowDoubleClick: 行ヘッダがダブルクリックされたときに発生します。

このトピックでは、Aspose.Cells.GridWeb でのダブルクリックイベントの有効化と、これらのイベントのためのイベントハンドラの作成について説明します。

{{% /alert %}} 
## **ダブルクリックイベントの有効化**
すべての種類のダブルクリックイベントをクライアント側で有効にするには、GridWeb コントロールの EnableDoubleClickEvent プロパティを true に設定します。

{{% alert color="primary" %}} 

デフォルトでは、EnableDoubleClickEvent プロパティは false に設定されています。 これは、ダブルクリックイベントがデフォルトで有効になっていないことを意味します。 このようなイベントを実装するには、まずこの機能を有効にする必要があります。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



ダブルクリックイベントが有効になると、任意のダブルクリックイベントのためのイベントハンドラを作成できます。 これらのイベントハンドラは、特定のダブルクリックイベントが発生したときに特定のタスクを実行します。
## **ダブルクリックイベントの処理**
Visual Studio でイベントハンドラを作成するには:

1. プロパティペインの **イベント** リストでイベントをダブルクリックします。

この例では、さまざまなダブルクリックイベントのためのイベントハンドラを実装しました。
### **セルのダブルクリック**
CellDoubleClick イベントのイベントハンドラは、CellEventArgs タイプの引数を提供します。 これにより、ダブルクリックされたセルの完全な情報が提供されます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **列ヘッダのダブルクリック**
ColumnDoubleClick イベントのイベントハンドラは、ColumnDoubleClick イベントのイベントハンドラは、RowColumnEventArgs タイプの引数を提供し、ダブルクリックされたヘッダの列のインデックス番号などの情報が提供されます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **行ヘッダのダブルクリック**
RowDoubleClick イベントのイベントハンドラは、RowColumnEventArgs タイプの引数を提供し、ダブルクリックされたヘッダの行のインデックス番号などの情報が提供されます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
