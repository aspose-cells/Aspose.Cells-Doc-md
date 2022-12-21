---
title: ワークシートでハイパーリンクを管理する
type: docs
weight: 100
url: /ja/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridWeb でサポートされているハイパーリンクの種類と、それらをプログラムで管理する方法について説明します。ハイパーリンクは、Web URL へのリンクを作成するか、サーバーへのポストバックを実行するために使用できます。

{{% /alert %}} 
## **ハイパーリンクの操作**
### **ハイパーリンクの種類**
通常、Aspose.Cells.GridWeb では次のハイパーリンクがサポートされています。

- [URL ハイパーリンク](/cells/ja/net/manage-hyperlinks-in-worksheet/)、Web URL にリンクできるハイパーリンク。
- [テキストハイパーリンク](/cells/ja/net/manage-hyperlinks-in-worksheet/)、テキストに適用された URL ハイパーリンク。
- [画像のハイパーリンク](/cells/ja/net/manage-hyperlinks-in-worksheet/)、画像に適用された URL ハイパーリンク。
- [Cell コマンドのハイパーリンク](/cells/ja/net/manage-hyperlinks-in-worksheet/)、サーバーにデータを送信するハイパーリンク。このようなハイパーリンクは、クリックするとサーバー側のイベントをトリガーするボタンのように機能します。

以下のセクションでは、すべての種類のハイパーリンクの使用について詳しく説明します。また、リンクへのアクセスまたはリンクの削除方法についても説明します。
### **ハイパーリンクの追加**

#### **URL ハイパーリンク**
URL ハイパーリンクは、Web サイトで通常見られる単純なハイパーリンクに似ています。 URL ハイパーリンクは、セル内のアンカーのように機能します。クリックするたびに、Web ページに移動するか、新しいブラウザー ウィンドウが開きます。

URL ハイパーリンクにはさまざまな種類があります。

- テキスト ハイパーリンク。
- 画像のハイパーリンク。

開発者は、ハイパーリンクのイメージを指定できます。画像が指定されていない場合は、テキスト ハイパーリンクが作成されます。それ以外の場合は、画像のハイパーリンクが作成されます。


##### **テキスト ハイパーリンク**
ワークシートにテキスト ハイパーリンクを追加するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. ワークシートのセルにハイパーリンクを追加します。
1. セルに表示されるテキストを設定します。
1. ハイパーリンクの URL を設定します。
1. 必要に応じて、ハイパーリンクのターゲットを設定します。
1. 必要に応じて、ツール ヒントを設定します。

{{% alert color="primary" %}} 

注: ハイパーリンク ターゲットは次のように設定できます。_自己、_top または _parent は、それぞれ新しいウィンドウ、現在のウィンドウ、またはトップ ウィンドウで Web URL を開くためのものです。

{{% /alert %}} 

次の例では、ワークシートに 2 つのハイパーリンクを追加します。 1 つはターゲットがなく、もう 1 つは _parent に設定されています。

**出力: ワークシートに追加されたテキスト ハイパーリンク** 

![todo:画像_代替_文章](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **画像ハイパーリンク**
画像ハイパーリンクを追加するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. セルにハイパーリンクを追加します。
1. ハイパーリンクとして表示される画像の URL を設定します。
1. ハイパーリンク URL を設定します。
1. 必要に応じて、ツール ヒントを設定します。
1. 必要に応じて、ハイパーリンク テキストを設定します。

**出力: ワークシートに追加された画像のハイパーリンク** 

![todo:画像_代替_文章](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

画像ハイパーリンクの AltText を設定すると、<ALT> HTMLのタグ。ハイパーリンクされた画像が表示されていない場合にのみ、テキストが表示されます。 (たとえば、画像が指定された場所にない場合。) 2 番目のハイパーリンクの画像が見つからない場合、以下のコード スニペットの出力は次のようになります。

**画像 URL の画像が見つかりませんでした** 

![todo:画像_代替_文章](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell コマンド ハイパーリンク**
セル コマンド ハイパーリンクは、Web ページを開く代わりにサーバー側のイベントをトリガーする特殊なタイプのハイパーリンクです。開発者は、サーバー側のイベントにコードを追加し、ハイパーリンクがクリックされたときに任意のタスクを実行できます。この機能により、開発者はよりインタラクティブなアプリケーションを作成できます。

セル コマンドのハイパーリンクを追加するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. セルにハイパーリンクを追加します。
1. ハイパーリンクの Command を任意の値に設定します。
この値は、ハイパーリンクのイベント ハンドラーがそれを認識するために使用されます。
1. 必要に応じて、ツール ヒントを設定します。
1. ハイパーリンクとして表示される画像の URL を設定します。

**セル コマンドのハイパーリンクがワークシートに追加されました** 

![todo:画像_代替_文章](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Cell コマンド ハイパーリンクのイベント処理**
開発者は、特定のセル コマンド ハイパーリンクがクリックされたときに特定のタスクを実行するために、GridWeb コントロールの CellCommand イベントのイベント ハンドラーを作成する必要があります。 CellCommand イベントのイベント ハンドラーは、Argument プロパティを提供する CellEventArgs 型のオブジェクトを提供します。 Argument プロパティを使用して、CellCommand 値を比較して特定のハイパーリンクを識別します。

以下の例では、上記のコードで作成されたセル コマンド ハイパーリンクのイベント ハンドラーを作成します。ハイパーリンクの CellCommand は Click に設定されました。そのため、イベント ハンドラーでまずチェックしてから、A6 セルにメッセージを表示するコードを追加します。

ハイパーリンクがクリックされると、イベント ハンドラーが呼び出されます。

**出力: ハイパーリンクがクリックされたときに A6 セルに追加されるテキスト** 

![todo:画像_代替_文章](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **ハイパーリンクへのアクセス**
既存のハイパーリンクにアクセスするには:

1. それを含むセルにアクセスします。
1. セル参照を取得します。
1. Hyperlinks コレクションの GetHyperlink メソッドへの参照を渡して、ハイパーリンクにアクセスします。
1. ハイパーリンクのプロパティを変更します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **ハイパーリンクの削除**
ハイパーリンクを削除するには:

1. アクティブなワークシートにアクセスします。
1. Hyperlinks コレクションの Remove メソッドを使用して、ハイパーリンクを削除します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
