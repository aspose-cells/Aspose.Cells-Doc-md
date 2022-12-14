---
title: Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun
type: docs
weight: 260
url: /tr/java/change-cells-alignment-and-keep-existing-formatting/
---
## **Olası Kullanım Senaryoları**

Bazen birden çok hücrenin hizalamasını değiştirmek, ancak mevcut biçimlendirmeyi de korumak istersiniz. Aspose.Cells, bunu kullanarak yapmanızı sağlar.[**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) Emlak. eğer ayarlayacaksan**doğru** , aksi takdirde hizalama değişiklikleri gerçekleşecektir. Lütfen aklınızda bulundurun,[**Stil Bayrağı**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) nesne parametre olarak iletilir[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) biçimlendirmeyi hücre aralığına fiilen uygulayan yöntem.

## **Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun**

Aşağıdaki örnek kod,[örnek excel dosyası](67338592.xlsx), aralığı oluşturur ve ortalayarak yatay ve dikey olarak hizalar ve mevcut biçimlendirmeyi olduğu gibi tutar. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını karşılaştırır ve[çıktı excel dosyası](67338591.xlsx)ve hücrelerin mevcut tüm biçimlendirmesinin aynı olduğunu, ancak hücrelerin artık yatay ve dikey olarak ortaya hizalanmış olduğunu gösterir.

![yapılacaklar:resim_alternatif_Metin](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
