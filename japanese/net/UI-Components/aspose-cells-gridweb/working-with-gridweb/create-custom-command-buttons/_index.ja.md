---
title: カスタムコマンドボタンを作成する
type: docs
weight: 100
url: /ja/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb,コマンド,カスタムコマンドボタン,カスタム
description: この記事では、GridWebでカスタムコマンドボタンを作成する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebには、**Submit**、**Save**、**Undo**などの特別なボタンが含まれています。これらのボタンは、それぞれ特定のタスクをAspose.Cells.GridWebで実行します。
カスタムタスクを実行するカスタムボタンを追加することも可能です。このトピックでは、この機能の使用方法について説明します。

{{% /alert %}} 
## **カスタムコマンドボタンの作成**
Aspose.Cells.GridWeb でカスタムコマンドボタンを作成するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
2. CustomCommandButton クラスのインスタンスを作成します。
3. ボタンのコマンドを特定の値に設定します。この値は、ボタンのイベントハンドラで使用されます。
4. ボタンのテキストを設定します。
5. ボタンの画像 URL を設定します。
6. 最後に、CustomCommandButton オブジェクトを GridWeb コントロールの CustomCommandButtons コレクションに追加します。

{{% alert color="primary" %}} 

カスタムコマンドボタンは、Visual Studio のプロパティダイアログを使用して WYSIWYG モードで追加することもできます。

{{% /alert %}} 

コードスニペットの出力は以下に示されます:

**GridWeb コントロールに追加されたカスタムコマンドボタン** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **カスタムコマンドボタンのイベント処理**
カスタムコマンドボタンの最も重要な側面は、クリック時に実行するアクションです。アクションを設定するには、GridWeb コントロールの CustomCommand イベントのイベントハンドラを作成します。

CustomCommand イベントは常にカスタムコマンドボタンがクリックされたときにトリガーされます。したがって、イベントハンドラは、GridWeb コントロールにボタンを追加するときに設定されたコマンドによって適用される特定のカスタムコマンドボタンを識別する必要があります。最後に、ボタンがクリックされたときに実行されるカスタムコードを追加します。

以下のコード例では、ボタンがクリックされたときにセル A1 にテキストメッセージを追加します。

**カスタムコマンドボタンがクリックされたときに A1 セルに追加されたテキスト** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
