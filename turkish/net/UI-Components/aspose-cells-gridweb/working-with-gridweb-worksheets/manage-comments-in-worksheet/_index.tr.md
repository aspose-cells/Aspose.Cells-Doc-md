---
title: Çalışma Sayfasındaki Yorumları Yönetin
type: docs
weight: 110
url: /tr/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

Bu konuda, çalışma sayfalarına yorum ekleme, çalışma sayfalarına erişme ve çalışma sayfalarından yorum kaldırma anlatılmaktadır. Yorumlar, sayfa ile çalışacak kullanıcılar için notlar veya faydalı bilgiler eklemek için kullanışlıdır. Geliştiriciler, çalışma sayfasının herhangi bir hücresine yorum ekleme esnekliğine sahiptir.

{{% /alert %}} 
## **Yorumlarla Çalışmak**
### **Yorum Ekleme**
Çalışma sayfasına yorum eklemek için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridWeb denetimini Web Formuna ekleyin.
1. Yorum eklediğiniz çalışma sayfasına erişin.
1. Bir hücreye yorum ekleyin.
1. Yeni yorum için bir not ayarlayın.

**Çalışma sayfasına bir yorum eklendi** 

![yapılacaklar:resim_alternatif_Metin](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Yorumlara Erişim**
Bir yoruma erişmek için:

1. Yorumu içeren hücreye erişin.
1. Hücrenin referansını alın.
1. Yoruma erişmek için referansı Yorum koleksiyonuna iletin.
1. Yorumun özelliklerini değiştirmek artık mümkün.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Yorumları Kaldırma**
Bir yorumu kaldırmak için:

1. Yukarıda açıklandığı gibi hücreye erişin.
1. Yorumu kaldırmak için Yorum koleksiyonunun RemoveAt yöntemini kullanın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
