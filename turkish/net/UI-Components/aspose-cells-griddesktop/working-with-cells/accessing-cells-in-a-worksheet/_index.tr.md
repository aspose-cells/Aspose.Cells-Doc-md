---
title: Bir Çalışsayfadaki GridCell e Erişim
type: docs
weight: 10
url: /tr/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: Bu makale, GridDesktop teki Çalışsayfadaki hücre nesnesine (GridCell) nasıl alacağınızı tanıtır.
---

{{% alert color="primary" %}} 

Bugüne kadar çalışsayfalar, satırlar ve sütunlarla ilgili konuştuk ancak bu hücreler hakkında daha derinlere inme ve hücreler hakkında konuşma zamanı geldi. Bu konuda, hücrelerle ilgili tartışmamıza hücrelere erişmenin temel bir özelliği ile başlayacağız.

{{% /alert %}} 
## **Bir Çalışsayfadaki Hücreye Erişim**
Aspose.Cells.GridDesktop'in API'si kullanılarak bir çalışsayfadaki herhangi bir hücreye erişebiliriz. Aşağıdaki gibi hücreye erişmenin üç mümkün yolu olabilir:

- **Hücre Adını Kullanarak**
- **Satır ve Sütun İndekslerini kullanarak**
- **Odaklanmış Hücreyi Almak**

Yukarıdaki üç yaklaşımı sırayla tartışalım.
### **Hücre Adı Kullanarak**
Çalışsayfadaki tüm hücrelerin benzersiz bir adı vardır. Örneğin, A1, A2, B1, B2 vb. Aspose.Cells.GridDesktop, istenen herhangi bir hücreye, sadece hücre adını (bir dizin olarak) **Worksheet**'in **Cells** koleksiyonuna ileterek erişmeyi sağlar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Dikkat**

cells[cellName] ile GridCell'a erişme daha fazla bellek tüketebilir. Bu her zaman yeni bir hücre (GridCell) nesnesi oluşturacaktır, hücre boş olsa bile.

### **Hücrenin Satır ve Sütun İndekslerini Kullanma**

**En İyi Uygulamalar:**

Hücre değerini veya hücre stiline erişmek ve güncelleme işlemini yapmak istemiyorsak, hücre **CheckCell** yöntemini kullanabiliriz, bu durumda hücre mevcut değilse null dönecektir. Bu bellek tasarrufu yapacaktır.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Satır ve sütun indislerini kullanarak bir hücreye erişme
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

Bir çalışma sayfasındaki bir hücre, satır ve sütun indisleri açısından konumunu kullanarak da tanımlanabilir. Yapmamız gereken tek şey, hücrenin satır ve sütun indislerini **Worksheet**'in **Cells** koleksiyonuna iletmektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Dikkat**

cells[rowIndex, columnIndex] kullanarak Hücreye Erişme, daha fazla bellek tüketebilir. Bu, hücre null olsun ya da olmasın her zaman yeni bir hücre (GridCell) nesnesi oluşturacaktır.


### **Odaklanan Hücreyi Alma**
Eğer kesin olarak hangi hücreye erişileceğini bilmiyorsanız, Aspose.Cells.GridDesktop aynı zamanda bir kullanıcının odaklandığı bir hücreye erişmenize de izin verir. Bu özelliği kullanarak bir kullanıcıya herhangi bir hücreyi seçme ve ardından bu hücreye backend tarafında erişme imkanı elde edersiniz. Bunun basitçe yapılabilmesi için **Worksheet**'in **GetFocusedCell** metodunu kullanılabilir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**En İyi Uygulamalar:**
### Hücreler Üzerinde Dolaşma
Eğer çalışma sayfasındaki tüm hücrelere birer birer erişmek istiyorsak, mevcut hücreleri dolaşmak için **yineleyicileri** kullanabiliriz. Bu bellek tasarrufu yapacaktır.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
Aşağıdaki kodu **kötü** olarak karşılaştırın, bu şekilde tüm hücre nesneleri oluşturulacaktır,  boş olup olmadığına bakılmaksızın, bu nedenle bellek sorunlarına yol açacaktır, bu nedenle lütfen bu yöntemi **kullanmayın**
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

