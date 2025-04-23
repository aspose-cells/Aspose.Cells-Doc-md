---  
title: Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın 
type: docs  
weight: 320  
url: /tr/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: AutoFilter ı yeniledikten sonra tüm gizlenmiş satırların dizinlerini almak için Aspose.Cells for Node.js via C++ API sini kullanmayı öğrenin.  
keywords: Node.js kullanarak AutoFilter ı yeniledikten sonra tüm gizlenmiş satırların dizinlerini elde edin, C++ kullanarak AutoFilter ı yeniledikten sonra tüm gizlenmiş satırların dizinlerini alın, C++ kullanarak AutoFilter ı yeniledikten sonra tüm gizlenmiş satırların dizinlerini alın.  
---  

## **Olası Kullanım Senaryoları**  

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda, bazı satırlar otomatik olarak gizlenir. Ancak, bazı satırlar Excel kullanıcıları tarafından manuel olarak gizlenmiş olabilir ve otomatik filtre tarafından gizlenmemiştir. Bu durumda, hangi satırların otomatik filtre ile gizlendiğini ve hangilerinin manuel olarak saklandığını bilmek zorlaşır. Aspose.Cells for Node.js via C++, bu sorunu [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-) dizisi kullanarak çözer. Bu yöntem, otomatik filtre tarafından gizlenen, ancak manuel olarak gizlenmeyen satırların dizinlerini döndürür.  

## **Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın**  

Lütfen aşağıdaki örnek kodu inceleyin; bu kod, bazı satırların Excel kullanıcıları tarafından manuel olarak gizlendiği [örnek Excel dosyasını](64716909.xlsx) yükler. Kod, otomatik filtre uygular ve `[**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-)` yöntemi kullanarak tüm gizlenmiş satırların satır dizinlerini döndürür. Ardından, gizlenmiş satırların dizinlerini, hücre isimleri ve değerleriyle birlikte konsola yazdırır.  

## **Örnek Kod**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


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
