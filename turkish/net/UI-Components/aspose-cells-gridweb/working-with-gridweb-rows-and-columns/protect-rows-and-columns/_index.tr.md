---
title: Satırları ve Sütunları Koru
type: docs
weight: 60
url: /tr/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

Bu konuda, satır ve sütunlardaki hücreleri son kullanıcılar tarafından gerçekleştirilen her türlü eylemden korumaya yönelik birkaç teknik ele alınmaktadır. Geliştiriciler bu korumayı iki teknik kullanarak uygulayabilir: satır ve sütunlardaki hücreleri salt okunur yaparak veya Aspose.Cells.GridWeb'in bağlam menüsü seçeneklerini kısıtlayarak. Bu tekniklerin her ikisi de aşağıda örnekler yardımıyla tartışılmaktadır.

{{% /alert %}} 
## **Satırlar ve Sütunlarda Cells'i koruma**
### **Satırları ve Sütunları Salt Okunur Hale Getirme**
Çalışma sayfasındaki satırları ve sütunları korumanın bir yolu, hücreleri salt okunur yapmaktır. Daha sonra son kullanıcılar tarafından silinemezler.

Satırları ve sütunları salt okunur yapmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Koleksiyondaki GridWorksheet'e erişin.
1. Satırlarda veya sütunlarda istediğiniz hücreleri salt okunur olarak ayarlayın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Bağlam Menüsü Seçeneklerini Kısıtlama**
Aspose.Cells.GridWeb, son kullanıcıların kontrol üzerinde işlem yapmak için kullanabilecekleri bir içerik menüsü sağlar. Menü, hücreleri, satırları ve sütunları değiştirmek için birçok seçenek sunar.

**Eksiksiz bağlamsal seçenekler** 

![yapılacaklar:resim_alternatif_Metin](protect-rows-and-columns_1.png)

Bağlam menüsünde bulunan seçenekleri kısıtlayarak, satırlar ve sütunlar üzerinde her türlü istemci tarafı işlemini kısıtlamak mümkündür. GridWeb denetiminin EnableClientColumnOperations ve EnableClientRowOperations özelliklerini false olarak ayarlayarak yapılabilir. GridWeb denetiminin EnableClientFreeze özelliğini false olarak ayarlayarak kullanıcıların satırları ve sütunları dondurmasını kısıtlamak da mümkündür.

**Satır ve sütun seçeneklerini kısıtladıktan sonra içerik menüsü** 

![yapılacaklar:resim_alternatif_Metin](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
