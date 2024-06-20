---
title: Harici Bağlantıları İçeren Menzil Al
type: docs
weight: 140
url: /tr/java/get-range-with-external-links/
---

## **Harici Bağlantıları Olan Aralığı Al**

Çoğu zaman Excel dosyaları diğer Excel dosyalarından veri erişimi yapar ve bunu harici bağlantılar kullanarak yapar. Aspose.Cells, bu harici bağlantıları [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) yöntemini kullanarak almak için seçenek sunar. [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) yöntemi, [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) türünde bir dizi döndürür. [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) sınıfı, harici dosyanın adını döndüren bir özellik olan bir [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName) özelliği sağlar. [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) sınıfı, aşağıdaki üyeleri açığa çıkarır.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Alanın son sütunu
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Alanın son satırı
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Bu harici bir başvuru ise harici dosya adını al
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Bu bir alan mı belirtir
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Bu bir harici bağlantı mı belirtir
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Bu başvurunun hangi tabloda olduğunu belirtir
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Alanın başlangıç sütunu
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Alanın başlangıç satırı

Aşağıda verilen örnek kod, harici bağlantıları içeren menzilleri almak için [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) yönteminin kullanımını gösterir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
