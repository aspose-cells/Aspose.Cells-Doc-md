---
title: セルの値を取得および変更する
type: docs
weight: 20
url: /ja/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: この記事では、GridDesktopのワークシート内でセルの値を取得および変更する方法を紹介します。
---

{{% alert color="primary" %}} 

前のトピックでワークシートのセルにアクセスする方法について説明しました。このトピックでは、それを拡張して、Aspose.Cells.GridDesktopのAPIを使用してセルの値をアクセスおよび変更する方法を開発者に示します。

{{% /alert %}} 
## **Aspose.Cells.GridDesktopを使用したセルの値へのアクセスと変更**
セルの値にアクセスして変更する前に、ワークシートのセルにアクセスする方法を知っておく必要があります。ワークシートのセルにアクセスする方法については、３つのアプローチがあります。これらの３つのアプローチの詳細については、[ワークシートのセルにアクセスする](/cells/ja/net/accessing-cells-in-a-worksheet/)を参照してください。

それぞれのセルにはValueというプロパティがあります。ですので、一度セルにアクセスしたら、開発者はValueプロパティの内容にアクセスして変更し、セルの値をアクセスおよび変更できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**重要：** セルのValueプロパティを使用して値を変更することは、1つまたは数個のセルの値を設定するための適切な方法です。しかし、多くのセルの値を設定する必要がある場合は、このアプローチのパフォーマンスが良くない可能性があります。そのため、多くのセルの値を設定する場合は、アプリケーションのパフォーマンスを向上させるために、セルの**SetCellValue**メソッドを使用する必要があります。**SetCellValue**メソッドを使用した上記のコードスニペットの改良版を以下に示します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
