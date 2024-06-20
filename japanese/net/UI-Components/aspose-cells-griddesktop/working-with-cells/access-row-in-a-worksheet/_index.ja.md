---
title: ワークシート内のGridRowにアクセス
type: docs
weight: 10
url: /ja/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop、GridRow、行を取得
description: この記事では、GridDesktopのワークシート内で行オブジェクト（GridRow）を取得する方法を紹介します。
---
### 行を反復処理する
**ベストプラクティス**：
ワークシート内のすべての行に順番にアクセスしたい場合は、**イテレータ**を使用して既存の行をトラバースします。これによりメモリを**節約**できます。
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// イテレータを使用して行にアクセス
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
以下のコードを比較すると、nullであってもすべての行オブジェクトが作成されるため、メモリの問題が発生する可能性がありますので、この方法は**使用しないで**ください
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
ただし、空であるかどうかを確認するためにCheckRowメソッドを使用できます
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
