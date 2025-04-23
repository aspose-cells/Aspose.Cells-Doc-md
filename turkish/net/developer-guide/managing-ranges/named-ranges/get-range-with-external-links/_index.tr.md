---
title: Harici Bağlantıları İçeren Menzil Al
type: docs
weight: 120
url: /tr/net/get-range-with-external-links/
---

## **Harici Bağlantıları Olan Aralığı Al**

Çoğu zaman Excel dosyaları, dış bağlantılı bağlantıları kullanarak diğer Excel dosyalarından veriye erişir. Aspose.Cells, bu dış bağlantıları almak için [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) yöntemini kullanma seçeneği sağlar. [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) yöntemi bir [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) türünde bir dizi döndürür. [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) sınıfı, bir [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename) özelliği döndüren bir sınıftır. [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) sınıfı, aşağıdaki üyeleri açığa çıkarır.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Alanın son sütunu
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Alanın son satırı
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Bu harici bir başvuru ise harici dosya adını al
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Bu bir alan mı belirtir
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Bu bir harici bağlantı mı belirtir
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Bu başvurunun hangi tabloda olduğunu belirtir
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Alanın başlangıç sütunu
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Alanın başlangıç satırı

Aşağıdaki örnek kod, [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) yöntemi kullanarak Dış Bağlantılı Aralıkları almanın kullanımını gösterir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
