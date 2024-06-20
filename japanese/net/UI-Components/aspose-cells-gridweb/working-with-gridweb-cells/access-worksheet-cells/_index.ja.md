---
title: ワークシートセルにアクセス
type: docs
weight: 10
url: /ja/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: この記事では、GridWebのワークシート内のセル（GridCell）の取得方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridWebのセルを見て、最も基本的な機能であるセルへのアクセスを見ていきます。

{{% /alert %}} 
## **ワークシート内のセルへのアクセス**
各ワークシートには、実際にはAspose.Cells.GridWeb内のセルを表すGridCellオブジェクトのコレクションであるCellsというプロパティが含まれています。Aspose.Cells.GridWebを使用して任意のセルにアクセスすることが可能です。以下でそれぞれの推奨される方法について説明します。


### **セル名の使用**
すべてのセルにはユニークな名称があります。たとえば、A1、A2、B1、B2などです。Aspose.Cells.GridWebでは、セル名（インデックスとして）をCellsコレクションに渡すことで、任意のセルにアクセスすることができます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**注意**

cells[cellName]を使用してGridCellにアクセスすると、より多くのメモリを消費してしまう場合があります。セルがnullであっても新しいセル（GridCell）オブジェクトが常に作成されます。


### **行と列のインデックスを使用する**


セルは行と列のインデックスによっても識別できます。セルの行と列のインデックスをCellsコレクションに渡すだけで、任意のセルにアクセスできます。この方法は、上記の方法よりも高速です。

**ベストプラクティス**：

セルの値やセルのスタイルを取得し、更新操作を行いたくない場合は、存在しないセルの場合はnullを返す**CheckCell**メソッドを使用することができます。これによりメモリが**節約**できます。
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**ベストプラクティス**：
### セルを反復処理する
ワークシート内のすべてのセルに1つずつアクセスしたい場合は、**反復子**を使用して存在するセルをトラバースできます。 これにより**メモリが節約**されます。
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
以下のコードを比較してください、これは**悪い**方法です。 これにより、nullであるかどうかに関係なくすべてのセルオブジェクトが作成されるため、メモリの問題が発生します。 したがって、この方法は**使用しないで**ください。
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~
