---
title: ワークシートに Cell 保護を追加する
type: docs
weight: 130
url: /ja/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

GridDesktop の Aspose.Cells を使用すると、ワークシート内のセルを保護できます。最初にワークシートを保護する必要があります。次に、ワークシート内の目的のセルを保護できます。ワークシートを保護するために、設定してください**Worksheet.Protected**プロパティを true に設定してから使用します**Worksheet.SetProtected()**セルの範囲を保護する方法。

{{% /alert %}} 
## **Aspose.Cells.GridDesktop を使用して Cell を保護します。**
次のサンプル コードは、範囲内のすべてのセルを保護します。**A1:B1** GridDesktop のアクティブなワークシートの。この範囲内の任意のセルをダブルクリックすると、編集できなくなります。これらのセルを読み取り専用にします。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
