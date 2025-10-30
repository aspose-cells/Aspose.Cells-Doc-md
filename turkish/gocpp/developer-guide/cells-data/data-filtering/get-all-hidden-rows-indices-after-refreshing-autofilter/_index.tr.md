---
title: Golang ve C++ kullanarak Yenileme sonrası Tüm Gizli Satırların Dizilerini Alma
linktitle: Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın
type: docs
weight: 320
url: /tr/go-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aspose.Cells for C++ API’sini kullanarak AutoFilter yenilendikten sonra tüm gizli satır dizilerini nasıl alacağınızı öğrenin.
keywords: AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Alın, AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Elde Edin, AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Alın
---

## **Olası Kullanım Senaryoları**

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda, bazı satırlar otomatik olarak gizlenir. Ancak bazı durumlarda, bazı satırlar otomatik filtre ile gizlenmeden önce Excel kullanıcısı tarafından manuel olarak gizlenmiş olabilir. Bu durumda, hangi satırların otomatik filtre tarafından gizlendiğini ve hangilerinin Excel kullanıcısı tarafından manuel olarak gizlendiğini bilmek zor olabilir. Aspose.Cells, bu problemi int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/) yöntemi ile çözer. Bu yöntem, otomatik filtre tarafından gizlenen tüm satırların dizinlerini ve Excel kullanıcısı tarafından manuel olarak gizlenmeyen tüm satırların dizinlerini döndürür.

## **Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın**

Aşağıdaki örnek kod, Excel kullanıcısı tarafından manuel olarak gizlenen bazı satırları içeren [örnek Excel dosyasını](64716909.xlsx) yükler. Kod, otomatik filtre uygular, int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/) yöntemini kullanarak otomatik olarak gizlenen tüm satırların dizarlarını döndürür. Daha sonra gizli satırların dizinlerini hücre adları ve değerleri ile birlikte konsola yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAllHiddenRowsIndicesAfterRefreshingAutofilter.go" >}}
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
