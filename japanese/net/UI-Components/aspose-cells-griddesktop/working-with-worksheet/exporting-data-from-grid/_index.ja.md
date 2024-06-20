---
title: Gridからデータをエクスポート
type: docs
weight: 60
url: /ja/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop,export,data,export data
description: この記事では、GridDesktopでデータをエクスポートする方法を紹介します。
---

{{% alert color="primary" %}} 

前のトピックでは、Aspose.Cells.GridDesktopコントロールにDataTableのコンテンツをインポートすることについて説明しましたが、わざとAspose.Cells.GridDesktopが逆のプロセスもサポートしていることに触れませんでした。そのため、このトピックでは、Aspose.Cells.GridDesktopコントロール内のデータをDataTableにエクスポートすることについて説明します。

{{% /alert %}} 
## **グリッドコンテンツのエクスポート**
### **特定のDataTableにエクスポート**
グリッドのコンテンツを特定のDataTableオブジェクトにエクスポートするには、以下の手順に従ってください:Aspose.Cells.GridDesktopコントロールを**Form**に追加します。

- 必要に応じて特定のDataTableオブジェクトを作成します。
- 選択した**Worksheet**のデータを指定したDataTableオブジェクトにエクスポートします。

以下の例では、4つの列を持つ特定のDataTableオブジェクトを作成しました。最後に、作成済みのDataTableオブジェクトにワークシートデータ（最初のセルから始まり、69行と4列）をエクスポートしました。

**例:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **新しいDataTableにエクスポート**
開発者は自分自身のDataTableオブジェクトを作成することに興味がない場合があり、ワークシートデータを新しいDataTableオブジェクトにエクスポートするだけでよい場合があります。これは開発者にとっては最も迅速な方法です。

以下の例では、ExportDataTableメソッドの使用方法を説明する別の方法を試みました。現在アクティブなワークシートの参照を取得し、そのアクティブなワークシートの完全なデータを新しいDataTableオブジェクトにエクスポートしました。このDataTableオブジェクトは、開発者が望むように使用できます。たとえば、このDataTableオブジェクトをDataGridにバインドしてデータを表示することができます。

**例:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

上記のケースでは、ExportDataTableメソッドのオーバーロードバージョンを使用して、単純にワークシートからエクスポートされたデータを含む新しいDataTableオブジェクトを返します。

{{% /alert %}}
