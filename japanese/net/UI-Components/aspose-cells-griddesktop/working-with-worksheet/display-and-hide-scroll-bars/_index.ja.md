---
title: スクロール バーの表示と非表示
type: docs
weight: 140
url: /ja/net/display-and-hide-scroll-bars/
---
{{% alert color="primary" %}}

スクロール バーは、幅が広く奥行きのある、つまり多数の行と列があるスプレッドシートの内容をナビゲートする場合に便利です。ほとんどのアプリケーションは、次の 2 種類のスクロール バーをサポートしています。

- 垂直スクロール バー
- 横スクロールバー

これらはどちらも Microsoft Excel にあります。

Aspose.Cell の GridDesktop API は、ワークシートの内容をスクロールするための水平および垂直スクロール バーを提供します。 Aspose.Cells.GridDesktop API を使用すると、開発者はこれら両方のスクロール バーの表示を制御できます。

{{% /alert %}}

## **スクロール バーの表示の制御**

GridDesktop でスクロール バーの可視性を制御するには、IsVerticalScrollBarVisible および IsHorizontalScrollBarVisible プロパティを使用します。以下の例は、スクロール バーを非表示および表示する方法を示しています。

### **プログラミング サンプル: スクロール バーの非表示**

スクロールバーを非表示にするには、可視性を制御するプロパティを false に設定します。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}

### **プログラミング サンプル: スクロール バーを表示する**

スクロールバーを表示するには、表示を制御するプロパティを true に設定します。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}
