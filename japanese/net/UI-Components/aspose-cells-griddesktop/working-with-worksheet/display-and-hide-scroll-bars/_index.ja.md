---
title: スクロールバーの表示と非表示
type: docs
weight: 140
url: /ja/net/aspose-cells-griddesktop/display-and-hide-scroll-bars/
keywords: GridDesktop,show,hide,scroll,scroll bar
description: この記事では、GridDesktopでスクロールバーの表示または非表示を紹介します。
---

{{% alert color="primary" %}}

スクロールバーは、幅や深さがあり、つまり多くの行や列を持つスプレッドシートのコンテンツをナビゲートするために便利です。ほとんどのアプリケーションは、2つのタイプのスクロールバーをサポートしています:

- 垂直スクロールバー
- 水平スクロールバー

これらはいずれもMicrosoft Excelで見つかります。

Aspose.Cells.GridDesktop APIは、ワークシートのコンテンツをスクロールするための水平および垂直スクロールバーを提供します。Aspose.Cells.GridDesktop APIを使用すると、開発者はこれらの両方のスクロールバーの表示を制御できます。

{{% /alert %}}

## **スクロールバーの表示を制御する**

GridDesktopでスクロールバーの表示を制御するには、IsVerticalScrollBarVisibleおよびIsHorizontalScrollBarVisibleプロパティを使用します。以下の例では、スクロールバーを非表示および表示する方法を示します。

### **プログラミングサンプル: スクロールバーの非表示**

スクロールバーを非表示にするには、表示を制御するプロパティをfalseに設定します。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}

### **プログラミングサンプル: スクロールバー表示**

スクロールバーを表示するには、表示を制御するプロパティをtrueに設定します。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}
