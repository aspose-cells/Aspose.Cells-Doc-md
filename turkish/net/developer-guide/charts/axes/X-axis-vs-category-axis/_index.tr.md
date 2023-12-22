---
title: X Ekseni Vs. Kategori Ekseni
description: Aspose.Cells for .NET numaralı telefondan X ekseni ile Kategori eksenini nasıl ayırt edeceğinizi öğrenin. Kılavuzumuz bunların kullanım ve özelliklerindeki farkları ve bunları ihtiyaçlarınıza göre nasıl yapılandıracağınızı anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /tr/net/X-axis-vs-category-axis/
---
##  **Olası Kullanım Senaryoları**
Farklı türde X eksenleri vardır. Y ekseni bir Değer türü ekseni iken, X ekseni bir Kategori türü ekseni veya Değer türü ekseni olabilir. Değer ekseni kullanıldığında, veriler sürekli değişen sayısal veriler olarak ele alınır ve işaretçi, eksen boyunca sayısal değerine göre değişen bir noktaya yerleştirilir. Kategori ekseni kullanıldığında veriler, sayısal olmayan metin etiketleri dizisi olarak ele alınır ve işaretçi, dizideki konumuna göre eksen boyunca bir noktaya yerleştirilir. Aşağıdaki örnek Değer ve Kategori Eksenleri arasındaki farkı göstermektedir.
 Örnek verilerimiz aşağıdaki şekilde gösterilmiştir.[örnek Tablo dosyası](sample.png) altında. İlk sütun, Kategoriler veya Değerler olarak değerlendirilebilecek X ekseni verilerimizi içerir. Sayıların eşit aralıklı olmadığını ve hatta sayısal sırada görünmediğini unutmayın.

![yapılacak şey:image_alt_text](sample.png)
##  **Microsoft Excel gibi X ve Kategori eksenini kullanın**
Bu verileri iki tür grafikte göstereceğiz, ilk grafik Değer Ekseni olarak XY (Dağılım) grafiği X, ikinci grafik ise Kategori Ekseni olarak çizgi grafiği X'tir.

![yapılacak şey:image_alt_text](compare.png)
##  **Basit kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
