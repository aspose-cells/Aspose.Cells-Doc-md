---
title: ワークシートをコピーする
type: docs
weight: 50
url: /ja/net/copy-a-worksheet/
---
{{% alert color="primary" %}} 

[ワークシートを追加](/cells/ja/net/add-worksheets/)Aspose.Cells.GridWeb に新しいワークシートを追加する方法について説明します。別のワークシートのコピー (またはレプリカ) を Aspose.Cells.GridWeb コントロールに追加することもできます。この機能は、あるワークシートの同一または類似のデータが別のワークシートでも必要な場合に役立ちます。その場合、ゼロから作成するよりも、既存のワークシートをコピーして Aspose.Cells.GridWeb に新しいワークシートとして追加する方が簡単です。

{{% /alert %}} 
## **ワークシートのコピー**
### **シート インデックスの使用**
以下のコード例は、GridWorksheetCollection の AddCopy メソッドでワークシートのインデックスを指定することにより、ワークシートのコピーを GridWeb コントロールに追加する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **シート名の使用**
次のコード例は、GridWorksheetCollection の AddCopy メソッドでワークシートの名前を指定して、ワークシートのコピーを GridWeb コントロールに追加する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

 AddCopy メソッドは、ワークシート インスタンスへのアクセスに使用できる、新しく追加されたワークシートのインデックスを返します。ワークシートへのアクセス方法の詳細については、次を参照してください。[ワークシートへのアクセス](/cells/ja/net/access-worksheets/).

{{% /alert %}}
