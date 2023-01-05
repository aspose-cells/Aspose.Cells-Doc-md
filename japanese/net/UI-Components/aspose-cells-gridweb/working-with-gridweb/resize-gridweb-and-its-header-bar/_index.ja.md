---
title: GridWeb とそのヘッダー バーのサイズを変更する
type: docs
weight: 30
url: /ja/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[GridWeb を Web フォームに追加する](/cells/ja/net/add-gridweb-to-web-form/)では、WYSIWYG を使用した Aspose.Cells.GridWeb コントロールのサイズ変更について説明しました。この記事では、実行時に Aspose.Cells.GridWeb API を使用して同じことを行う方法について説明します。また、データを読みやすくするために Aspose.Cells.GridWeb コントロールのヘッダー バーのサイズを変更する方法についても説明します。

{{% /alert %}} 
## **Aspose.Cells.GridWeb の幅と高さを変更する**
Aspose.Cells.GridWeb コントロールの幅と高さを変更することは、単純ですが重要な機能です。 Aspose.Cells.GridWeb コントロールは、API の GridWeb クラスによって表されます。GridWeb コントロールの幅と高さを変更するには、幅と高さのプロパティを使用します。

{{% alert color="primary" %}} 

コントロールの幅と高さは、ピクセルまたはポイントで定義できます。

{{% /alert %}} 

次のコード スニペットの出力を以下に示します。

**GridWeb コントロールの幅と高さを変更** 

![todo:画像_代替_文章](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **ヘッダーバーの幅と高さを変更する**
Aspose.Cells.GridWeb コントロールには、次の 2 つのヘッダー バーが含まれています。

- 上部のヘッダー バー。このヘッダー バーは列を A 、 B 、 C 、 D などとして表します。
- 左のヘッダー バー。このヘッダー バーは行を 1 、 2 、 3 、 4 などとして表します。

これらのヘッダー バーの両方を以下に示します。

**ヘッダーバー** 

![todo:画像_代替_文章](resize-gridweb-and-its-header-bar_2.png)

GridWeb コントロールの HeaderBarHeight プロパティと HeaderBarWidth プロパティをそれぞれ使用して、上部のヘッダー バーの高さと左側のヘッダー バーの幅を変更します。次の図は、次のコード例の出力を示しています。

**ヘッダーバーの幅と高さを変更** 

![todo:画像_代替_文章](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
