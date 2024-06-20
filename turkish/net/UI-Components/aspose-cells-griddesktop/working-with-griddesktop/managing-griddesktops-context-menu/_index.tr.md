---
title: GridDesktop ın Bağlam Menüsünü Yönetme
type: docs
weight: 40
url: /tr/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop, bağlam, bağlam menüsü
description: Bu makale, GridDesktop ta bağlam menüsünü nasıl özelleştireceğinizi tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop'un tüm yaygın olarak kullanılan komutları içeren bir bağlam menüsü bulunmaktadır. Kontrol, menü öğelerini gizlemeye/göstermeye izin verir. Ayrıca, menüye yeni menü öğeleri eklemek de mümkündür ve bunlara etkinlik yöneticileri eklemek de mümkündür.

{{% /alert %}} 
## **Giriş**
ContextMenuManager sınıfı, bağlam menü öğelerini yönetmek için kullanılır. GridDesktop.ContextMenuManager özniteliği, ContextMenuManager nesnesinin örneğini alır. Örneğin, ContextMenuManager.MenuItemAvailable_Copy özniteliği, bağlam menü öğesi **Kopyala**'nın mevcut olup olmadığını belirten bir değer alır veya bu değeri ayarlar. Benzer şekilde, farklı bağlam menü öğeleri için tüm karşılık gelen özniteliklere sahibiz.

**ÖNEMLİ:** Varsayılan olarak, tüm bağlam menü öğeleri listede görünür.
## **Bağlam Menüsünü Yönetme**
### **Bağlam Menü Öğelerini Gizleme**
Bu görevi gerçekleştirmek için öncelikle GridDesktop'un varsayılan bağlam menüsüne bakalım.

**GridDeskop'un varsayılan menüsü** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

Şimdi, aşağıdaki kodu kullanarak bazı menü öğelerini gizleyin:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Yukarıdaki kodu çalıştırdıktan sonra, bazı menü öğeleri kullanıcılar için görünmez olacaktır:

**Bazı menü öğeleri gizlendi** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **Yeni Menü Öğeleri Ekleme**
Aşağıdaki kod parçasını kullanarak listeye yeni bir bağlam menü öğesi ekleyin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Ayrıca, yeni komut/seçenek için bir etkinlik yöneticisi belirtiyoruz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Yukarıdaki kodu çalıştırdıktan sonra, bağlam menüsünde yeni bir menü öğesi görünebilir. Bir hücre tıklandığında ayrıca bir ileti de görünecektir.

**Listeye yeni bir menü öğesi eklendi** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
