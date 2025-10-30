---
title: C++ ile Golang kullanarak Sparkline ı Kopyalayın, veri aralığını ve Sparkline grubunun konumunu belirtin
linktitle: Veri Aralığını ve Konumu Belirterek Sparkline Kopyalama
type: docs
weight: 300
url: /tr/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Aspose.Cells for C++ kullanarak veri aralığını ve konumu belirterek sparklines nasıl kopyalanır öğrenin.
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

Aspose.Cells, sparkline grubunun veri aralığını ve konumunu belirlemek için `SparklineCollection.Add(dataRange, row, column)` metodunu sağlar. Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ilk sparkline grubuna erişir ve ona veri aralıklarını ve konumlarını ekler. Sonunda, çıktıyı diske kaydeder ve bu da yukarıdaki ekran görüntüsünde gösterilmiştir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
