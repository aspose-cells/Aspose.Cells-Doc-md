---
title: Excel in Kopyalanması
linktitle: Kopya Aralıkları
type: docs
weight: 30
url: /tr/java/copy-ranges-of-Excel/
---

## **Giriş**

Excel'de bir aralığı seçebilir, ardından bu aralığı belirli seçeneklerle aynı çalışma sayfasına, diğer çalışma sayfalarına veya diğer dosyalara yapıştırabilirsiniz.

## **Aspose.Cells Kullanarak Aralıkları Kopyalama**

Aspose.Cells, aralığı kopyalamak için bazı aşırı yüklemeye sahip [Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range) yöntemleri sağlar.
## **Aralık Kopyalama**

İki aralık oluşturarak: kaynak aralık, hedef aralık, ardından Range.Copy yöntemi ile kaynak aralığı hedef aralığa kopyalama.

Aşağıdaki kodu görün:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Seçeneklerle Aralık Yapıştırma**

Aspose.Cells, belirli bir türle aralığı yapıştırmayı destekler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Yalnızca Aralığın Verilerini Kopyalama.**
Ayrıca aşağıdaki kodları kullanarak verileri Range.CopyData yöntemiyle kopyalayabilirsiniz:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


