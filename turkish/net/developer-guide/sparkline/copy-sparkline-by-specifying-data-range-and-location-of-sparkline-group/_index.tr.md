---
title: Belirli Veri Aralığını ve Sparkline Grubu Konumunu Belirterek Sparkline Kopyalama
type: docs
weight: 300
url: /tr/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel, bir sparkline grubunun veri aralığını ve konumunu belirterek bir sparkline kopyalamanıza izin verir. Aspose.Cells, bu özelliği destekler.

{{% /alert %}}

Microsoft Excel'de sparkline kopyalamak için:

1. Sparkline içeren hücreyi seçin.
1. **Tasarım** sekmesinin **Sparkline** bölümünden **Veri Düzenle**'yi seçin.
1. **Grup Konumunu ve Veriyi Düzenle**'yi seçin.
1. Veri aralığını ve konumu belirtin.
1. **Tamam**'a tıklayın.

Aspose.Cells, SparklineCollection.Add(dataRange, row, column) yöntemini kullanarak bir sparkline grubunun veri aralığını ve konumunu belirtir. Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ardından ilk sparkline grubuna erişir ve sparkline grubunda veri aralıklarını ve konumları ekler. Son olarak, çıktı Excel dosyasını diskte yazarak ekran görüntüsünde de gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
