---
title: Çalışma Sayfası Hücresine Erişme
type: docs
weight: 10
url: /tr/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: Bu makale, GridWeb de hücre (GridCell) nasıl alınacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konu hücreleri ele alır, Aspose.Cells.GridWeb'in en temel özelliğine bakar: hücrelere erişme.

{{% /alert %}} 
## **Çalışma Sayfasındaki Hücrelere Erişme**
Her çalışma sayfası, Aspose.Cells.GridWeb'in bir hücreyi temsil eden bir GridCell nesneleri koleksiyonu olan Cells adlı bir özelliğe sahiptir. Aspose.Cells.GridWeb'i kullanarak herhangi bir hücreye erişmek mümkündür. Bu konuda her biri aşağıda tartışılan iki tercih edilen yöntem vardır.


### **Hücre Adı Kullanarak**
Tüm hücrelerin benzersiz bir adı vardır. Örneğin, A1, A2, B1, B2 vs. Aspose.Cells.GridWeb, geliştiricilere hücre adını (bir dizin olarak) GridWorksheet'in Cells koleksiyonuna geçirerek istenen herhangi bir hücreye erişme imkanı verir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Dikkat**

cells[cellName] ile GridCell'a erişme daha fazla bellek tüketebilir. Bu her zaman yeni bir hücre (GridCell) nesnesi oluşturacaktır, hücre boş olsa bile.


### **Satır ve Sütun Dizinlerini Kullanarak**


Bir hücre ayrıca satır ve sütun dizinleri olarak konumu ile tanınabilir. Tek yapmanız gereken bir hücrenin satır ve sütun dizinlerini GridWorksheet'in Cells koleksiyonuna geçirmektir. Bu yaklaşım yukarıdaki yöntemden daha hızlıdır.

**En İyi Uygulamalar:**

Hücre değerini veya hücre stiline erişmek ve güncelleme işlemini yapmak istemiyorsak, hücre **CheckCell** yöntemini kullanabiliriz, bu durumda hücre mevcut değilse null dönecektir. Bu bellek tasarrufu yapacaktır.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**En İyi Uygulamalar:**
### Hücreler Üzerinde Dolaşma
Eğer çalışma sayfasındaki tüm hücrelere birer birer erişmek istiyorsak, mevcut hücreleri dolaşmak için **yineleyicileri** kullanabiliriz. Bu bellek tasarrufu yapacaktır.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
Aşağıdaki kodu **kötü** olarak karşılaştırın, bu şekilde tüm hücre nesneleri oluşturulacaktır,  boş olup olmadığına bakılmaksızın, bu nedenle bellek sorunlarına yol açacaktır, bu nedenle lütfen bu yöntemi **kullanmayın**
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
