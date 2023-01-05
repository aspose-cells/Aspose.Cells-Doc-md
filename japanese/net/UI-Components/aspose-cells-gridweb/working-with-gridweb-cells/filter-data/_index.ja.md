---
title: データのフィルタリング
type: docs
weight: 80
url: /ja/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb は、自動フィルターおよびカスタム データ フィルター機能を提供します。これらの機能を使用すると、リストに表示するワークシート内の項目のみを選択できます。さらに、設定された基準に従ってリスト内のアイテムをフィルタリングできます。フィルタリング機能を使用して、テキスト、数値、または日付をフィルタリングします。

{{% /alert %}} 
## **フィルターの操作**
ワークシートの AddAutoFilter メソッドを使用して、ワークシートのオートフィルターを有効にします。このメソッドは、行、開始、および終了列のインデックスを受け入れます。

カスタム フィルターを有効にするには、ワークシートの AddCustomFilter メソッドを使用します。このメソッドは、フィルターを適用する必要がある行インデックスとカスタム フィルター条件を受け入れます。

以下の例では、自動データ フィルターとカスタム データ フィルターの両方を実装しています。この例では、自動フィルター機能が有効になっており、フィルター処理された行がいくつかの基準に基づいて検索されます。

**入力: 最初のワークシートのデータ リスト** 

![todo:画像_代替_文章](filter-data_1.jpg)

**出力: 自動フィルター機能を有効にする** 

![todo:画像_代替_文章](filter-data_2.jpg)
### **オートフィルター**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **カスタム データ フィルタ**
**基準に基づいてカスタム フィルター処理されたデータ** 

![todo:画像_代替_文章](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
