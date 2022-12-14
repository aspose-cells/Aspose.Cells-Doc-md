---
title: Excel Aralıklarını Kopyala
linktitle: Aralıkları Kopyala
type: docs
weight: 105
url: /tr/net/copy-ranges-of-Excel/
---
## **giriiş**

Excel'de bir aralık seçebilir, aralığı kopyalayabilir ve ardından belirli seçeneklerle aynı çalışma sayfasına, diğer çalışma sayfalarına veya diğer dosyalara yapıştırabilirsiniz.

## **Aspose.Cells Kullanarak Aralıkları Kopyala**

 Aspose.Cells biraz aşırı yük sağlıyor[Aralık.Kopya](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) aralığı kopyalama yöntemleri.
 Ve[Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) aralığın yalnızca kopyalama stili;[Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) aralığın yalnızca kopya değeri

## **Aralığı Kopyala**

İki aralık oluşturma: kaynak aralık, hedef aralık, ardından kaynak aralığın Range.Copy yöntemiyle hedef aralığa kopyalanması.

Aşağıdaki koda bakın:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Aralığı Seçeneklerle Yapıştır**

Aspose.Cells, aralığın belirli bir türle yapıştırılmasını destekler.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Yalnızca Aralığın Verilerini Kopyalayın.**
Ayrıca Range.CopyData yöntemi ile aşağıdaki kodlar gibi verileri kopyalayabilirsiniz:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **ileri konular**
- [Kaynak Aralığının Satır Yüksekliklerini Hedef Aralığa Kopyala](/cells/tr/net/copy-row-heights-of-source-range-to-destination-range/)


