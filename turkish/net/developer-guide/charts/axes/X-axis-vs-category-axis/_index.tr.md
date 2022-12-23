---
title: X Ekseni Vs. Kategori Ekseni
type: docs
weight: 180
url: /tr/net/X-axis-vs-category-axis/
---
## **Olası Kullanım Senaryoları**
Farklı tipte X eksenleri vardır. Y ekseni bir Değer türü ekseni iken, X ekseni bir Kategori türü ekseni veya bir Değer türü ekseni olabilir. Bir Değer ekseni kullanılarak, veriler sürekli değişen sayısal veriler olarak ele alınır ve işaretçi, sayısal değerine göre değişen eksen boyunca bir noktaya yerleştirilir. Bir Kategori ekseni kullanılarak, veriler sayısal olmayan metin etiketleri dizisi olarak ele alınır ve işaretçi, dizideki konumuna göre eksen boyunca bir noktaya yerleştirilir. Aşağıdaki örnek, Değer ve Kategori Eksenleri arasındaki farkı göstermektedir.
 Örnek verilerimiz aşağıda gösterilmiştir.[örnek Tablo dosyası](sample.png) altında. İlk sütun, Kategoriler veya Değerler olarak ele alınabilecek X ekseni verilerimizi içerir. Sayıların eşit aralıklı olmadığına ve hatta sayısal sırayla görünmediğine dikkat edin.

![yapılacaklar:resim_alternatif_metin](sample.png)
## **Microsoft Excel gibi X ve Kategori eksenini kullanın**
Bu verileri iki tür grafikte göstereceğiz, ilk grafik Değer Ekseni olarak XY (Dağılım) grafiği X, ikinci grafik Kategori Ekseni olarak X çizgi grafiğidir.

![yapılacaklar:resim_alternatif_metin](compare.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
