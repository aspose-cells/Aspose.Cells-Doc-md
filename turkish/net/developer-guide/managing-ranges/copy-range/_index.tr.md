---
title: Excel in Kopyalanması
linktitle: Kopya Aralıkları
type: docs
weight: 105
url: /tr/net/copy-ranges-of-Excel/
---

## **Giriş**

Excel'de bir aralığı seçebilir, ardından bu aralığı belirli seçeneklerle aynı çalışma sayfasına, diğer çalışma sayfalarına veya diğer dosyalara yapıştırabilirsiniz.

## **Aspose.Cells Kullanarak Aralıkları Kopyalama**

Aspose.Cells, aralığı kopyalamak için bazı aşırı yüklemeli [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) yöntemleri sunar.
Ve [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) sadece aralığın kopya stilini; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) yalnızca aralığın kopya değerini alır

## **Aralık Kopyalama**

İki aralık oluşturarak: kaynak aralık, hedef aralık, ardından Range.Copy yöntemi ile kaynak aralığı hedef aralığa kopyalama.

Aşağıdaki kodu görün:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Seçeneklerle Aralık Yapıştırma**

Aspose.Cells, belirli bir türle aralığı yapıştırmayı destekler.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Yalnızca Aralık Verilerini Kopyalama**
Ayrıca aşağıdaki kodları kullanarak verileri Range.CopyData yöntemiyle kopyalayabilirsiniz:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Gelişmiş Konular**
- [Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Kopyalama](/cells/tr/net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="csharp" >}}
