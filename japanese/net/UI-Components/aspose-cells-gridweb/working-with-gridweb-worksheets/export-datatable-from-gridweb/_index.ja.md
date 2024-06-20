---
title: GridWebからDataTableをエクスポート
type: docs
weight: 70
url: /ja/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb、エクスポート
description: この記事では、GridWeb内のデータテーブルをエクスポートする方法について紹介しています。
---

{{% alert color="primary" %}} 

[DataviewをGridWebにインポート](/cells/ja/net/aspose-cells-gridweb/import-dataview-to-gridweb/)では、データビューの内容をAspose.Cells.GridWebコントロールにインポートする方法について説明しています。このトピックでは、Aspose.Cells.GridWebコントロールからデータをDataTableにエクスポートすることについて説明しています。

{{% /alert %}} 
## **ワークシートデータのエクスポート**
### **特定のDataTableに**
ワークシートデータを特定のDataTableオブジェクトにエクスポートするには：

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. 特定のDataTableオブジェクトを作成します。
1. 選択したセルのデータを指定されたDataTableオブジェクトにエクスポートします。

以下の例では、4つの列を持つ特定のDataTableオブジェクトが作成されます。ワークシートデータは、ワークシートで可視なすべての行と列から始まって、すでに作成されたDataTableオブジェクトにエクスポートされます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **新しいDataTableに**
時々、新しいDataTableオブジェクトを作成したくない場合は、単純にワークシートデータを新しいDataTableオブジェクトにエクスポートする必要があります。

以下の例では、Exportメソッドの使用方法を別の方法で示しています。アクティブなワークシートの参照を取得し、そのワークシートの完全なデータを新しいDataTableオブジェクトにエクスポートします。 DataTableオブジェクトは、任意の方法で使用できます。 たとえば、DataTableオブジェクトをGridViewにバインドしてデータを表示することができます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
