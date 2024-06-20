---
title: データのフィルタリング
type: docs
weight: 80
url: /ja/net/aspose-cells-gridweb/filter-data/
keywords: GridWeb、フィルター、データのフィルタリング
description: この記事では、GridWebでデータのフィルタリング方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebでは、オートフィルターおよびカスタムデータフィルター機能が提供されています。これらの機能を使用すると、ワークシート内で表示したいアイテムのみを選択する方法が可能になります。さらに、フィルターを使用してリスト内のアイテムを設定した基準に従ってフィルタリングすることができます。フィルタリング機能を使用して、テキスト、数字、または日付をフィルタリングできます。

{{% /alert %}} 
## **フィルターの使用**
オートフィルターを有効にするには、ワークシートのAddAutoFilterメソッドを使用します。このメソッドは、行、開始列、および終了列のインデックスを受け入れます。

カスタムフィルターを有効にするには、ワークシートのAddCustomFilterメソッドを使用します。このメソッドは、フィルタを適用する行インデックスとカスタムフィルタリング基準を受け入れます。

以下の例では、オートフィルターおよびカスタムデータフィルターの両方を実装しています。例では、オートフィルター機能が有効になり、ある基準に基づいてフィルタリングされた行が検索されます。

**入力：最初のワークシート内のデータリスト** 

![todo:image_alt_text](filter-data_1.jpg)

**出力：オートフィルター機能を有効にする** 

![todo:image_alt_text](filter-data_2.jpg)
### **オートフィルター**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **カスタムデータフィルタ**
**基準に基づくカスタムフィルタリングされたデータ** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
