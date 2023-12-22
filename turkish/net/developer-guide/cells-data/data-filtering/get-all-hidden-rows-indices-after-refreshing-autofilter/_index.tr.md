---
title: Otomatik Filtreyi Yeniledikten Sonra Tüm Gizli Satır Dizinlerini Al
type: docs
weight: 320
url: /tr/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aspose.Cells for .NET API'i kullanarak Otomatik Filtreyi yeniledikten sonra tüm gizli satır dizinlerini nasıl alacağınızı öğrenin.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **Olası Kullanım Senaryoları**

Otomatik filtreyi çalışma sayfası hücrelerine uyguladığınızda bazı satırlar otomatik olarak gizlenir. Ancak bazı satırların Excel son kullanıcısı tarafından manuel olarak gizlenmiş olması ve otomatik filtreyle gizlenmemiş olması da söz konusu olabilir. Bu nedenle hangi satırların otomatik filtre tarafından gizlendiğini ve hangilerinin Excel son kullanıcısı tarafından manuel olarak gizlendiğini bilmek zorlaştırır. Aspose.Cells bu sorunla int[] kullanarak ilgilenir[**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)yöntem. Bu yöntem, Excel son kullanıcısı tarafından manuel olarak değil, otomatik filtre tarafından gizlenen tüm satırların satır dizinlerini döndürür.

##  **Otomatik Filtreyi Yeniledikten Sonra Tüm Gizli Satır Dizinlerini Al**

 Lütfen aşağıdaki örnek koda bakın.[örnek Excel dosyası](64716909.xlsx) Excel son kullanıcısı tarafından manuel olarak gizlenen bazı satırları içerir. Kod, otomatik filtreyi uygular ve int[] kullanarak onu yeniler.[**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)Otomatik filtreyle tüm gizli satırların satır indekslerini döndüren yöntem. Daha sonra konsoldaki gizli satırların indekslerini hücre adları ve değerleriyle birlikte yazdırır.

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **Konsol Çıkışı**

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
