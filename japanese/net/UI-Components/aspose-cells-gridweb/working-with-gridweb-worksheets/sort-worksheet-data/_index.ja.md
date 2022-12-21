---
title: ワークシート データの並べ替え
type: docs
weight: 80
url: /ja/net/sort-worksheet-data/
---
{{% alert color="primary" %}} 

並べ替えは、データ処理に関して非常に価値のある機能です。ソートされていないデータは、特定の情報を検索するときにユーザーにとって苦痛です。 Aspose.Cells.GridWeb は、強力な並べ替え機能をサポートしています。このトピックでは、Aspose.Cells.GridWeb API を使用したデータの並べ替えについて説明します。

{{% /alert %}} 
## **データの並べ替え**
Aspose.Cells.GridWeb を使用すると、開発者はデータを水平および垂直に並べ替えることができるため、開発者はデータを上から下または左から右に並べ替えることができます。
### **上から下まで**
データを上から下に並べ替えるには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 並べ替えるワークシートにアクセスします。
1. データの範囲を任意の順序 (昇順または降順) で並べ替えます。必ず上から下の方向を選択してください。

次の例では、ワークシートの 4 つの列のデータを降順で並べ替えます。 4 つの列のうち 20 行のみが上から下の方向に並べ替えられます。

コードを適用する前は、ワークシートには順序付けされていないデータが含まれています。

![todo:画像_代替_文章](sort-worksheet-data_1.png)

コードの実行後、データは昇順でソートされます。

![todo:画像_代替_文章](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **左から右へ**
データを左から右に並べ替えるには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. 並べ替えるワークシートにアクセスします。
1. データの範囲を任意の順序 (昇順または降順) で並べ替えます。必ず左から右に選択してください。

次の例では、4 つの行のデータを昇順に並べ替えます。 7 列の 4 行のみが左から右に並べ替えられます。

コードを適用する前は、ワークシートには順序付けされていないデータが含まれています。

![todo:画像_代替_文章](sort-worksheet-data_3.png)

コードの実行後、データは昇順でソートされます。

![todo:画像_代替_文章](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

重要: 上記の例は、1 つの列 (上から下) または行 (左から右) に基づいてデータを並べ替える方法を示しています。 Aspose.Cells.GridWeb は、複数の列または行に従ってデータを並べ替えることもできます。これを行うには、列または行のインデックスの配列を Sort メソッドに渡します。ハイブリッド データ型の並べ替えもサポートされています。

{{% /alert %}}
