---
title: ワークシートデータの並べ替え
type: docs
weight: 80
url: /ja/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb、sort
description: この記事では、Aspose.Cells.GridWebを使用してデータを並べ替える方法について紹介します。
---

{{% alert color="primary" %}} 

データの並べ替えは、データ処理において非常に有益な機能です。ソートされていないデータは、特定の情報を検索する際にユーザーにとって煩わしいものです。Aspose.Cells.GridWebは強力なソート機能をサポートしています。このトピックでは、Aspose.Cells.GridWeb APIを使用してデータをソートする方法について説明します。

{{% /alert %}} 
## **データのソート**
Aspose.Cells.GridWebは、開発者がデータを水平および垂直にソートすることができるようにします。つまり、開発者はデータを上から下にまたは左から右にソートすることができます。
### **上から下へ**
上から下へのデータをソートするには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ソートしたいワークシートにアクセスします。
1. データの範囲を昇順または降順でソートします。必ず上から下への向きを選択してください。

以下の例は、ワークシートの4つの列のデータを降順でソートしています。4つの列のうちの20行のデータが上から下への向きでソートされています。

コードを適用する前、ワークシートには順不同のデータが含まれています。

![todo:image_alt_text](sort-worksheet-data_1.png)

コードを実行した後、データは昇順でソートされます。

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **左から右へ**
左から右へのデータをソートするには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ソートしたいワークシートにアクセスします。
1. データの範囲を昇順または降順でソートします。必ず左から右への向きを選択してください。

以下の例は、7つの列のうちの4行のデータを昇順でソートしています。4行のデータが左から右への向きでソートされています。

コードを適用する前、ワークシートには順不同のデータが含まれています。

![todo:image_alt_text](sort-worksheet-data_3.png)

コードを実行した後、データは昇順でソートされます。

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

重要: 上記の例は、1つの列（上から下へ）または1つの行（左から右へ）を基準にデータをソートする方法を示しています。Aspose.Cells.GridWebは、複数列または複数行の基準に応じてデータをソートすることも可能です。そのためには、Sortメソッドに列または行のインデックスの配列を渡します。また、ハイブリッドデータ型のソートもサポートされています。

{{% /alert %}}
