---
title: DataTable からグリッドへのデータのインポート
type: docs
weight: 50
url: /ja/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

.NET フレームワークのリリース以来、Microsoft は DataTable オブジェクトの形式でオフライン モードでデータを保存する優れた方法を提供してきました。開発者のニーズを理解し、Aspose.Cells.GridDesktop はデータ テーブルからのデータのインポートもサポートしています。このトピックでは、これを行う方法について説明します。

{{% /alert %}} 
## **例**
Aspose.Cells.GridDesktop コントロールを使用してデータ テーブルの内容をインポートするには:

1. Aspose.Cells.GridDesktop コントロールをフォームに追加します。
1. インポートするデータを含む DataTable オブジェクトを作成します。
1. 目的のワークシートの参照を取得します。
1. データ テーブルの内容をワークシートにインポートします。
1. データ テーブルの列名に従って、ワークシートの列ヘッダーを設定します。
1. 必要に応じて、列の幅を設定します/
1. ワークシートを表示します。

以下の例では、DataTable オブジェクトを作成し、Products という名前のデータベース テーブルから取得したデータを入力しています。最後に、Aspose.Cells.GridDesktop を使用して、その DataTable オブジェクトから目的のワークシートにデータをインポートしました。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
