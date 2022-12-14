---
title: Çalışma Sayfasının Sorgu Tablosunu Okuma ve Yazma
type: docs
weight: 40
url: /tr/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells, dizine göre QueryTable türündeki nesneyi döndüren Worksheet.QueryTables koleksiyonu sağlar. Aşağıdaki iki özelliğe sahiptir

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Bunların her ikisi de Boole değerleridir. Bunları Microsoft Excel'de Veri > Bağlantılar > Özellikler aracılığıyla görüntüleyebilirsiniz.

{{% /alert %}}

## Çalışma Sayfasının Sorgu Tablosunu Okuma ve Yazma

Aşağıdaki örnek kod, ilk çalışma sayfasının ilk QueryTable'ını okur ve ardından QueryTable özelliklerinin her ikisini de yazdırır. Sonra QueryTable.PreserveFormatting'i true olarak ayarlar.

Bu kodda kullanılan kaynak Excel dosyasını ve kodun oluşturduğu çıktı Excel dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

- [Kaynak Excel Dosyası](5115533.xlsx)
- [Çıktı Excel Dosyası](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Konsol Çıkışı

İşte yukarıdaki örnek kodun konsol çıktısı

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Sorgu tablosu sonuç aralığını al

 Aspose.Cells, bir sorgu tablosu için adresi, yani sonuç hücre aralığını okuma seçeneği sunar. Aşağıdaki kod, bir sorgu tablosu için sonuç aralığının adresini okuyarak bu özelliği gösterir. Örnek dosya indirilebilir[burada](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
