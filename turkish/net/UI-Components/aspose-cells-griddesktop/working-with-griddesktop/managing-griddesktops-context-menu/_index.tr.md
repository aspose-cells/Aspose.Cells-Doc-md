---
title: GridDesktops Bağlam Menüsünü Yönetme
type: docs
weight: 40
url: /tr/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop, yaygın olarak kullanılan tüm komutları içeren bir içerik menüsüne sahiptir. Kontrol, menü öğelerini gizlemenizi/göstermenizi sağlar. Ayrıca, olay işleyicileri ile menüye yeni menü öğeleri eklemek mümkündür.

{{% /alert %}} 
## **giriiş**
ContextMenuManager sınıfı, bağlam menüsü öğelerini yönetmek için kullanılır. GridDesktop.ContextMenuManager özniteliği, ContextMenuManager nesnesinin örneğini alır. Örneğin, ContextMenuManager.MenuItemAvailable_Copy özniteliği, **Kopyala** bağlam menüsü öğesinin kullanılabilir olup olmadığını gösteren bir değer alır veya ayarlar. Benzer şekilde, farklı bağlam menüsü öğeleri için karşılık gelen tüm özniteliklere sahibiz.

**ÖNEMLİ:** Varsayılan olarak, tüm bağlam menüsü öğeleri listede görünür.
## **İçerik Menüsünü Yönetme**
### **Bağlam Menüsü Öğelerini Gizleme**
Bu görevi gerçekleştirmek için önce GridDesktop'un sahip olduğu varsayılan içerik menüsüne bir göz atacağız.

**GridDeskop'un varsayılan menüsü** 

![yapılacaklar:resim_alternatif_Metin](managing-griddesktops-context-menu_1.png)

Şimdi, aşağıdaki kodu kullanarak bazı menü öğelerini gizleyin:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Yukarıdaki kodu çalıştırdıktan sonra, bazı menü öğeleri kullanıcılar tarafından görülemez:

**Bazı menü öğeleri gizlidir** 

![yapılacaklar:resim_alternatif_Metin](managing-griddesktops-context-menu_2.png)
### **Yeni Menü Öğeleri Ekleme**
Aşağıdaki kod parçacığını kullanarak listeye yeni bir bağlam menüsü öğesi ekleyin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Ayrıca yeni komut/seçenek için bir olay işleyicisi belirliyoruz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Yukarıdaki kodu çalıştırdıktan sonra, bağlam menüsünde yeni bir menü öğesi görülebilir. Hücre tıklandığında da bir mesaj görünecektir.

**Listeye yeni bir menü öğesi eklendi** 

![yapılacaklar:resim_alternatif_Metin](managing-griddesktops-context-menu_3.png)
