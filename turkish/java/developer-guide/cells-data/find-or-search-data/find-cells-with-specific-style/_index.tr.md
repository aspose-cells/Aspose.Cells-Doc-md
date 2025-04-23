---
title: Belirli bir stil ile hücreleri bul
type: docs
weight: 80
url: /tr/java/find-cells-with-specific-style/
description: Bu makale, MS Excel ve Aspose.Cells for Java API kullanarak belirli bir stile sahip hücreleri bulmanın nasıl yapıldığını göstermektedir.
keywords: belirli bir stile sahip hücreleri bul, belirli bir stile sahip hücreleri bul excel, belirli bir stile sahip hücreleri bul excel java, belirli bir stile sahip hücreleri ara, belirli bir stile sahip hücreleri ara excel, belirli bir stile sahip hücreleri ara excel java, belirli bir stile sahip hücreleri bulmanın yolları, belirli bir stile sahip hücreleri bulmanın yolları excel, belirli bir stile sahip hücreleri bulmanın yolları excel java
---

{{% alert color="primary" %}}

Bazen, belirli bir stile sahip hücreleri bulmanız gerekebilir. Bu makale, bu işlemi Microsoft Excel ve Aspose.Cells for Java API kullanarak nasıl gerçekleştireceğinizi göstermektedir.

{{% /alert %}}

## Microsoft Excel Kullanarak

MS Excel'de belirli stillerdeki hücreleri aramak için gereken adımlar şunlardır.

1. **Ana Sekme**'de **Bul & Seç** seçin.
1. **Bul**'u seçin.
1. Gelişmiş seçenekler görünmüyorsa **Seçenekler**'ü tıklayın.
1. **Biçim** açılır menüsünden **Hücreden Biçim Seç...**'i seçin.
1. Aramak istediğiniz stile benzer bir hücreyi seçin.
1. **Tümünü Bul** seçeneğini belirli stile sahip tüm hücreleri bulmak için tıklayın.

## Aspose.Cells for Java Kullanarak

Aspose.Cells for Java, çalışma sayfasındaki belirli bir stile sahip hücreleri bulma özelliği sağlar. Bu amaçla, API [**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) özelliğini sağlar.

### Örnek Kod

Aşağıdaki kod parçası, **A1** hücresiyle aynı stildeki tüm hücreleri bulur ve bu hücrelerin içindeki metni değiştirir. Lütfen kaynak ve çıktı dosyalarının ekran görüntüsünü inceleyerek örnek kodun çıktısını analiz edin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Kodun çalıştırılmasından sonra, A1 hücresinin stiliyle aynı stile sahip tüm hücrelerde "Bulundu" metni olacaktır.

### Ekran Görüntüleri

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**Şekil:** Stilleri olan hücrelere sahip kaynak dosya

Aşağıdaki kod tarafından oluşturulan çıktı dosyası. **A1** hücresiyle aynı stile sahip tüm hücreleri "Bulundu" metnini görebilirsiniz

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**Şekil:** **A1** stiline göre arama sonrası bulunan hücrelerin çıktı dosyası
{{< app/cells/assistant language="java" >}}
