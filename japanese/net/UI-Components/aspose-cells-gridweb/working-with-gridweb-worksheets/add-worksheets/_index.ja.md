---
title: ワークシートの追加
type: docs
weight: 20
url: /ja/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: この記事では、GridWebでワークシート（GridWorksheet）を追加する方法について紹介します。
---

{{% alert color="primary" %}} 

ワークシートはAspose.Cells.GridWebの重要な部分です。すべてのデータはワークシートの形式で管理および格納されます。Aspose.Cells.GridWebを使用して、1つ以上のワークシートをAspose.Cells.GridWebコントロールに追加できます。

{{% /alert %}} 
## **ワークシートの追加**
### **シート名を指定せずに**
Aspose.Cells.GridWebにワークシートを追加する最も簡単な方法は、GridWebコントロール内のGridWorksheetCollectionコレクションのAddメソッドを呼び出すことです。これにより、デフォルトの名前（Sheet1、Sheet2、Sheet3など）が使用されるワークシートが作成され、GridWebコントロールに追加されます。

**出力: デフォルトの名前のワークシートがGridWebに追加されました** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Addメソッドは、新しいワークシートのインデックスを返します。これを使用してこのワークシートのインスタンスにアクセスできます。ワークシートにアクセスする詳細については、[ワークシートへのアクセス](/cells/ja/net/aspose-cells-gridweb/access-worksheets/)をお読みください。

{{% /alert %}} 
### **指定されたシート名を使用して**
デフォルトの命名方式を使用せずに、GridWebコントロールに特定の名前を持つワークシートを追加するには、指定されたSheetNameを取るAddメソッドのオーバーロードバージョンを呼び出します。例えば、以下の例はInvoiceという名前のワークシートを追加します。

**出力: 指定された名前のワークシートがGridWebに追加されました** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

文字列としてワークシート名を受け取るAddメソッドは、GridWorksheetのインスタンスを返します。

{{% /alert %}}
