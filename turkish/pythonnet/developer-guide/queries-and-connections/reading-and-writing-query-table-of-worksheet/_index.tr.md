---
title: Çalışsaydı, Çalışma Sorgusu Tablosu Okuma ve Yazma
type: docs
weight: 40
url: /tr/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, Worksheet.QueryTables koleksiyonunu sağlar; bu koleksiyon, index ile QueryTable nesnesi döndürür. Kullanılabilecek iki özellik vardır

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Bunlar her ikisi de Boolean değerlerdir. Bunları Microsoft Excel'de Veri > Bağlantılar > Özellikler menüsünde görebilirsiniz.

{{% /alert %}}

## Çalışsayfa Sorgu Tablosu Okuma ve Yazma

Aşağıdaki örnek kod, ilk çalışsayfanın ilk Sorgu Tablosunu okur ve ardından Sorgu Tablosunun her iki özelliğini de yazdırır. Daha sonra QueryTable.PreserveFormatting özelliğini true olarak ayarlar.

Bu kodda kullanılan kaynak Excel dosyasını ve kod tarafından oluşturulan çıktı Excel dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

- [Kaynak Excel Dosyası](5115533.xlsx)
- [Çıktı Excel Dosyası](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### Konsol Çıktısı

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Sorgu tablosu sonuç aralığını alın

Aspose.Cells for Python via .NET, sorgu tablosunun adresi yani sonuç aralığını okuma seçeneği sağlar. Aşağıdaki kod, bu özelliği kullanarak sorgu tablosunun sonuç aralığının adresini okumayı gösterir. Örnek dosya [buradan](72417290.xlsx) indirilebilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

{{< app/cells/assistant language="python-net" >}}
