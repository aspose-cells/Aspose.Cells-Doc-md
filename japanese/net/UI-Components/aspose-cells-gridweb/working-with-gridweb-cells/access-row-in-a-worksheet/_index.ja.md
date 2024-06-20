---
title: ワークシート内のGridRowにアクセス
type: docs
weight: 10
url: /ja/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb、GridRow、行を取得します
description: この記事では、GridWebのワークシート内の行オブジェクト（GridRow）の取得方法について紹介します。
---
### 行を反復処理する
**ベストプラクティス**：
ワークシート内のすべての行に順番にアクセスしたい場合は、**イテレータ**を使用して既存の行をトラバースします。これによりメモリを**節約**できます。
~~~C#

// イテレータを使用して行にアクセス
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
以下のコードを比較すると、nullであってもすべての行オブジェクトが作成されるため、メモリの問題が発生する可能性がありますので、この方法は**使用しないで**ください
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
ただし、空であるかどうかを確認するためにCheckRowメソッドを使用できます
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
