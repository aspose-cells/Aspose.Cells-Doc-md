---
title: Özel Komut Düğmeleri Oluşturun
type: docs
weight: 100
url: /tr/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb gibi özel düğmeler içerir**Göndermek**, **Kayıt etmek** ve**Geri alma**. Tüm bu düğmeler, Aspose.Cells.GridWeb için belirli görevleri yerine getirir.
Özel görevleri gerçekleştiren özel düğmeler eklemek de mümkündür. Bu konuda, bu özelliğin nasıl kullanılacağı açıklanmaktadır.

{{% /alert %}} 
## **Özel Komut Düğmeleri Oluşturma**
Aspose.Cells.GridWeb'de özel bir komut düğmesi oluşturmak için:

1. Web formuna Aspose.Cells.GridWeb denetimi ekleyin.
1. Bir çalışma sayfasına erişin.
1. CustomCommandButton sınıfının bir örneğini oluşturun.
1. Düğmenin Komutunu bir değere ayarlayın. Bu değer, düğmenin olay işleyicisinde kullanılır.
1. Düğmenin metnini ayarlayın.
1. Düğmenin resim URL'sini ayarlayın.
1. Son olarak, CustomCommandButton nesnesini GridWeb denetiminin CustomCommandButtons koleksiyonuna ekleyin.

{{% alert color="primary" %}} 

Visual Studio'nun Özellikler iletişim kutusu kullanılarak WYSIWYG modunda özel komut düğmeleri de eklenebilir.

{{% /alert %}} 

Kod parçacığının çıktısı aşağıda gösterilmiştir:

**GridWeb kontrolüne eklenen özel bir komut düğmesi** 

![yapılacaklar:resim_alternatif_metin](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Özel Komut Düğmesinin Olay İşleme**
Özel komut düğmelerinin en önemli yönü, tıklandığında gerçekleştirdikleri eylemdir. Eylemi ayarlamak için GridWeb denetiminin CustomCommand olayı için bir olay işleyicisi oluşturun.

CustomCommand olayı, her zaman özel bir komut düğmesine tıklandığında tetiklenir. Bu nedenle, olay işleyici, düğmeyi GridWeb denetimine eklerken Komut kümesi tarafından uygulanan belirli özel komut düğmesini tanımlamalıdır. Son olarak, düğme tıklandığında yürütülen özel kodu ekleyin.

Aşağıdaki kod örneğinde butona tıklandığında A1 hücresine bir metin mesajı eklenmektedir.

**Özel komut düğmesi tıklandığında A1 hücresine eklenen metin** 

![yapılacaklar:resim_alternatif_metin](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
