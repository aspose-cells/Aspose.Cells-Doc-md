---
title: Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun
type: docs
weight: 340
url: /tr/net/change-cells-alignment-and-keep-existing-formatting/
---
## **Olası Kullanım Senaryoları**

Bazen birden çok hücrenin hizalamasını değiştirmek, ancak mevcut biçimlendirmeyi de korumak istersiniz. Aspose.Cells, bunu kullanarak yapmanızı sağlar.[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) Emlak. eğer ayarlayacaksan**doğru** , aksi takdirde hizalama değişiklikleri gerçekleşecektir. Lütfen aklınızda bulundurun,[**Stil Bayrağı**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) nesne parametre olarak iletilir[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)biçimlendirmeyi gerçekten bir hücre aralığına uygulayan yöntem.

## **Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun**

 Aşağıdaki örnek kod,[örnek excel dosyası](67338585.xlsx) , aralığı oluşturur ve ortalayarak yatay ve dikey olarak hizalar ve mevcut biçimlendirmeyi olduğu gibi tutar. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını karşılaştırır ve[çıktı excel dosyası](67338586.xlsx)ve hücrelerin mevcut tüm biçimlendirmesinin aynı olduğunu, ancak hücrelerin artık yatay ve dikey olarak ortaya hizalanmış olduğunu gösterir.

![yapılacaklar:resim_alternatif_metin](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
