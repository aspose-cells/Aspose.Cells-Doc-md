---
title: Cell の値へのアクセスと変更
type: docs
weight: 20
url: /ja/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

前のトピックでは、ワークシートのセルへのアクセスについて説明しました。このトピックでは、Aspose.Cells.GridDesktop の API を使用してセルの値にアクセスして変更する方法を開発者に示すために、そのトピックを単純に拡張します。

{{% /alert %}} 
## **Aspose.Cells.GridDesktop を使用して Cell 値にアクセスして変更します**
セルの値にアクセスして変更する前に、セルへのアクセス方法を知っておく必要があります。ワークシートのセルにアクセスするには、3 つの方法があります。これら 3 つのアプローチの詳細については、[ワークシートで Cells にアクセスします。](/cells/ja/net/accessing-cells-in-a-worksheet/)

各セルには、 Value という名前のプロパティがあります。そのため、セルにアクセスすると、開発者は Value プロパティの内容にアクセスして変更し、セルの値にアクセスして変更することができます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**重要：**セルの Value プロパティを使用してその値を変更することは、単一または少数のセルの値を設定するための優れた方法です。多くのセルの値を設定する必要がある場合、このアプローチのパフォーマンスは良くありません。したがって、多くのセルの値を設定するには、使用する必要があります**SetCellValue**アプリケーションのパフォーマンスを向上させるためのセルのメソッド。を使用した上記のコード スニペットの修正版**SetCellValue**方法を以下に示します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
