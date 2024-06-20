---
title: ワークシートでハイパーリンクを管理する
type: docs
weight: 100
url: /ja/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb、ハイパーリンク
description: この記事では、GridWebでハイパーリンクを操作する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridWebでサポートされているハイパーリンクの種類とそれらをプログラムで管理する方法について説明します。 ハイパーリンクはWeb URLへのリンクを作成したり、サーバーへのポストバックを実行したりするために使用できます。

{{% /alert %}} 
## **ハイパーリンクの操作**
### **ハイパーリンクの種類**
一般的に、Aspose.Cells.GridWebでサポートされているハイパーリンクの種類は次のとおりです：

- [URLハイパーリンク](/cells/ja/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)、Web URLにリンクできるハイパーリンク。
- [テキストハイパーリンク](/cells/ja/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)、テキストに適用されたURLハイパーリンク。
- [画像ハイパーリンク](/cells/ja/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)、画像に適用されたURLハイパーリンク。
- [セルコマンドハイパーリンク](/cells/ja/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)、サーバーにデータを送信するハイパーリンク。 このようなハイパーリンクは、クリックしたときにサーバーサイドイベントをトリガーするボタンのような役割を果たします。

以下のセクションでは、すべての種類のハイパーリンクの使用方法について詳しく説明します。また、リンクにアクセスしたり削除したりする方法についても説明します。
### **ハイパーリンクの追加**

#### **URLハイパーリンク**
URLハイパーリンクは、通常ウェブサイトで見ることができるシンプルなハイパーリンクのように見えます。URLハイパーリンクはセル内のアンカーのように機能します。クリックすると、ウェブページに移動したり、新しいブラウザウィンドウが開かれます。

異なる種類のURLハイパーリンクがあります:

- テキストハイパーリンク。
- 画像ハイパーリンク。

開発者は、ハイパーリンクのための画像を指定できます。画像が指定されていない場合、テキストハイパーリンクが作成されます。それ以外の場合は、画像ハイパーリンクが作成されます。


##### **テキストハイパーリンク**
ワークシートにテキストハイパーリンクを追加するには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ワークシートにアクセスします。
3. ワークシートのセルにハイパーリンクを追加します。
4. セルに表示されるテキストを設定します。
5. ハイパーリンクのURLを設定します。
6. 必要に応じて、ハイパーリンクのターゲットを設定します。
1. 必要に応じてツールヒントを設定します。

{{% alert color="primary" %}} 

注: ハイパーリンクのターゲットは、ウェブURLを新しいウィンドウ、現在のウィンドウ、またはトップウィンドウで開くために、それぞれ_self、_top、_parentに設定できます。

{{% /alert %}} 

以下の例は、ワークシートに2つのハイパーリンクを追加します。一つはターゲットが指定されていない状態で、もう一つは_parentに設定されています。

**出力: ワークシートにテキストハイパーリンクが追加されました** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **画像ハイパーリンク**
画像ハイパーリンクを追加するには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ワークシートにアクセスします。
1. セルにハイパーリンクを追加します。
4. ハイパーリンクとして表示される画像のURLを設定します。
5. ハイパーリンクのURLを設定します。
1. 必要に応じてツールヒントを設定します。
7. 必要に応じて、ハイパーリンクのテキストを設定します。

**出力: ワークシートに画像ハイパーリンクが追加されました** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**画像のURLに対応する画像は見つかりませんでした** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **セルコマンドハイパーリンク**
セルコマンドハイパーリンクは、ウェブページを開く代わりにサーバーサイドのイベントをトリガーする特別なハイパーリンクの種類です。開発者は、サーバーサイドイベントにコードを追加し、ハイパーリンクがクリックされたときに任意のタスクを実行できます。この機能により、開発者はよりインタラクティブなアプリケーションを作成することができます。

セルコマンドハイパーリンクを追加する:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ワークシートにアクセスします。
1. セルにハイパーリンクを追加します。
1. ハイパーリンクのコマンドを任意の値に設定します。
   その値は、ハイパーリンクのイベントハンドラーがそれを認識するために使用されます。
1. 必要に応じてツールヒントを設定します。
1. ハイパーリンクとして表示される画像のURLを設定します。

**ワークシートにセルコマンドハイパーリンクが追加されました** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **セルコマンドハイパーリンクのイベントハンドリング**
特定のセルコマンドハイパーリンクがクリックされたときに特定のタスクを実行するために、開発者はGridWebコントロールのCellCommandイベントのイベントハンドラーを作成する必要があります。CellCommandイベントのイベントハンドラーは、Argumentプロパティを提供するCellEventArgs型のオブジェクトを提供します。Argumentプロパティを使用して、CellCommandの値を比較して特定のハイパーリンクを識別します。

以下の例では、上記のコードで作成されたセルコマンドハイパーリンクに対するイベントハンドラーを作成します。 ハイパーリンクのCellCommandがClickに設定されていたので、イベントハンドラーではまずそれを確認し、その後、A6セルにメッセージを表示するコードを追加します。

ハイパーリンクがクリックされたときにイベントハンドラーが呼び出されます。

**出力: ハイパーリンクがクリックされたときにA6セルにテキストが追加されます** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **ハイパーリンクのアクセス**
既存のハイパーリンクにアクセスするには:

1. それを含むセルにアクセスします。
1. セルの参照を取得します。
1. ハイパーリンクのプロパティを変更します。
1. ハイパーリンクコレクションのGetHyperlinkメソッドに参照を渡してハイパーリンクにアクセスします。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **ハイパーリンクの削除**
ハイパーリンクを削除するには:

1. アクティブなワークシートにアクセスします。
1. HyperlinksコレクションのRemoveメソッドを使用してハイパーリンクを削除します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
