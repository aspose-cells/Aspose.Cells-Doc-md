---
title: Aspose.Cells.GridWeb de İçerik Menü Öğeleri Ekle veya Kaldır
type: docs
weight: 130
url: /tr/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb, contextmenu, menü
description: Bu makale, GridWeb de içerik menü öğeleri eklemeyi veya kaldırmayı nasıl tanıttığını açıklar.
---

{{% alert color="primary" %}} 

ASP.NET işaretleme dilini veya .NET kodunu kullanarak içerik menü öğeleri ekleyebilir veya kaldırabilirsiniz. Ayrıca, .NET kodunu kullanarak içerik menü öğelerini kaldırabilirsiniz. Bu amaçlar için GridWeb.CustomCommandButtons.Add() ve GridWeb.CustomCommandButtons.Remove() veya RemoveAt() yöntemlerini kullanınız.

{{% /alert %}} 
## **ASP.NET İşaretleme Dilini Kullanarak İçerik Menü Öğesi Ekleme**
Aşağıdaki ASP.NET işaretleme, GridWeb'de içerik menü öğesini ekler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



İşte yukarıdaki içerik menü öğesini içeren bir GridWeb oluşturan tam ASP.NET işaretleme. Lütfen OnCustomCommand="GridWeb1_CustomCommand" özniteliğine dikkat edin. Bu, içerik menü öğeniz tıklanıldığında çağrılacak olay işleyici adıdır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Yukarıdaki ASP.NET işaretleme ile eklenen içerik menü öğesi böyle görünmektedir.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Bu, içerik menü öğesi tıklandığında yürütülen olay işleyici kodudur. Kod öncelikle komut adını kontrol eder, eşleşirse, etkin GridWeb çalışsayfasında A1 hücresine bir metin ekler ve metni görmek için birinci sütun genişliğini 40 birime ayarlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


İçerik menü öğesine tıkladığınızda GridWeb'in görünümü budur.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Aspose.Cells.GridWeb'de Kod Kullanarak İçerik Menü Öğeleri Ekleme**
Bu kod, kod kullanarak GridWeb'in içine içerik menü öğesi eklemenin nasıl yapıldığını gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Aspose.Cells.GridWeb'de Kod Kullanarak İçerik Menü Öğeleri Kaldırma**
Bu kod, CustomCommandButtons.Remove() ve CustomCommandButtons.RemoveAt() yöntemlerini kullanarak içerik menü öğesi kaldırmanın nasıl yapıldığını gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
