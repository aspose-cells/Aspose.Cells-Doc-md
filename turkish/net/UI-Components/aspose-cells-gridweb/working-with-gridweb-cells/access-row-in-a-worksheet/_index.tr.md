---
title: GridWeb Çalışsayındaki GridRow a Erişim
type: docs
weight: 10
url: /tr/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb, GridRow, satır alma
description: Bu makale, GridWeb çalışsayısında satır nesnesi (GridRow) nasıl alınacağını tanıtır.
---
### Satırları Üzerinde Dolaşma
**En İyi Uygulamalar:**
Eğer çalışma sayfasındaki tüm satırlara birer birer erişmek istiyorsak, **yineleyicileri** kullanarak mevcut satırları dolaşabiliriz. Bu bellek tasarrufu yapacaktır.
~~~C#

// Yineleyiciler kullanarak bir satıra erişme
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
Aşağıdaki kodu karşılaştırın, bu şekilde tüm satır nesneleri oluşturulacaktır,  boş olup olmadığına bakılmaksızın, bu nedenle bellek sorunlarına yol açacaktır, bu nedenle lütfen bu yöntemi **kullanmayın**
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
Bununla birlikte, CheckRow yöntemini kullanarak, satırın boş olup olmadığını kontrol edebilirsiniz.
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
