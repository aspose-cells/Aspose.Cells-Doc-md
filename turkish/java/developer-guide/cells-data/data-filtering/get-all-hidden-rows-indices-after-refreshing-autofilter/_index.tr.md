---
title: Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın
type: docs
weight: 240
url: /tr/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Olası Kullanım Senaryoları**

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda, bazı satırlar otomatik olarak gizlenir. Ancak bazı satırlar Excel son kullanıcısı tarafından manuel olarak zaten gizlenmiş olabilir ve bunlar otomatik filtre tarafından gizlenmemiş olabilir. Bu durumda, hangi satırların otomatik filtre tarafından gizlendiğini ve hangilerinin Excel son kullanıcısı tarafından manuel olarak gizlendiğini bilmek zor olabilir. Aspose.Cells, bu problemi Excel son kullanıcısı tarafından manuel olarak gizlenmeyen tüm satırların satır dizinlerini döndüren int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-) yöntemini kullanarak çözüyor.

## **Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın**

Lütfen, Excel son kullanıcısı tarafından manuel olarak gizlenen bazı satırları içeren [örnek Excel dosyasını](64716913.xlsx) yükleyen ve auto filtre uygulayan aşağıdaki örnek kodu görün. Kod, int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-) yöntemini kullanarak auto filtre tarafından gizli satırların satır dizinlerini döndürür. Daha sonra gizli satırların indislerini hücre adları ve değerleri ile birlikte konsola yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
{{< app/cells/assistant language="java" >}}
