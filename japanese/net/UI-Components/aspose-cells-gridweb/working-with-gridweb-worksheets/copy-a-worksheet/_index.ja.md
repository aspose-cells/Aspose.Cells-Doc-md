---
title: ワークシートのコピー
type: docs
weight: 50
url: /ja/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb,コピー,GridWorksheet
description: この記事では、GridWebでワークシート（GridWorksheet）をコピーする方法について紹介しています。
---

{{% alert color="primary" %}} 

[ワークシートの追加](/cells/ja/net/aspose-cells-gridweb/add-worksheets/)では、Aspose.Cells.GridWebに新しいワークシートを追加する方法について説明しています。また、Aspose.Cells.GridWebに別のワークシートのコピー（またはレプリカ）を追加することも可能です。同様のデータが別のワークシートにも必要な場合、既存のワークシートをコピーして新しいワークシートとしてAspose.Cells.GridWebに追加する方が簡単です。 

{{% /alert %}} 
## **ワークシートのコピー**
### **Sheetのインデックスを使用して**
以下のサンプルコードは、GridWebコントロールにワークシートのインデックスを指定してワークシートのコピーを追加する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **シート名を使用する**
以下のサンプルコードは、GridWorksheetCollectionのAddCopyメソッドでワークシートの名前を指定して、そのワークシートのコピーをGridWebコントロールに追加する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

AddCopyメソッドは、新しく追加されたワークシートのインデックスを返し、そのインデックスを使用してワークシートインスタンスにアクセスすることができます。ワークシートへのアクセス方法の詳細については、[ワークシートへのアクセス](/cells/ja/net/aspose-cells-gridweb/access-worksheets/)を参照してください。

{{% /alert %}}
