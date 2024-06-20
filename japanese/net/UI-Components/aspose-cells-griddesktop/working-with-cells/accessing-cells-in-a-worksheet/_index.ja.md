---
title: ワークシート内のGridCellにアクセスする
type: docs
weight: 10
url: /ja/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: この記事では、GridDesktopのワークシート内でセルオブジェクト（GridCell）を取得する方法を紹介します。
---

{{% alert color="primary" %}} 

これまでワークシート、行、列について説明してきましたが、これからはもう少し深く掘り下げて、セルについて話を進めていきます。このトピックでは、セルのアクセスに関する基本的な機能から始めます。

{{% /alert %}} 
## **ワークシートのセルにアクセスする**
Aspose.Cells.GridDesktopのAPIを使用して、ワークシートの任意のセルにアクセスすることができます。セルにアクセスする方法として、次の３つの可能な方法があります：

- **セル名を使用する**
- **行および列のインデックスを使用する**
- **フォーカスを当てるセルの取得**

以上の3つのアプローチについて、1つずつ議論しましょう。
### **セル名の使用**
ワークシート内のすべてのセルにはユニークな名前があります。 たとえば、A1、A2、B1、B2などです。 Aspose.Cells.GridDesktopを使用すると、開発者はセルの名前を使用して任意のセルにアクセスできます。 セルの名前（インデックスとして）を**Worksheet**の**Cells**コレクションに渡すだけで済みます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**注意**

cells[cellName]を使用してGridCellにアクセスすると、より多くのメモリを消費してしまう場合があります。セルがnullであっても新しいセル（GridCell）オブジェクトが常に作成されます。

### **セルの行および列のインデックスを使用する**

**ベストプラクティス**：

セルの値やセルのスタイルを取得し、更新操作を行いたくない場合は、存在しないセルの場合はnullを返す**CheckCell**メソッドを使用することができます。これによりメモリが**節約**できます。
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// 行および列のインデックスを使用してセルにアクセスする
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

ワークシート内のセルは、その行および列のインデックスによっても識別できます。 セルの行および列のインデックスを**Worksheet**の**Cells**コレクションに渡すだけで済みます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**注意**

cells[rowIndex, columnIndex]を使用してGridCellにアクセスすると、より多くのメモリを消費する可能性があります。 セルがnullであるかどうかに関係なく、新しいセル（GridCell）オブジェクトを常に作成します。


### **フォーカスを当てるセルの取得**
正確にどのセルにアクセスするか分からない場合は、Aspose.Cells.GridDesktopを使用して、ユーザーのフォーカスが当たっているセルにアクセスすることもできます。 この機能を使用すると、ユーザーが任意のセルを選択し、それをバックエンドでアクセスすることができます。 これは単に**Worksheet**の**GetFocusedCell**メソッドを使用することで簡単に実現できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**ベストプラクティス**：
### セルを反復処理する
ワークシート内のすべてのセルに1つずつアクセスしたい場合は、**反復子**を使用して存在するセルをトラバースできます。 これにより**メモリが節約**されます。
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
以下のコードを比較してください、これは**悪い**方法です。 これにより、nullであるかどうかに関係なくすべてのセルオブジェクトが作成されるため、メモリの問題が発生します。 したがって、この方法は**使用しないで**ください。
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~

