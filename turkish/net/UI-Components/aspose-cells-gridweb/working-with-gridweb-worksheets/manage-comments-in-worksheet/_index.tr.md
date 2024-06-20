---
title: Çalışma Sayfasında Yorumları Yönet
type: docs
weight: 110
url: /tr/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: Bu makale, GridWeb deki yorumlarla çalışmayı tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konu, çalışsayfalardan yorum eklemeyi, erişmeyi ve kaldırmayı tartışır. Yorumlar, çalışsayfa ile çalışacak olan kullanıcılar için not veya kullanışlı bilgiler eklemek için kullanışlıdır. Geliştiriciler, çalışsayfanın herhangi bir hücresine yorum eklemekte esneklik sahip olurlar.

{{% /alert %}} 
## **Yorumlarla Çalışma**
### **Yorum Ekleme**
Bir çalışsayfaya yorum eklemek için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridWeb denetimini Web Formuna ekleyin.
2. Yorum eklemek istediğiniz çalışsayfaya erişin.
1. Bir hücreye yorum ekleyin.
4. Yeni yorum için bir not ayarlayın.

**Çalışsayfaya bir yorum eklenmiştir** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Yorumlara Erişme**
Bir yoruma erişmek için:

1. Yorum içeren hücreye erişin.
2. Hücrenin referansını alın.
3. Yoruma erişmek için referansı Comment koleksiyonuna iletil.
1. Artık yorumun özelliklerini değiştirmek mümkün.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Yorumları Kaldırma**
Bir yorumu kaldırmak için:

1. Yukarıda açıklandığı gibi hücreye erişin.
1. Yorum koleksiyonunun RemoveAt yöntemini kullanarak yorumu kaldırın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
