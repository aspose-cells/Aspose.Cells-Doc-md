---
title: グリッドからのデータのエクスポート
type: docs
weight: 60
url: /ja/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

前のトピックでは、DataTable の内容を Aspose.Cells.GridDesktop コントロールにインポートすることについて説明しましたが、意図的に Aspose.Cells.GridDesktop が逆のプロセスもサポートすることについては言及しませんでした。したがって、このトピックでは、Aspose.Cells.GridDesktop コントロール内のデータを DataTable にエクスポートする方法について説明します。

{{% /alert %}} 
## **グリッド コンテンツのエクスポート**
### **特定の DataTable へのエクスポート**
グリッドの内容を特定の DataTable オブジェクトにエクスポートするには、次の手順に従ってください: Aspose.Cells.GridDesktop コントロールを**形**.

- 必要に応じて特定の DataTable オブジェクトを作成します。
- 選択したデータのエクスポート**ワークシート**指定した DataTable オブジェクトに。

以下の例では、内部に 4 つの列を持つ特定の DataTable オブジェクトを作成しました。最後に、ワークシート データ (69 行 4 列の最初のセルから開始) を、作成済みの DataTable オブジェクトにエクスポートしました。

**例：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **新しい DataTable へのエクスポート**
場合によっては、開発者が独自の DataTable オブジェクトを作成することに関心がなく、ワークシート データを新しい DataTable オブジェクトにエクスポートするだけの単純な必要性がある場合があります。開発者にとっては、ワークシート データをエクスポートするのが最も簡単な方法です。

以下の例では、ExportDataTable メソッドの使用法を説明するために別の方法を試しました。現在アクティブなワークシートの参照を取得し、そのアクティブなワークシートの完全なデータを新しい DataTable オブジェクトにエクスポートしました。現在、この DataTable オブジェクトは、開発者が望むあらゆる方法で使用できます。例として、開発者はこの DataTable オブジェクトを DataGrid にバインドしてデータを表示できます。

**例：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

上記の場合、ワークシートからエクスポートされたデータを含む新しい DataTable オブジェクトを単に返す ExportDataTable メソッドのオーバーロードされたバージョンを使用します。

{{% /alert %}}
