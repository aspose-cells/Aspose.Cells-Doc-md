---
title: Excel de Bir Aralıktaki Verileri Arama ve Değiştirme
type: docs
weight: 60
url: /tr/java/search-and-replace-data-in-a-range/
description: Bu makale, Java kodu kullanarak bir Excel deki bir aralıktaki verileri arama ve değiştirme konusunu ele almaktadır.
keywords: java da excel de veri arama ve değiştirme, java da excel de veri arama, java da aralıktaki veri arama ve değiştirme, java da aralıktaki veri arama, java da bir aralıktaki veri arama, java da bir aralıktaki veri arama, java da bir aralıktaki veri arama, java da veri arama ve değiştirme, java da bir aralıktaki veri arama, java ile excel de veri arama ve değiştirme, java ile bir aralıktaki veri arama ve değiştirme, java ile aralıktaki veri arama ve değiştirme
---

{{% alert color="primary" %}}

Bazen, istenen aralık dışındaki hücre değerlerini yoksayarak belirli verileri aramak ve değiştirmek gerekebilir. Aspose.Cells, bir arama işlemini belirli bir aralıkla sınırlandırmanıza olanak tanır. Bu makale, bunun nasıl yapıldığını açıklamaktadır.

{{% /alert %}}

Aspose.Cells, veri arama işlemi için bir aralığı belirtmek için [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange-com.aspose.cells.CellArea-) yöntemini sağlar.

Varsayalım ki **"arama"** dizesini **"değiştir"** ile değiştirmek istiyoruz ve bu işlemi **E3:H6** aralığında yapmak istiyoruz. Aşağıdaki ekran görüntüsünde, **"arama"** dizesi birkaç hücrede görülebilir ancak yalnızca belirli bir aralıkta, burada sarı ile vurgulanmış olan alanda, değiştirmek istiyoruz.

**Giriş dosyası**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

Kodun çalıştırılmasından sonra, çıktı dosyası aşağıdaki gibi görünecektir. Belirtilen aralık içindeki tüm "arama" dizeleri "değiştir" ile değiştirilmiştir.

**Çıkış dosyası**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## İlgili Makaleler

- [Veri Bulma veya Arama](/cells/tr/java/find-or-search-data/)
{{< app/cells/assistant language="java" >}}
