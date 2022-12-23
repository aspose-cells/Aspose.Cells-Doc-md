---
title: Belirli bir stile sahip hücreleri bulun
type: docs
weight: 80
url: /tr/java/find-cells-with-specific-style/
description: Bu makale, MS Excel ve Aspose.Cells for Java API kullanarak belirli stile sahip hücrelerin nasıl bulunacağını gösterir.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

Bazen, belirli bir stile sahip hücreleri bulmanız gerekir. Bu makale, Microsoft Excel'in yanı sıra Aspose.Cells for Java API kullanarak bunu nasıl başaracağınızı gösterir.

{{% /alert %}}

## Microsoft Excel'i kullanma

Bunlar, MS Excel'de belirli stillere sahip hücreleri aramak için gereken adımlardır.

1.  Seçme**Bul ve Seç** içinde**Ana Sayfa Sekmesi**.
1.  Seçme**Bulmak**.
1.  Tıklamak**Seçenekler**gelişmiş seçenekler görünmüyorsa.
1.  Seçme**Cell'den Biçimi Seçin...** dan**Biçim** yıkılmak.
1. Aramak istediğiniz stile sahip hücreyi seçin.
1.  Tıklamak**Hepsini bul** Seçtiğiniz hücreye benzer stile sahip tüm hücreleri bulmak için.

## Aspose.Cells for Java'i kullanma

 Aspose.Cells for Java, çalışma sayfasında belirli bir stille hücreleri bulma özelliğini sağlar. Bunun için API şunları sağlar:[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) Emlak.

### Basit kod

 Aşağıdaki kod parçacığı, cell ile aynı stile sahip tüm hücreleri bulur.**A1** ve bu hücrelerin içindeki metni değiştirir. Örnek kodun çıktısını analiz etmek için lütfen kaynak ve çıktı dosyalarının ekran görüntüsüne bakın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Kodun yürütülmesinden sonra, A1 hücresi ile aynı stile sahip tüm hücrelerde "Bulundu" metni olacaktır.

### Ekran görüntüleri

![yapılacaklar:resim_alternatif_metin](find-cells-with-specific-style_1.png)

**Figür:** Stilleri olan hücrelere sahip kaynak dosya

 İşte aşağıdaki kod tarafından oluşturulan çıktı dosyasıdır. Hücre ile aynı stile sahip tüm hücreleri görebilirsiniz.**A1** "Bulundu" metni var

![yapılacaklar:resim_alternatif_metin](find-cells-with-specific-style_2.png)

**Figür:**Şuna göre arama yaptıktan sonra bulunan hücrelerle çıktı dosyası**A1** stil
