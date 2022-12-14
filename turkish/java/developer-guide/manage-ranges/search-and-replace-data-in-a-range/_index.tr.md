---
title: Bir Aralıktaki Verileri Arayın ve Değiştirin
type: docs
weight: 60
url: /tr/java/search-and-replace-data-in-a-range/
description: Bu makale, Java kodunu kullanarak Excel'de bir aralıktaki verilerin nasıl aranacağını ve değiştirileceğini gösterir.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

Bazen, istenen aralığın dışındaki tüm hücre değerlerini yok sayarak bir aralıktaki belirli verileri aramanız ve değiştirmeniz gerekir. Aspose.Cells, bir aramayı belirli bir aralıkla sınırlamanıza izin verir. Bu makale nasıl yapılacağını açıklıyor.

{{% /alert %}}

Aspose.Cells şunları sağlar:[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) veri ararken bir aralık belirtmek için yöntem.

 Dizeyi aramak istediğinizi varsayalım**"arama"** ve onunla değiştir**"yer değiştirmek"** aralıkta**E3:H6**. Aşağıdaki ekran görüntüsünde, "arama" dizesi birkaç hücrede görülebilir, ancak biz onu yalnızca belirli bir aralıkta değiştirmek istiyoruz, burada sarı renkle vurgulanmıştır.

**Giriş dosyası**

![yapılacaklar:resim_alternatif_Metin](search-and-replace-data-in-a-range_1.png)

Kodun çalıştırılmasından sonra çıktı dosyası aşağıdaki gibi görünür. Aralık içindeki tüm "arama" dizeleri "değiştir" ile değiştirilmiştir.

**Çıktı dosyası**

![yapılacaklar:resim_alternatif_Metin](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## İlgili Makaleler

- [Veri Bul veya Ara](/cells/tr/java/find-or-search-data/)
