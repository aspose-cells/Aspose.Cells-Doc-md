---
title: Belirli Veri Aralığını ve Sparkline Grubu Konumunu Belirterek Sparkline Kopyalama
type: docs
weight: 300
url: /tr/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel, veri aralığını ve bir sparkline grubunun konumunu belirterek bir sparkline'yi kopyalamanıza olanak tanır. Aspose.Cells for Python via .NET bu özelliği destekler.

{{% /alert %}}

Microsoft Excel'de sparkline kopyalamak için:

1. Sparkline içeren hücreyi seçin.
1. **Tasarım** sekmesinin **Sparkline** bölümünden **Veri Düzenle**'yi seçin.
1. **Grup Konumunu ve Veriyi Düzenle**'yi seçin.
1. Veri aralığını ve konumu belirtin.
1. **Tamam**'a tıklayın.

Aspose.Cells for Python via .NET, SparklineCollection.Add(dataRange, satır, sütun) metodunu sağlar; böylece sparkline grubunun veri aralığını ve konumunu belirleyebilirsiniz. Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ilk sparkline grubuna erişir ve veri aralıkları ile konumlar ekler. Son olarak, çıktı Excel dosyasını disk üzerinde yazar, bu da yukarıdaki ekran görüntüsünde gösterilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
