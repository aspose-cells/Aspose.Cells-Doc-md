---
title: Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın
type: docs
weight: 320
url: /tr/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aspose.Cells for Python via .NET API kullanarak otomatik filtrelemeyi yeniden yükledikten sonra tüm gizli satır endekslerini nasıl alacağınızı öğrenin.
keywords: Python Excel Kütüphanesi, Python Otomatik Filtrelemeyi Yeniden Yükleme Sonrası Tüm Gizlenen Satır Dizini Almayı, Python Otomatik Filtrelemeyi Yeniden Yükleme Sonrası Tüm Gizlenen Satır Dizini Almayı, Python Otomatik Filtrelemeyi Yeniden Yükleme Sonrası Tüm Gizlenen Satır Endekslerini Almayı Almayı
---

## **Olası Kullanım Senaryoları**

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda bazı satırlar otomatik olarak gizlenir. Ancak bazı satırların Excel son kullanıcısı tarafından manuel olarak zaten gizlenmiş olabilir ve bunlar otomatik filtre tarafından gizlenmemiş olabilir. Bu nedenle hangi satırların otomatik filtre tarafından gizlendiğini ve hangilerinin Excel son kullanıcısı tarafından manuel olarak gizlendiğini bilmek zor olabilir. Aspose.Cells for Python via .NET, bu sorunu çözmek için [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) metodu kullanır. Bu metod otomatik filtre tarafından gizlenen tüm satırların end Excel end kullanıcısı tarafından manuel olarak gizlenmeyen satırların end satır indislerini döndürür.

## **Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın**

Lütfen, aşağıdaki örnek kodu inceleyin, bu kod, Excel son kullanıcısı tarafından manuel olarak gizlenmiş bazı satırları içeren [örneği Excel dosyasını](64716909.xlsx) yükler. Kod, otomatik filtreyi uygular ve [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) metodu kullanarak yeniler, otomatik filtre tarafından gizlenen tüm satırların end satır indislerini döndürür. Daha sonra gizli satırların end indislerini ve hücre adlarını ve değerlerini konsolda yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
