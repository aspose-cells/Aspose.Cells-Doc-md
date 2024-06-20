---
title: GridWeb Çalışsayındaki GridRow a Erişim
type: docs
weight: 10
url: /tr/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop,GridRow,satır al
description: Bu makale, GridDesktop teki Çalışsayfadaki satır nesnesine (GridRow) erişmeyi tanıtır.
---
### Satırları Üzerinde Dolaşma
**En İyi Uygulamalar:**
Eğer çalışma sayfasındaki tüm satırlara birer birer erişmek istiyorsak, **yineleyicileri** kullanarak mevcut satırları dolaşabiliriz. Bu bellek tasarrufu yapacaktır.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Yineleyiciler kullanarak bir satıra erişme
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
Aşağıdaki kodu karşılaştırın, bu şekilde tüm satır nesneleri oluşturulacaktır,  boş olup olmadığına bakılmaksızın, bu nedenle bellek sorunlarına yol açacaktır, bu nedenle lütfen bu yöntemi **kullanmayın**
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
Bununla birlikte, CheckRow yöntemini kullanarak, satırın boş olup olmadığını kontrol edebilirsiniz.
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
