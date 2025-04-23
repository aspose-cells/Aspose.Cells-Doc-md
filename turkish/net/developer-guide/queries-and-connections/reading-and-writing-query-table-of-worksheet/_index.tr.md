---
title: Çalışsaydı, Çalışma Sorgusu Tablosu Okuma ve Yazma
type: docs
weight: 40
url: /tr/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells, İçerikSorgusunu döndüren Worksheet.QueryTables koleksiyonunu sağlar. Bu koleksiyon bir endekse göre QueryTable türünde bir nesne döndürür. Aşağıdaki iki özelliğe sahiptir

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Bunlar her ikisi de Boolean değerlerdir. Bunları Microsoft Excel'de Veri > Bağlantılar > Özellikler menüsünde görebilirsiniz.

{{% /alert %}}

## Çalışsayfa Sorgu Tablosu Okuma ve Yazma

Aşağıdaki örnek kod, ilk çalışsayfanın ilk Sorgu Tablosunu okur ve ardından Sorgu Tablosunun her iki özelliğini de yazdırır. Daha sonra QueryTable.PreserveFormatting özelliğini true olarak ayarlar.

Bu kodda kullanılan kaynak Excel dosyasını ve kod tarafından oluşturulan çıktı Excel dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

- [Kaynak Excel Dosyası](5115533.xlsx)
- [Çıktı Excel Dosyası](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Konsol Çıktısı

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Sorgu tablosu sonuç aralığını alın

Aspose.Cells, bir sorgu tablosu için hücrelerin adresini yani sonuç aralığını okuma seçeneği sağlar. Aşağıdaki kod, bir sorgu tablosunun sonuç aralığının adresini okuyarak bu özelliği göstermektedir. Örnek dosyayı [buradan](72417290.xlsx) indirebilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
