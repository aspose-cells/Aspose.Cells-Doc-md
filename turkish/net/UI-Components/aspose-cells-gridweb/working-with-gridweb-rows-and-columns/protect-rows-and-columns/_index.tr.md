---
title: Satırları ve Sütunları Koruma
type: docs
weight: 60
url: /tr/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb,koruma
description: Bu makale, GridWeb de satırları ve sütunları korumanın nasıl yapılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konu, geliştiricilerin kullanıcılar tarafından gerçekleştirilen her türlü eylemden satırlarda ve sütunlardaki hücreleri koruması için birkaç teknik tartışmaktadır. Geliştiriciler, hücreleri satırlarda ve sütunlarda salt okunur yaparak veya Aspose.Cells.GridWeb'in bağlam menüsü seçeneklerini sınırlayarak bu korumayı uygulayabilirler. Bu tekniklerin her ikisi de aşağıda örneklerle tartışılmıştır.

{{% /alert %}} 
## **Satırlarda ve Sütunlarda Hücreleri Koruma**
### **Satırları ve Sütunları Salt Okunur Yapma**
Bir çalışma sayfasında satırları ve sütunları korumanın bir yolu hücreleri salt okunur yapmaktır. Böylece, kullanıcılar tarafından silinemiyorlar.

Satırları ve sütunları salt okunur yapma:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Koleksiyondaki GridWorksheet'e erişin.
1. Satırlardaki veya sütunlardaki istenen hücreleri salt okunur olarak ayarlayın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Bağlam Menü Seçeneklerini Kısıtlama**
Aspose.Cells.GridWeb, kullanıcıların denetimi üzerinde işlemler yapmaları için bir bağlam menüsü sağlar. Bu menü, hücreleri, satırları ve sütunları manipüle etmek için birçok seçenek sağlar.

**Tüm bağlamsal seçenekler** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

Bağlam menüsünde sunulan seçenekleri kısıtlayarak her türlü istemci tarafı işlemini kısıtlamak mümkündür. GridWeb kontrolünün EnableClientColumnOperations ve EnableClientRowOperations özelliklerini false olarak ayarlayarak bunu yapmak mümkündür. Ayrıca, GridWeb kontrolünün EnableClientFreeze özelliğini false olarak ayarlayarak kullanıcıların satır ve sütun dondurmalarını da kısıtlamak mümkündür.

**Satır ve sütun seçenekleri kısıtlandıktan sonra bağlam menüsü** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
