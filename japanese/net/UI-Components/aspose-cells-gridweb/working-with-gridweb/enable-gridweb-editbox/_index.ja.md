---
title: GridWeb EditBox を有効にする
type: docs
weight: 110
url: /ja/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

GridWeb の編集ボックスは、データ/式をセルに表示/入力またはコピーするために使用できるコントロールの上部に表示されるツールバーです。また、編集中のセルの名前も表示されます。フレームをクリックした後、またはデータの書き込みを開始するか、等号 (=) 記号を入力すると、編集ボックスがアクティブになります。

{{% /alert %}} 
## **Aspose.Cells.GridWebのエディットボックスの設定**
GridWeb コントロールは、開発者がそれを "True" に割り当ててツールバーをオンにできる ShowCellEditBox プロパティを提供します。この属性のデフォルト値は False です。その値を「True」に設定すると、編集ボックスが GridWeb コントロールの上部に表示されます。

{{% alert color="primary" %}} 

この機能を有効にするには、「jquery.js」ファイルをプロジェクトにインポートし、.aspx ページで参照して機能させる必要があります。 jQuery アーカイブは次の場所からダウンロードできます。<https://jqueryui.com/download/all/>ライブラリファイルをプロジェクト内のフォルダーに配置し、ライブラリファイルへの参照を追加します<script>次のように .aspx Web フォームにタグを付けます。最新の jQuery バージョンはすべて問題ありません。

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**編集ボックスを使用した GridWeb コントロール** 

![todo:画像_代替_文章](enable-gridweb-editbox_1.png)
### **例**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
