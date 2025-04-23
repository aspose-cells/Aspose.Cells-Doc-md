---
title: Çalışma Kitabı Sıkıştırma Seviyesini Ayarlayın
type: docs
weight: 130
url: /tr/java/adjust-workbook-compression-level/
---

## **Çalışma kitabının sıkıştırma seviyesi ayarlanabilir.**

Geliştiriciler, daha büyük çalışma kitaplarıyla çalışırken çalışma kitabının sıkıştırma seviyesini ayarlayabilirler. Geliştiriciler, dosya boyutlarını işleme süresinin üzerine tercih edebilir ya da tam tersi. Aspose.Cells, çalışma kitabının sıkıştırma seviyesini ayarlamanızı sağlayan [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) numaralı sınıfı sağlar. [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) sınıfı aşağıdaki üyeleri sağlar.

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1): En hızlı ama en az etkili sıkıştırma.
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-2): Düzey 1'den biraz daha yavaş, ama daha iyi.
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-3): Düzey 2'den biraz daha yavaş, ama daha iyi.
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-4): Düzey 3'ten biraz daha yavaş, ama daha iyi.
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-5): Düzey 4'ten biraz daha yavaş, ama daha iyi sıkıştırma.
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6): Hız ve sıkıştırma verimliliğinin iyi bir dengesi.
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-7): Oldukça iyi sıkıştırma!
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-8): Düzey7'den daha iyi sıkıştırma!
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9): "En iyi" sıkıştırma, en iyi, en büyük giriş veri akışının boyutunda en büyük azalma demektir. Aynı zamanda en yavaş sıkıştırmadır.

Aşağıdaki kod parçacığı, [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) sınıfının kullanımını gösterir ve [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1), [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6) ve [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9) için dönüşüm sürelerini karşılaştırır. Ayrıca oluşturulan dosyaların boyutlarını da karşılaştırabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
{{< app/cells/assistant language="java" >}}
