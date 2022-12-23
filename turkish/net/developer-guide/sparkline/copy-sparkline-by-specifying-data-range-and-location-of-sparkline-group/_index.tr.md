---
title: Mini Grafik Grubunun Veri Aralığını ve Konumunu Belirterek Mini Tabloyu Kopyalayın
type: docs
weight: 300
url: /tr/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Excel, bir mini grafik grubunun veri aralığını ve konumunu belirterek bir mini grafiği kopyalamanıza olanak tanır. Aspose.Cells bu özelliği destekler.

{{% /alert %}}

Mini grafiği Microsoft Excel'de diğer hücrelere kopyalamak için:

1. Sparkline'ı içeren hücreyi seçin.
1.  Seçme**Verileri Düzenle** dan**küçük resim** bölümü**Tasarım** sekme.
1.  Seçme**Grup Konumunu ve Verilerini Düzenle**.
1. Veri aralığını ve konumu belirtin.
1.  Tıklamak**Tamam**.

Aspose.Cells, mini grafik grubunun veri aralığını ve konumunu belirtmek için SparklineCollection.Add(dataRange, row, column) yöntemini sağlar. Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ardından ilk mini grafik grubuna erişir ve mini grafik grubuna veri aralıkları ve konumlar ekler. Son olarak, yukarıdaki ekran görüntüsünde de gösterilen çıktı Excel dosyasını diske yazar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
