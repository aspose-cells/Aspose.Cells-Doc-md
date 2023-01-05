---
title: AutoFilter'ı Yeniledikten Sonra Tüm Gizli Satır Dizinlerini Alın
type: docs
weight: 240
url: /tr/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **Olası Kullanım Senaryoları**

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda, bazı satırlar otomatik olarak gizlenir. Ancak, bazı satırların zaten Excel son kullanıcısı tarafından manuel olarak gizlendiği ve otomatik filtre tarafından gizlenmediği durum olabilir. Bu nedenle, hangi satırların otomatik filtre tarafından gizlendiğini ve hangilerinin Excel son kullanıcısı tarafından manuel olarak gizlendiğini bilmeyi zorlaştırır. Aspose.Cells int[] kullanarak bu sorunu çözer[**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) yöntem. Bu yöntem, Excel son kullanıcısı tarafından manuel olarak değil, otomatik filtre tarafından gizlenen tüm satırların satır dizinlerini döndürür.

## **AutoFilter'ı Yeniledikten Sonra Tüm Gizli Satır Dizinlerini Alın**

Lütfen yükleyen aşağıdaki örnek koda bakın.[örnek excel dosyası](64716913.xlsx)Excel son kullanıcısı tarafından manuel olarak gizlenen bazı satırları içerir. Kod, otomatik filtreyi uygular ve int[] kullanarak yeniler.[**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) tüm gizli satırların satır dizinlerini otomatik filtre ile döndüren yöntem. Daha sonra, hücre adları ve değerleri ile birlikte konsoldaki gizli satırların dizinlerini yazdırır.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

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
