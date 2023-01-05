---
title: カスタム コマンド ボタンの作成
type: docs
weight: 100
url: /ja/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb には、次のような特別なボタンが含まれています。**送信**, **セーブ**と**元に戻す**.これらのボタンはすべて、Aspose.Cells.GridWeb の特定のタスクを実行します。
カスタム タスクを実行するカスタム ボタンを追加することもできます。このトピックでは、この機能の使用方法について説明します。

{{% /alert %}} 
## **カスタム コマンド ボタンの作成**
Aspose.Cells.GridWeb でカスタム コマンド ボタンを作成するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. CustomCommandButton クラスのインスタンスを作成します。
1. ボタンのコマンドを何らかの値に設定します。この値は、ボタンのイベント ハンドラーで使用されます。
1. ボタンのテキストを設定します。
1. ボタンの画像 URL を設定します。
1. 最後に、CustomCommandButton オブジェクトを GridWeb コントロールの CustomCommandButtons コレクションに追加します。

{{% alert color="primary" %}} 

カスタム コマンド ボタンは、Visual Studio の [プロパティ] ダイアログを使用して WYSIWYG モードで追加することもできます。

{{% /alert %}} 

コード スニペットの出力を以下に示します。

**GridWeb コントロールに追加されたカスタム コマンド ボタン** 

![todo:画像_代替_文章](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **カスタム コマンド ボタンのイベント処理**
カスタム コマンド ボタンの最も重要な側面は、クリックしたときに実行されるアクションです。アクションを設定するには、GridWeb コントロールの CustomCommand イベントのイベント ハンドラーを作成します。

CustomCommand イベントは、カスタム コマンド ボタンがクリックされると常にトリガーされます。そのため、イベント ハンドラーは、ボタンを GridWeb コントロールに追加するときに、コマンド セットによって適用される特定のカスタム コマンド ボタンを識別する必要があります。最後に、ボタンがクリックされたときに実行されるカスタム コードを追加します。

以下のコード例では、ボタンがクリックされると、セル A1 にテキスト メッセージが追加されます。

**カスタム コマンド ボタンがクリックされたときに A1 セルに追加されるテキスト** 

![todo:画像_代替_文章](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
