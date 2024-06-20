---
title: GridWeb およびそのヘッダーバーのリサイズ
type: docs
weight: 30
url: /ja/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb,resize
description: この記事では、GridWebのリサイズ方法について紹介します。
---

{{% alert color="primary" %}} 

[Web フォームに GridWeb を追加する](/cells/ja/net/aspose-cells-gridweb/add-gridweb-to-web-form/)では、WYSIWYG を使用して Aspose.Cells.GridWeb コントロールのサイズ変更について説明しました。この記事では、Aspose.Cells.GridWeb API を使用してランタイムで同じことを行う方法と、ヘッダーバーのデータを読みやすくするためにAspose.Cells.GridWebコントロールのヘッダーバーのサイズ変更方法について説明します。

{{% /alert %}} 
## **Aspose.Cells.GridWeb の幅と高さを変更する**
Aspose.Cells.GridWebコントロールの幅と高さを変更することは、単純ながら重要な機能です。Aspose.Cells.GridWebコントロールはAPI内のGridWebクラスで表されます。GridWebコントロールの幅と高さを変更するには、その幅と高さのプロパティを単純に使用します。

{{% alert color="primary" %}} 

コントロールの幅と高さはピクセルまたはポイントで定義できます。

{{% /alert %}} 

以下のコードスニペットの出力は以下のようになります。

**GridWebコントロールの幅と高さを変更しました** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **ヘッダーバーの幅と高さを変更する**
Aspose.Cells.GridWebコントロールには、次のような2つのヘッダーバーがあります:

- 上部ヘッダーバー：このヘッダーバーには、A、B、C、Dなどの列が表示されます。
- 左側ヘッダーバー：このヘッダーバーには、1、2、3、4などの行が表示されます。

これらのヘッダーバーは以下に示しています。

**ヘッダーバー** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

GridWebコントロールのHeaderBarHeightとHeaderBarWidthプロパティを使用して、上部ヘッダーバーの高さと左側ヘッダーバーの幅を変更します。以下のコード例の出力は以下のようになります。

**ヘッダーバーの幅と高さを変更しました** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
