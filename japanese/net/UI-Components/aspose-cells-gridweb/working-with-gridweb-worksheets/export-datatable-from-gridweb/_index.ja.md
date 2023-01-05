---
title: GridWeb から DataTable をエクスポートする
type: docs
weight: 70
url: /ja/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[DataView を GridWeb にインポートする](/cells/ja/net/import-dataview-to-gridweb/)DataView の内容を Aspose.Cells.GridWeb コントロールにインポートする方法について説明しました。このトピックでは、Aspose.Cells.GridWeb コントロールから DataTable へのデータのエクスポートについて説明します。

{{% /alert %}} 
## **ワークシート データのエクスポート**
### **特定の DataTable へ**
ワークシート データを特定の DataTable オブジェクトにエクスポートするには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 特定の DataTable オブジェクトを作成します。
1. 選択したセルのデータを指定した DataTable オブジェクトにエクスポートします。

次の例では、4 つの列を持つ特定の DataTable オブジェクトを作成します。ワークシート データは、ワークシートに表示されているすべての行と列を含む最初のセルから、既に作成されている DataTable オブジェクトにエクスポートされます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **新しいデータテーブルへ**
場合によっては、DataTable オブジェクトを作成するのではなく、単にワークシート データを新しい DataTable オブジェクトにエクスポートする必要がある場合があります。

次の例では、Export メソッドの使用方法を示す別の方法を試しています。アクティブなワークシートの参照を取得し、そのワークシートの完全なデータを新しい DataTable オブジェクトにエクスポートします。 DataTable オブジェクトは、任意の方法で使用できるようになりました。たとえば、DataTable オブジェクトを GridView にバインドしてデータを表示することができます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
