---
title: ペインのフリーズとフリーズ解除
type: docs
weight: 50
url: /ja/net/freeze-and-unfreeze-panes/
---
{{% alert color="primary" %}} 

このトピックでは、行と列を固定および固定解除する方法について説明します。列または行を固定すると、ユーザーはワークシートの他の部分にスクロールしている間、列見出しまたは行タイトルを表示したままにすることができます。この機能は、大量のデータを含むワークシートを操作する場合に非常に役立ちます。ユーザーがスクロールすると、データのみが下にスクロールされ、見出しがそのまま残るため、日付が読みやすくなります。フリーズ ペイン機能は、Internet Explorer 6.0 以降でのみサポートされています。

{{% /alert %}} 
## **行と列の固定**
特定の数の行と列を固定するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. 行と列の数を固定します。



{{% alert color="primary" %}} 

インターフェイスを使用して、特定の数の行と列を固定することもできます。行と列を固定するセルを右クリックして選択します**氷結**リストから。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-FreezePanes.aspx-FreezePanes.cs" >}}
## **行と列の解凍**
行と列を固定解除するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. 行と列の固定を解除します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-FreezePanes.aspx-UnfreezePanes.cs" >}}
