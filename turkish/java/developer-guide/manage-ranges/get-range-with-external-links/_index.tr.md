---
title: Harici Bağlantılarla Menzil Alın
type: docs
weight: 140
url: /tr/java/get-range-with-external-links/
---
## **Harici Bağlantılarla Menzil Alın**

Çoğu zaman Excel dosyaları, dış bağlantıları kullanarak diğer Excel dosyalarındaki verilere erişir. Aspose.Cells, bu harici bağlantıları kullanarak alma seçeneği sunar.[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) yöntem. bu[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) yöntemi bir tür dizisi döndürür[**YönlendirilenAlan**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). bu[**YönlendirilenAlan**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)sınıf bir sağlar[**HariciDosyaAdı**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)harici dosyanın adını döndüren özellik. bu[**YönlendirilenAlan**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)sınıf aşağıdaki üyeleri gösterir.

- [**Bitiş Sütunu**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Alanın bitiş sütunu
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Alanın son satırı
- [**HariciDosyaAdı**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Bu bir harici referans ise harici dosya adını alın
- [**alan**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Bunun bir alan olup olmadığını gösterir
- [**Harici Bağlantı**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Bunun harici bir bağlantı olup olmadığını gösterir
- [**SayfaAdı**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Bu referansın hangi sayfada olduğunu gösterir
- [**Başlat Sütunu**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Alanın başlangıç sütunu
- [**Satırı Başlat**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Alanın başlangıç satırı

Aşağıda verilen örnek kod,[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) harici bağlantılarla Aralıkları alma yöntemi.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
