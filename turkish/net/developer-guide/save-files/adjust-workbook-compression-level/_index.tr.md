---
title: Çalışma kitabı sıkıştırma düzeyini ayarla
type: docs
weight: 180
url: /tr/net/adjust-workbook-compression-level/
---
## **Çalışma Kitabı Sıkıştırma Düzeyini Ayarla**

Geliştiriciler, daha büyük çalışma kitaplarıyla çalışırken çalışma kitabının sıkıştırma düzeyini ayarlayabilir. Geliştiriciler, işlem süresi yerine daha küçük dosya boyutlarına öncelik verebilir veya bunun tersi de geçerlidir. Aspose.Cells sağlar**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** çalışma kitabının sıkıştırma düzeyini ayarlamak için kullanabileceğiniz numaralandırma. bu**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** numaralandırma aşağıdaki üyeleri sağlar.

- Level1: En hızlı ancak en az etkili sıkıştırma.
- Seviye 2: Seviye 1'den biraz daha yavaş ama daha iyi.
- Seviye 3: Seviye 2'den biraz daha yavaş ama daha iyi.
- Seviye 4: Seviye 3'ten biraz daha yavaş ama daha iyi.
- Level5: Level 4'ten biraz daha yavaş ama daha iyi sıkıştırma ile.
- Level6: İyi bir hız ve sıkıştırma verimliliği dengesi.
- Level7: Oldukça iyi sıkıştırma!
- Level8: Level7'den daha iyi sıkıştırma!
- Düzey9: "en iyi" sıkıştırma, burada en iyi, giriş veri akışının boyutunda en büyük azalma anlamına gelir. Bu aynı zamanda en yavaş sıkıştırmadır.

 Aşağıdaki kod parçacığı, kullanımını gösterir**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**numaralandırır ve Düzey1, Düzey6 ve Düzey9 için dönüştürme süresini karşılaştırır. Oluşturulan dosyaların boyutlarını da karşılaştırabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
