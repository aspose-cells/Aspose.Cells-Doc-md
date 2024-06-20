---
title: DataTableからグリッドにデータをインポートする
type: docs
weight: 50
url: /ja/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop、import、data、datatable
description: この記事では、GridDesktopでデータをインポートする方法について紹介します。
---

{{% alert color="primary" %}} 

.NET Frameworkのリリース以来、MicrosoftはDataTableオブジェクトの形式でデータをオフラインモードで保存する優れた方法を提供してきました。開発者のニーズを理解して、Aspose.Cells.GridDesktopもデータテーブルからデータをインポートする機能をサポートしています。このトピックでは、これを行う方法について説明します。

{{% /alert %}} 
## **例**
Aspose.Cells.GridDesktopコントロールを使用してデータテーブルの内容をインポートするには:

1. フォームにAspose.Cells.GridDesktopコントロールを追加します。
1. インポートされるデータを含むDataTableオブジェクトを作成します。
1. 所望のワークシートの参照を取得します。
1. データテーブルの内容をワークシートにインポートします。
1. データテーブルの列名に応じてワークシートの列ヘッダーを設定します。
1. 必要に応じて列の幅を設定します。
1. ワークシートを表示します。

以下の例では、DataTableオブジェクトを作成し、データベーステーブル「Products」から取得したいくつかのデータでそれを埋めました。最後に、そのDataTableオブジェクトからデータを希望のワークシートにインポートしました。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
