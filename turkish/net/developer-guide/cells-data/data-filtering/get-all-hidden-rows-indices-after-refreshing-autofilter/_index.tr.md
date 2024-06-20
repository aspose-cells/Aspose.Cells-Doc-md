---
title: Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın
type: docs
weight: 320
url: /tr/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aspose.Cells for .NET API sını kullanarak AutoFilter yenilendikten sonra tüm gizli satır dizinlerini nasıl alacağınızı öğrenin.
keywords: AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Alın, AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Elde Edin, AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Alın
---

## **Olası Kullanım Senaryoları**

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda, bazı satırlar otomatik olarak gizlenir. Ancak bazı durumlarda, bazı satırlar otomatik filtre ile gizlenmeden önce Excel kullanıcısı tarafından manuel olarak gizlenmiş olabilir. Bu durumda, hangi satırların otomatik filtre tarafından gizlendiğini ve hangilerinin Excel kullanıcısı tarafından manuel olarak gizlendiğini bilmek zor olabilir. Aspose.Cells, bu problemi int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) yöntemi ile çözer. Bu yöntem, otomatik filtre tarafından gizlenen tüm satırların dizinlerini ve Excel kullanıcısı tarafından manuel olarak gizlenmeyen tüm satırların dizinlerini döndürür.

## **Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın**

Aşağıdaki örnek kod, Excel kullanıcısı tarafından manuel olarak gizlenen bazı satırları içeren [örnek Excel dosyasını](64716909.xlsx) yükler. Kod, otomatik filtre uygular, int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) yöntemini kullanarak otomatik olarak gizlenen tüm satırların dizarlarını döndürür. Daha sonra gizli satırların dizinlerini hücre adları ve değerleri ile birlikte konsola yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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
