---
title: X Ekseni ve Kategori Ekseni Arasındaki Fark
description: Aspose.Cells for Java de X ekseni ile Kategori ekseni arasındaki farkı nasıl ayırt edeceğinizi öğrenin. Rehberimiz, bunların kullanımı ve özelliklerindeki farklılıkları anlamanıza ve ihtiyaçlarınıza göre nasıl yapılandıracağınıza yardımcı olacaktır.
keywords: Aspose.Cells for Java, X ekseni, Kategori eksen, fark, kullanım, özellikler, yapılandırma.
type: docs
weight: 180
url: /tr/java/x-axis-vs-category-axis/
---

## **Olası Kullanım Senaryoları**
Farklı türde X ekseni bulunmaktadır. Y ekseni Bir Değer tipi ekseni iken X ekseni Kategori tipi eksen veya Değer tipi eksen olabilir. Değer eksenini kullanarak, veri sürekli değişen sayısal veri olarak işlenir ve işaretçi, numerik değerine göre değişen bir noktaya yerleştirilir. Kategori ekseni kullanarak, veri, sayısal olmayan metin etiketlerinden oluşan bir dizi olarak işlenir ve işaretçi, dizideki konumuna göre eksen boyunca bir noktaya yerleştirilir. Aşağıdaki örnek, Değer ve Kategori Eksenleri arasındaki farkı açıklar.
Örnek verilerimiz [örnek Tablo dosyasında](sample.png) gösterilmektedir. İlk sütun, Kategori veya Değer olarak işleme alınabilen X ekseni verilerimizi içerir. Sayıların eşit aralıklarla dağılmadığına veya hatta sayısal sırayla görünmediğine dikkat edin.

![todo:image_alt_text](sample.png)
## **X ve Kategori eksenini Microsoft Excel gibi ele alın**
Bu verileri iki tür grafikte göstereceğiz, birinci grafik XY (Saçılım) grafiği X olarak Değer Ekseni, ikinci grafik ise Kategori Ekseni olarak çizgi grafiğidir.

![todo:image_alt_text](compare.png)

Aşağıdaki örnek kod [çıkış Excel dosyasını](XAxis.xlsx) üretir.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
{{< app/cells/assistant language="java" >}}
