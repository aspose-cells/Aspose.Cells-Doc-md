---
title: Harici Bağlantılarla Menzil Alın
type: docs
weight: 120
url: /tr/net/get-range-with-external-links/
---
## **Harici Bağlantılarla Menzil Alın**

Çoğu zaman Excel dosyaları, dış bağlantıları kullanarak diğer Excel dosyalarındaki verilere erişir. Aspose.Cells, bu harici bağlantıları kullanarak alma seçeneği sunar.[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)yöntem. bu[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)yöntem bir tür dizisi döndürür[**YönlendirilenAlan**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). bu[**YönlendirilenAlan**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) sınıf bir sağlar[**HariciDosyaAdı**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)harici dosyanın adını döndüren özellik. bu[**YönlendirilenAlan**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)sınıf aşağıdaki üyeleri gösterir.

- [**Bitiş Sütunu**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Alanın bitiş sütunu
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Alanın son satırı
- [**HariciDosyaAdı**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Bu bir harici referans ise harici dosya adını alın
- [**alan**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Bunun bir alan olup olmadığını gösterir
- [**Harici Bağlantı**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Bunun harici bir bağlantı olup olmadığını gösterir
- [**SayfaAdı**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Bu referansın hangi sayfada olduğunu gösterir
- [**Başlat Sütunu**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Alanın başlangıç sütunu
- [**Satırı Başlat**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Alanın başlangıç satırı

 Aşağıda verilen örnek kod,[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)Harici bağlantılarla Aralıkları alma yöntemi.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
