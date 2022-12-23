---
title: GridWeb'de Bağlam Menüsü Öğeleri Ekleme veya Kaldırma
type: docs
weight: 130
url: /tr/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

ASP.NET işaretlemesini veya .NET kodunu kullanarak bağlam menüsü öğeleri ekleyebilirsiniz. .NET kodunu kullanarak bağlam menüsü öğelerini de kaldırabilirsiniz. Lütfen bu amaçla GridWeb.CustomCommandButtons.Add() ve GridWeb.CustomCommandButtons.Remove() veya RemoveAt() yöntemlerini kullanın.

{{% /alert %}} 
## **ASP.NET İşaretlemesini Kullanarak Bağlam Menüsü Öğesi Ekleme**
Aşağıdaki ASP.NET işaretlemesi, GridWeb'e bağlam menüsü öğesi ekler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



İşte yukarıdaki bağlam menüsü öğesiyle bir GridWeb oluşturan tam ASP.NET işaretlemesi. Lütfen OnCustomCommand="GridWeb1_CustomCommand" özniteliğine dikkat edin. Bağlam menüsü öğeniz tıklandığında çağrılacak olay işleyici adıdır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Yukarıdaki ASP.NET işaretlemesi kullanılarak eklendikten sonra içerik menüsü öğesi bu şekilde görünür.

![yapılacaklar:resim_alternatif_metin](add-or-remove-context-menu-items-in-gridweb_1.png)

Bu, bağlam menüsü öğesi tıklandığında yürütülen olay işleyici kodudur. Kod önce komut adını kontrol eder, bizim komutumuzla eşleşirse, aktif GridWeb çalışma sayfasının A1 hücresine bir metin ekler ve metni görünür kılmak için ilk sütun genişliğini 40 birim olarak ayarlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Bağlam menüsü öğesine tıkladığınızda GridWeb böyle görünür.

![yapılacaklar:resim_alternatif_metin](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Kod Kullanarak Aspose.Cells.GridWeb'de Bağlam Menüsü Öğeleri Ekleme**
Bu kod, kod kullanarak bir GridWeb içine bağlam menüsü öğesinin nasıl ekleneceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Kod Kullanarak Aspose.Cells.GridWeb'deki Bağlam Menüsü Öğelerini Kaldırma**
Bu kod, CustomCommandButtons.Remove() ve CustomCommandButtons.RemoveAt() yöntemleri kullanılarak bağlam menüsü öğesinin nasıl kaldırılacağını gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
