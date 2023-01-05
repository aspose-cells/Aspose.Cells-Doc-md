---
title: Çalışma kitabı sıkıştırma düzeyini ayarla
type: docs
weight: 130
url: /tr/java/adjust-workbook-compression-level/
---
## **Çalışma kitabı sıkıştırma düzeyini ayarla**

Geliştiriciler, daha büyük çalışma kitaplarıyla çalışırken çalışma kitabının sıkıştırma düzeyini ayarlayabilir. Geliştiriciler, işlem süresi yerine daha küçük dosya boyutlarına öncelik verebilir veya bunun tersi de geçerlidir. Aspose.Cells sağlar**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**çalışma kitabının sıkıştırma düzeyini ayarlamak için kullanabileceğiniz numaralandırma. bu**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** numaralandırma aşağıdaki üyeleri sağlar.

- **[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: En hızlı ancak en az etkili sıkıştırma.
- **[LEVEL_2](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: 1. seviyeden biraz daha yavaş ama daha iyi.
- **[LEVEL_3](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**Seviye 2'den biraz daha yavaş ama daha iyi.
- **[LEVEL_4](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: 3. seviyeden biraz daha yavaş ama daha iyi.
- **[LEVEL_5](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: Seviye 4'ten biraz daha yavaş, ancak daha iyi sıkıştırma ile.
- **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**: İyi bir hız ve sıkıştırma verimliliği dengesi.
- **[LEVEL_7](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: Oldukça iyi sıkıştırma!
- **[LEVEL_8](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: Level7'den daha iyi sıkıştırma!
- **[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**"En iyi" sıkıştırma, burada en iyi, giriş veri akışının boyutunda en büyük azalma anlamına gelir. Bu aynı zamanda en yavaş sıkıştırmadır.

Aşağıdaki kod parçacığı, kullanımını gösterir**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** numaralandırma ve dönüşüm süresini karşılaştırır**[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)** , ve**[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**. Oluşturulan dosyaların boyutlarını da karşılaştırabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
